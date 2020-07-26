from .Formatting import Bold, Newline, Header, ListLines
from .NSCGenUtils import NameToSeed, DrawWithWeights,StartCapital,InsertWordAtSpace
from .config import baseURL

import random
import json

einstellungVamp = {
    'Trinken': {
        'Praktik': [
            'trinkt Blut meist indirekt (Gläser, Spritzen, Blutbeutel o.ä.)',
            'trinkt Blut meist  aus dem Hals',
            'trinkt Blut meist aus dem Handgelenk',
            'trinkt Blut meist an anderen Körperstellen',
            'trinkt Blut meist über einen Kuss (beisst in Lippe oder Zunge)',
            'tötet beim Bluttrinken',
            'trinkt meist Tierblut',
            'trinkt nur von bekannten Gefäßen (Herde)',
            'trinkt nur Blut aus Blutbanken',
        ],
        'Einstellung': [
            'verabscheut das Bluttrinken und trinkt nur im Notfall indirekt oder in Raserei',
            'hasst das Bluttrinken',
            'liebt das Bluttrinken',
            'betrachtet es nüchtern als Nahrungsaufnahme'
            'liebt Blut mit Rauschmitteln (Drogen, Alkohol o.ä.)',
            'liebt Blut mit starken Emotionen (Angst, Leidenschaft o.ä.)',
            'bevorzugt sehr exotischen Bluttyp (wie Ventrue)',
            'hat Angst vor dem Bluttrinken und braucht das Überwindung',
        ]
    },
    'Sterbliche': [
        'verabscheut Sterbliche',
        'sieht sich selbst auf demselben Level wie Sterbliche',
        'genießt die Gesellschaft von Sterblichen',
        'betrachtet Sterbliche als niedere Kreaturen',
        'betrachtet Sterbliche als dumme unwissende Kreaturen',
        'hat Angst vor Menschen',
        'fühlt sich von Menschen verfolgt (Paranoia)',
        'sieht Sterbliche als Schützdenswert an',
    ],
    'Maskerade': [],
    'Camarilla': [],
    'Anarchen': [],
    'Sabbat': [],
}

sekten = {
    'Camarilla': 1,
    'Anarchen': 1,
    'Sabbat': 1
}

disziplinen = {

}

clans = {
    'Assamiten': 1,
    'Brujah': 1,
    'Gangrel': 1,
    'Giovanni': 1,
    'Jünger des Set': 1,
    'Lasombra': 1,
    'Malkavianer': 1,
    'Nosferatu': 1,
    'Ravnos': 1,
    'Toreador': 1,
    'Tremere': 1,
    'Tzimisce': 1,
    'Ventrue': 1,
    'Caitiff': 1
}

unleben = {
    'Verlust des Erzeugers': '',
    'Zeugen eines Kindes': '',
    'Starre': ['für ein paar Tage', 'über einige Monate hinweg', 'längere Zeit'],
    'Lossagung vom Erzeuger': '',
    'Umzug in neue Domäne': ['in eine andere Stadt', 'in ein anderes Land', 'auf einen anderen Kontinent'],
    'Aufnehmen eines Amtes': ['ein niederes Amt', 'ein inoffizielles Amt', 'ein höheres Amt'],
    'Niederlegen eines Amtes': '',
    'Beginn eines Streites mit anderem Vampir': '',
    'Sieg in einem Streit': '',
    'Niederlage in einem Streit': '',
    'Ende eines Streites mit anderem Vampir': '',
    'Beginn einer Liebschaft': '',
    'Ende einer Liebschaft': '',
}

# region stuff
kuss = {
    'legalität': ['mit Erlaubnis', 'im Geheimen', 'ohne Erlaubnis'],
    'beweggrund': ['Liebe', 'Bewunderung', 'einem Bedürfnis', 'Gier nach Macht', 'Hang zur Rebellion', 'Pflichtgefühl']
}

