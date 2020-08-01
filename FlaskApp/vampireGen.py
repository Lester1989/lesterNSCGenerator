from .Formatting import Bold, Newline, Header, ListLines
from .NSCGenUtils import NameToSeed, DrawWithWeights,StartCapital,InsertWordAtSpace
from .config import baseURL, basePath

import random
import json


with open(basePath+'jsons/einstellungVamp.json', 'r', encoding='utf-8') as infile:
    einstellungVamp = json.load(infile)
with open(basePath+'jsons/sekten.json', 'r', encoding='utf-8') as infile:
    sekten = json.load(infile)
with open(basePath+'jsons/clans.json', 'r', encoding='utf-8') as infile:
    clans = json.load(infile)
with open(basePath+'jsons/unleben.json', 'r', encoding='utf-8') as infile:
    unleben = json.load(infile)
with open(basePath+'jsons/kuss.json', 'r', encoding='utf-8') as infile:
    kuss = json.load(infile)
with open(basePath+'jsons/GhulLookup.json', 'r', encoding='utf-8') as infile:
    GhulLookup = json.load(infile)
with open(basePath+'jsons/GenerationLookup.json', 'r', encoding='utf-8') as infile:
    GenerationLookup = json.load(infile)
with open(basePath+'jsons/kinderChances.json', 'r', encoding='utf-8') as infile:
    kinderChances = {int(key):int(val) for (key,val) in json.load(infile).items()}

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
        maxDepth = min(4, 10-nsc['Powerlevel'])
    else:
        nsc['Clan'] = nsc['treeSeed'].split('#')[2]
        maxDepth = min(4, 11-int(nsc['treeSeed'].split('#')[1]))
    NameToSeed(nsc['treeSeed'])
    Creator = MakeVampireName(nsc)
    tree = {Creator: [{nsc['treeSeed'].split('#')[0]:MakeChildren(nsc['treeSeed'],max(0,int(nsc['treeSeed'].split('#')[1])+1))}]+MakeChildren(Creator)}
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
    result = '\n<div class="tree-container">\n<div class="tree"><ul>'
    result += PrintTreeRecursion(nsc)
    result += '</ul></div></div>\n'
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
    nrEreignisse = nsc['Powerlevel']+random.randint(4,8)
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
        return f'{nsc["vorname"]} war {ereignis[1]} in <b>Starre</b>.'
    elif ereignis[0] == 'Umzug in neue Domäne':
        return f'Eine Domäne {ereignis[1]} wurde die <b>neue Heimat</b> von {nsc["vorname"]}.'
    elif ereignis[0] == 'Verlust des Erzeugers':
        reaktion = 'ein schwerer Schlag.' if not ereignis[1] else 'eine Erleichterung.'
        if nsc['Erzeuger'] is None:
            return f'Der <b>Verlust</b> von {nsc["possesivpronomen"]}m Erzeuger war für {nsc["vorname"]} {reaktion}'
        return f'Der <b>Verlust</b> von <a href={MakeLink(nsc,nsc["Erzeuger"],nsc["Powerlevel"]+1)}>{nsc["Erzeuger"]}</a> war für {nsc["vorname"]} {reaktion}'
    elif ereignis[0] == 'Lossagung vom Erzeuger':
        return f'Irgendwann verlässt jedes Küken das Nest, manchmal sogar endgültig. So hat sich {nsc["vorname"]} <b>von {nsc["possesivpronomen"]}m Erzeuger gelöst</b>.'
    elif ereignis[0] == 'Aufnehmen eines Amtes':
        return f'Der <b>Aufstieg in {ereignis[1]}</b> festigte {nsc["vorname"]}s Weg zur Macht'
    elif ereignis[0] == 'Niederlegen eines Amtes':
        return f'{nsc["vorname"]} musste {nsc["possesivpronomen"][:-1]} <b>Amt abgeben</b>'
    elif ereignis[0] == 'Beginn eines Streites mit anderem Vampir':
        return f'Es keimte eine <b>Rivalität</b> zwischen {nsc["vorname"]} und <a href={MakeLink(nsc,ereignis[1],nsc["Powerlevel"],True)}>{ereignis[1]}</a> auf.'
    elif ereignis[0] == 'Sieg in einem Streit':
        return f'Im Streit mit <a href={MakeLink(nsc,ereignis[1],nsc["Powerlevel"],True)}>{ereignis[1]}</a> erzielte {nsc["vorname"]} einen <b>Sieg</b>.'
    elif ereignis[0] == 'Niederlage in einem Streit':
        return f'Im Streit mit <a href={MakeLink(nsc,ereignis[1],nsc["Powerlevel"],True)}>{ereignis[1]}</a> erlitt {nsc["vorname"]} eine <b>Niederlage</b>.'
    elif ereignis[0] == 'Ende eines Streites mit anderem Vampir':
        return f'Die <b>Rivalität</b> zwischen {nsc["vorname"]} und <a href={MakeLink(nsc,ereignis[1],nsc["Powerlevel"],True)}>{ereignis[1]}</a> <b>endet</b>.'
    elif ereignis[0] == 'Beginn einer Liebschaft':
        return f'Obwohl Liebe selten ist, glaubte {nsc["vorname"]} in <a href={MakeLink(nsc,ereignis[1],nsc["Powerlevel"],True)}>{ereignis[1]}</a> eine echte <b>Liebe gefunden</b> zu haben.'
    elif ereignis[0] == 'Ende einer Liebschaft':
        return f'Der Durst übertrifft alles, so kam es zum <b>Ende der Liebe</b> zwischen {nsc["vorname"]} und <a href={MakeLink(nsc,ereignis[1],nsc["Powerlevel"],True)}>{ereignis[1]}</a>.'
    elif ereignis[0] == 'Zeugen eines Kindes':
        return f'Um die Einsamkeit zu überbrücken, oder auch nur, um einen Untergebenen zu besitzen: {nsc["vorname"]} <b>verwandelt</b> <a href={MakeLink(nsc,ereignis[1],nsc["Powerlevel"]-1)}>{ereignis[1]}</a> in ein Kainskind.'
    else:
        return f'TODO {ereignis}'