GhulLookup = {
    -1: [0, 1],
    0: [0, 1],
    1: [0, 2],
    2: [1, 2],
    3: [1, 3],
    5: [1, 4],
    6: [2, 5],
    7: [3, 6],
    8: [3, 6],
    9: [3, 7],
    10: [2, 5],
    11: [2, 4],
    12: [1, 3],
}

GenerationLookup = {
    -1: 14,
    0: 13,
    1: 13,
    2: 12,
    3: 11,
    5: 10,
    6: 9,
    7: 8,
    8: 7,
    9: 6,
    10: 5,
    11: 4,
    12: 4,
}

kinderChances = {
    0: 13,
    1: 15,
    2: 1,
    3: 1
}
# endregion

# region Family Tree


def MakeVampireName(nsc):
    from .kinfolkGen import GetRandomVorname, GetRandomNachname
    return GetRandomVorname()+' '+GetRandomNachname()


def MakeChildren(creator, maxDepth=1):
    from .kinfolkGen import GetRandomVorname, GetRandomNachname
    if maxDepth > 0:
        return [{(GetRandomVorname()+' '+GetRandomNachname()): MakeChildren(creator, maxDepth-1)} for _ in range(DrawWithWeights(kinderChances))]
    else:
        return []


def CheckDepth(tree):
    if len(list(tree.values())[0]) > 0:
        return 1 + max([CheckDepth(child) for child in list(tree.values())[0] if len(child) > 0])
    else:
        return 0


def MakeRelationTree(nsc):
    maxDepth = 4
    if nsc['treeSeed'] == -1:
        nsc['Clan'] = DrawWithWeights(clans)
        nsc['treeSeed'] = f'{nsc["vorname"]} {nsc["nachname"]}#{nsc["Powerlevel"]}#{nsc["Clan"]}'
        maxDepth = min(4, 11-nsc['Powerlevel'])
    else:
        nsc['Clan'] = nsc['treeSeed'].split('#')[2]
        maxDepth = min(4, 11-int(nsc['treeSeed'].split('#')[1]))
    NameToSeed(nsc['treeSeed'])
    Creator = MakeVampireName(nsc)
    tree = {Creator: [{nsc['treeSeed'].split('#')[0]:MakeChildren(nsc['treeSeed'])}]+MakeChildren(Creator)}
    while CheckDepth(tree) < maxDepth:
        Creator = MakeVampireName(list(tree.keys())[0])
        tree = {Creator: [tree]+MakeChildren(Creator, CheckDepth(tree))}
    nsc['RelationTree'] = tree
    return nsc


def FindCreator(nsc, tree=None):
    if tree is None:
        tree = nsc['RelationTree']
    if (nsc['vorname']+' '+nsc['nachname']) in map(lambda x: list(x.keys())[0], list(tree.values())[0]):
        return list(tree.keys())[0]
    elif len(list(tree.values())[0]) > 0:
        return [FindCreator(nsc, subTree) for subTree in list(tree.values())[0]][0]


def FindChildren(nsc, tree=None):
    if tree is None:
        tree = nsc['RelationTree']
    if (nsc['vorname']+' '+nsc['nachname']) in list(tree.keys())[0]:
        return list(map(lambda x: list(x.keys())[0], list(tree.values())[0]))
    elif len(list(tree.values())[0]) > 0:
        return [FindChildren(nsc, subTree) for subTree in list(tree.values())[0]][0]


def GetLevelInTree(nsc, tree=None, level=0):
    if tree is None:
        tree = nsc['RelationTree']
    if (nsc['vorname']+' '+nsc['nachname']) in list(tree.keys())[0]:
        return level
    elif (nsc['vorname']+' '+nsc['nachname']) in map(lambda x: list(x.keys())[0], list(tree.values())[0]):
        return level+1
    elif len(list(tree.values())[0]) > 0:
        result = [x for x in [GetLevelInTree(nsc, subTree, level+1) for subTree in list(tree.values())[0]] if x is not None]
        if len(result) > 0:
            return min(result)


def PrintLineageTree(nsc):
    result = '\n<div class="tree"><ul>'
    result += PrintTreeRecursion(nsc)
    result += '</ul></div><div class="clearfix"></div>\n'
    return result


def MakeLink(nsc, Name, Powerlevel, extern=False):
    if extern:
        return baseURL+f'/nsc/vampir/{Powerlevel}/html/{Name.replace(" ","_")}/'
    else:
        return baseURL+f'/nsc/vampir/{Powerlevel}/html/{Name.replace(" ","_")}/?treeSeed={nsc["treeSeed"].replace(" ","_").replace("#","__")}'


def PrintTreeRecursion(nsc, tree=None):
    if tree is None:
        tree = nsc['RelationTree']
    result = '\n<li>\n'
    anchor = {'vorname': nsc['treeSeed'].split('#')[0].split(' ')[0], 'nachname': nsc['treeSeed'].split('#')[0].split(' ')[1]}
    current = {'vorname': list(tree.keys())[0].split(' ')[0], 'nachname': list(tree.keys())[0].split(' ')[1]}
    if nsc['vorname'] == current['vorname'] and nsc['nachname'] == current['nachname']:
        highlight = 'style="background-color:darkred;color:white;"'
    else:
        highlight = ''
    pwLvL = int(nsc['treeSeed'].split('#')[1])+GetLevelInTree(anchor, nsc['RelationTree'])-GetLevelInTree(current, nsc['RelationTree'])
    result += f'<a {highlight} href={MakeLink(nsc,list(tree.keys())[0],pwLvL)}>{list(tree.keys())[0]}</a>'
    if len(list(tree.values())[0]) > 0:
        result += '<ul>\n' + '\n'.join([PrintTreeRecursion(nsc, subTree) for subTree in list(tree.values())[0]])+'\n</ul>\n'
    return result + '\n</li>\n '

# endregion

# region undead history


def MakeUnleben(nsc):
    NameToSeed(nsc['vorname']+' '+nsc['nachname'])
    erzeugerLebt = True
    erzeugerLosgesagt = False
    feinde = []
    liebschaften = []
    aemter = []
    ungezeugteKinder = nsc['Kinder'] if nsc['Kinder'] is not None else []
    nrEreignisse = 5+nsc['Powerlevel']
    nsc['Unleben'] = []

    while nrEreignisse > 0:
        possibilities = ['Starre', 'Beginn eines Streites mit anderem Vampir', 'Beginn einer Liebschaft']
        if erzeugerLebt:
            possibilities.append('Verlust des Erzeugers')
            if not erzeugerLosgesagt:
                possibilities.append('Lossagung vom Erzeuger')
        if len(ungezeugteKinder) > 0:
            possibilities.append('Zeugen eines Kindes')
        if len(feinde) > 0:
            possibilities.append('Sieg in einem Streit')
            possibilities.append('Niederlage in einem Streit')
            possibilities.append('Ende eines Streites mit anderem Vampir')
        if len(liebschaften) > 0:
            possibilities.append('Ende einer Liebschaft')
        if len(aemter) > 0:
            possibilities.append('Niederlegen eines Amtes')
        else:
            possibilities.append('Umzug in neue Domäne')
            possibilities.append('Aufnehmen eines Amtes')
        ereignis = random.choice(possibilities)
        nrEreignisse -= 1
        if ereignis in ['Starre', 'Umzug in neue Domäne']:
            nsc['Unleben'].append([ereignis, random.choice(unleben[ereignis])])
        elif ereignis == 'Verlust des Erzeugers':
            erzeugerLebt = False
            nsc['Unleben'].append([ereignis, erzeugerLosgesagt])
        elif ereignis == 'Lossagung vom Erzeuger':
            erzeugerLosgesagt = True
            nsc['Unleben'].append([ereignis])
        elif ereignis == 'Aufnehmen eines Amtes':
            aemter.append(random.choice(unleben[ereignis]))
            nsc['Unleben'].append([ereignis, aemter[0]])
        elif ereignis == 'Niederlegen eines Amtes':
            amt = random.choice(aemter)
            aemter.remove(amt)
            nsc['Unleben'].append([ereignis, amt])
        elif ereignis == 'Beginn eines Streites mit anderem Vampir':
            feinde.append(MakeVampireName(nsc))
            nsc['Unleben'].append([ereignis, feinde[-1]])
        elif ereignis in ['Sieg in einem Streit', 'Niederlage in einem Streit']:
            feind = random.choice(feinde)
            nsc['Unleben'].append([ereignis, feind])
        elif ereignis == 'Ende eines Streites mit anderem Vampir':
            feind = random.choice(feinde)
            feinde.remove(feind)
            nsc['Unleben'].append([ereignis, feind])
        elif ereignis == 'Beginn einer Liebschaft':
            liebschaften.append(MakeVampireName(nsc))
            nsc['Unleben'].append([ereignis, liebschaften[-1]])
        elif ereignis == 'Ende einer Liebschaft':
            ex = random.choice(liebschaften)
            liebschaften.remove(ex)
            nsc['Unleben'].append([ereignis, ex])
        elif ereignis == 'Zeugen eines Kindes':
            kind = random.choice(ungezeugteKinder)
            ungezeugteKinder.remove(kind)
            nsc['Unleben'].append([ereignis, kind])

    while len(ungezeugteKinder) > 0:
        kind = random.choice(ungezeugteKinder)
        ungezeugteKinder.remove(kind)
        nsc['Unleben'].insert(random.randint(2, len(nsc['Unleben'])), ['Zeugen eines Kindes', kind])

    return nsc