# endregion


def MakeVampire(nsc):
    nsc = MakeRelationTree(nsc)
    NameToSeed(nsc['vorname']+' '+nsc['nachname'])
    nsc['Erzeuger'] = FindCreator(nsc)
    nsc['Generation'] = GenerationLookup[str(nsc['Powerlevel'])]
    nsc['Kuss'] = [random.choice(kuss['legalität']) if nsc['Generation']<=14 else 'ohne Erlaubnis', random.choice(kuss['beweggrund'])]
    nsc['Kinder'] = FindChildren(nsc)
    nsc['Guhle'] = random.randint(GhulLookup[str(nsc['Powerlevel'])][0], GhulLookup[str(nsc['Powerlevel'])][0])
    nsc['TrinkPraktik'] = random.choice(einstellungVamp['Trinken']['Praktik'])
    nsc['TrinkMoral'] = random.choice(einstellungVamp['Trinken']['Einstellung'])
    nsc['Ansichten'] = {'Sterbliche':random.choice(einstellungVamp['Sterbliche'])}
    nsc = MakeUnleben(nsc)
    return nsc


def PrintVampire(nsc, language):
    result = Header('Unleben', '', language, 3)
    result += PrintLineageTree(nsc)
    if nsc['Erzeuger'] is not None:
        Zeugung = f'{nsc["vorname"]} wurde von {nsc["Erzeuger"]} {nsc["Kuss"][0]} geschaffen. Die Motivation zu diesem Kuss bestand aus {nsc["Kuss"][1]}.{Newline(language)}'
    else:
        Zeugung = f'Über den Erzeuger von {nsc["vorname"]} ist nichts bekannt, jedoch Erfahren Vertraute {nsc["vorname"]} der Kuss aus {nsc["Kuss"][1]} geschenkt wurde.{Newline(language)}'
    result += f'''    
    {Zeugung}
    Als neues Kainskind der {nsc["Generation"]}. Generation begann das Unleben mit dem niemals endenden Durst.{Newline(language)}
    Seit dieser Nacht gab es einige Ereignisse im Dasein von {nsc["vorname"]}:{Newline(language)}
    <ul>
    '''
    for ereignis in nsc['Unleben']:
        result += f'<li>{PrintEreignis(nsc,ereignis,language)}</li>'
    result += '</ul>'
    result += f'''
    Diese Erfahrungen prägen {nsc["vorname"]}. {StartCapital(nsc["pronomen"])} {nsc["TrinkPraktik"]} und {nsc["TrinkMoral"]}.{Newline(language)}
    Außerdem {InsertWordAtSpace(nsc["Ansichten"]["Sterbliche"],nsc["pronomen"])}.{Newline(language)}
    '''
    return result + f'{Newline(language)}Dieser Abschnitt ist aktuell noch in Bearbeitung...{Newline(language)} {Newline(language)} Vorschläge gerne an mich!<div class="clearfix"></div>\n '