def PrintEreignis(nsc, ereignis, language):
    if ereignis[0] == 'Starre':
        return f'{nsc["vorname"]} war {ereignis[1]} in Starre.'
    elif ereignis[0] == 'Umzug in neue Domäne':
        return f'Eine Domäne {ereignis[1]} wurde die neue Heimat von {nsc["vorname"]}.'
    elif ereignis[0] == 'Verlust des Erzeugers':
        reaktion = 'ein schwerer Schlag.' if not ereignis[1] else 'eine Erleichterung.'
        return f'Der Verlust von <a href={MakeLink(nsc,nsc["Erzeuger"],nsc["Powerlevel"]+1)}>{nsc["Erzeuger"]}</a> war für {nsc["vorname"]} {reaktion}'
    elif ereignis[0] == 'Lossagung vom Erzeuger':
        return f'Irgendwann verlässt jedes Küken das Nest, manchmal sogar endgültig. So hat sich {nsc["vorname"]} von {nsc["possesivpronomen"]}m Erzeuger gelöst.'
    elif ereignis[0] == 'Aufnehmen eines Amtes':
        return f'Der Aufstieg in {ereignis[1]} festigte {nsc["vorname"]}s Weg zur Macht'
    elif ereignis[0] == 'Niederlegen eines Amtes':
        return f'{nsc["vorname"]} musste {nsc["possesivpronomen"][:-1]} Amt abgeben'
    elif ereignis[0] == 'Beginn eines Streites mit anderem Vampir':
        return f'Es keimte eine Rivalität zwischen {nsc["vorname"]} und <a href={MakeLink(nsc,ereignis[1],nsc["Powerlevel"],True)}>{ereignis[1]}</a> auf.'
    elif ereignis[0] == 'Sieg in einem Streit':
        return f'Im Streit mit <a href={MakeLink(nsc,ereignis[1],nsc["Powerlevel"],True)}>{ereignis[1]}</a> erzielte {nsc["vorname"]} einen Sieg.'
    elif ereignis[0] == 'Niederlage in einem Streit':
        return f'Im Streit mit <a href={MakeLink(nsc,ereignis[1],nsc["Powerlevel"],True)}>{ereignis[1]}</a> erlitt {nsc["vorname"]} eine Niederlage.'
    elif ereignis[0] == 'Ende eines Streites mit anderem Vampir':
        return f'Die Rivalität zwischen {nsc["vorname"]} und <a href={MakeLink(nsc,ereignis[1],nsc["Powerlevel"],True)}>{ereignis[1]}</a> endet.'
    elif ereignis[0] == 'Beginn einer Liebschaft':
        return f'Obwohl Liebe selten ist, glaubte {nsc["vorname"]} in <a href={MakeLink(nsc,ereignis[1],nsc["Powerlevel"],True)}>{ereignis[1]}</a> eine echte Liebe gefunden zu haben.'
    elif ereignis[0] == 'Ende einer Liebschaft':
        return f'Der Durst übertrifft alles, so auch die Liebe von {nsc["vorname"]} für <a href={MakeLink(nsc,ereignis[1],nsc["Powerlevel"],True)}>{ereignis[1]}</a>.'
    elif ereignis[0] == 'Zeugen eines Kindes':
        return f'Um die Einsamkeit zu überbrücken, oder auch nur, um einen Untergebenen zu besitzen: {nsc["vorname"]} verwandelt <a href={MakeLink(nsc,ereignis[1],nsc["Powerlevel"]-1)}>{ereignis[1]}</a> in ein Kainskind.'
    else:
        return f'TODO {ereignis}'
# endregion


def MakeVampire(nsc):
    nsc = MakeRelationTree(nsc)
    NameToSeed(nsc['vorname']+' '+nsc['nachname'])
    nsc['Erzeuger'] = FindCreator(nsc)
    nsc['Kuss'] = [random.choice(kuss['legalität']), random.choice(kuss['beweggrund'])]
    nsc['Kinder'] = FindChildren(nsc)
    nsc['Gouhle'] = random.randint(GhulLookup[nsc['Powerlevel']][0], GhulLookup[nsc['Powerlevel']][0])
    nsc['Generation'] = GenerationLookup[nsc['Powerlevel']]
    nsc['TrinkPraktik'] = random.choice(einstellungVamp['Trinken']['Praktik'])
    nsc['TrinkMoral'] = random.choice(einstellungVamp['Trinken']['Einstellung'])
    nsc['Ansichten'] = {'Sterbliche':random.choice(einstellungVamp['Sterbliche'])}
    nsc = MakeUnleben(nsc)
    return nsc


def PrintVampire(nsc, language):
    result = Header('Unleben', '', language, 3)
    result += PrintLineageTree(nsc)
    result += f'''
    {nsc["vorname"]} wurde von {nsc["Erzeuger"]} {nsc["Kuss"][0]} geschaffen. Die Motivation zu diesem Kuss bestand aus {nsc["Kuss"][1]}.{Newline(language)}
    Als neues Kainskind der {nsc["Generation"]}. Generation begann das Unleben mit dem niemals endenden Durst.{Newline(language)}
    Seit dieser Nacht gab es einige Ereignisse im Dasein von {nsc["vorname"]}:{Newline(language)}
    <ul>
    '''
    for ereignis in nsc['Unleben']:
        result += f'<li>{PrintEreignis(nsc,ereignis,language)}</li>'
    result += '</ul>'
    result += f'Diese Erfahrungen prägen {nsc["vorname"]}. {StartCapital(nsc["pronomen"])} {nsc["TrinkPraktik"]} und {nsc["TrinkMoral"]}.{Newline(language)} Außerdem {InsertWordAtSpace(nsc["Ansichten"]["Sterbliche"],nsc["pronomen"])}.{Newline(language)} '
    return result + f' Dieser Abschnitt ist aktuell noch in Bearbeitung...{Newline(language)} {Newline(language)} Vorschläge gerne an mich!'
