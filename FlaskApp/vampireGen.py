from .Formatting import Bold, Newline, Header, ListLines
from .NSCGenUtils import NameToSeed, DrawWithWeights
from .config import baseURL

import random
import json

clans = {
    'Assamiten':1,
    'Brujah':1,
    'Gangrel':1,
    'Giovanni':1,
    'Jünger des Set':1,
    'Lasombra':1,
    'Malkavianer':1,
    'Nosferatu':1,
    'Ravnos':1,
    'Toreador':1,
    'Tremere':1,
    'Tzimisce':1,
    'Ventrue':1,
    'Caitiff':1
}

unleben = {
    'Vernichtung des Erzeugers': '',
    'Zeugen eines Kindes': '',
    'Starre': '',
    'Lossagung vom Erzeuger': '',
    'Umzug in neue Domäne': '',
    'Konflikt mit anderem Vampir': '',
    'Wechsel der Sekte': '',
    'selbst Blutsgebunden': '',
    'jemanden Blutsgebunden': '',
}

GhulLookup = {
    -1: [0,1],
    0: [0,1],
    1: [0,2],
    2: [1,2],
    3: [1,3],
    5: [1,4],
    6: [2,5],
    7: [3,6],
    8: [3,6],
    9: [3,7],
    10: [2,5],
    11: [2,4],
    12: [1,3],
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
    0: 3,
    1: 4,
    2: 2,
    3: 1
}


def MakeCreator(nsc):
    from .kinfolkGen import  GetRandomVorname, GetRandomNachname
    return GetRandomVorname()+' '+GetRandomNachname()


def MakeChildren(creator, maxDepth=1):
    from .kinfolkGen import  GetRandomVorname, GetRandomNachname
    if maxDepth>0:
        return [{(GetRandomVorname()+' '+GetRandomNachname()): MakeChildren(creator, maxDepth-1)} for _ in range(DrawWithWeights(kinderChances))]
    else:
        return []


def CheckDepth(tree):
    if len(list(tree.values())[0])>0:
        return 1 + max([CheckDepth(child) for child in list(tree.values())[0] if len(child)>0])
    else:
        return 0


def MakeRelationTree(nsc):
    maxDepth = 4
    if nsc['treeSeed'] == -1:
        nsc['Clan'] = DrawWithWeights(clans)
        nsc['treeSeed'] = f'{nsc["vorname"]} {nsc["nachname"]}#{nsc["Powerlevel"]}#{nsc["Clan"]}' 
        maxDepth = min(4,11-nsc['Powerlevel'])
    else:
        nsc['Clan'] = nsc['treeSeed'].split('#')[2]
        maxDepth = min(4,11-int(nsc['treeSeed'].split('#')[1]))
    NameToSeed(nsc['treeSeed'])
    Creator = MakeCreator(nsc)
    tree = {Creator: [{nsc['treeSeed'].split('#')[0]:MakeChildren(nsc['treeSeed'])}]+MakeChildren(Creator)}
    while CheckDepth(tree) < maxDepth:
        Creator = MakeCreator(list(tree.keys())[0])
        tree = {Creator: [tree]+MakeChildren(Creator, CheckDepth(tree))}
    nsc['RelationTree'] = tree
    return nsc

def FindCreator(nsc, tree=None):
    if tree is None:
        tree = nsc['RelationTree']
    if (nsc['vorname']+' '+nsc['nachname']) in map(lambda x: list(x.keys())[0],list(tree.values())[0]):
        return list(tree.keys())[0]
    elif len( list(tree.values())[0])>0:
        return [FindCreator(nsc,subTree) for subTree in list(tree.values())[0]][0]

def FindChildren(nsc, tree=None):
    if tree is None:
        tree = nsc['RelationTree']
    if (nsc['vorname']+' '+nsc['nachname']) in list(tree.keys())[0]:
        return list(map(lambda x: list(x.keys())[0],list(tree.values())[0]))
    elif len( list(tree.values())[0])>0:
        return [FindChildren(nsc,subTree) for subTree in list(tree.values())[0]][0]

def GetLevelInTree(nsc,tree=None,level=0):
    if tree is None:
        tree = nsc['RelationTree']
    if (nsc['vorname']+' '+nsc['nachname']) in list(tree.keys())[0]:
        return level
    elif (nsc['vorname']+' '+nsc['nachname'])  in map(lambda x: list(x.keys())[0],list(tree.values())[0]):
        return level+1
    elif len( list(tree.values())[0])>0:
        result =[x for x in [GetLevelInTree(nsc,subTree,level+1) for subTree in list(tree.values())[0]] if x is not None]
        if len(result)>0:
            return min(result)
    



def MakeVampire(nsc):
    nsc = MakeRelationTree(nsc)
    nsc['Erzeuger'] = FindCreator(nsc)
    nsc['Kuss'] = {}
    nsc['Kinder'] = FindChildren(nsc)
    nsc['Gouhle'] = random.randint(GhulLookup[nsc['Powerlevel']][0],GhulLookup[nsc['Powerlevel']][0])
    nsc['Generation'] = GenerationLookup[nsc['Powerlevel']]
    nsc['Unleben'] = []
    return nsc

def PrintLineageTree(nsc):
    result = '\n<div class="tree"><ul>'
    result += PrintTreeRecursion(nsc)
    result += '</ul></div>'
    return result

def MakeLink(nsc,Name,Powerlevel):
    return baseURL+f'/nsc/vampir/{Powerlevel}/html/{Name.replace(" ","_")}/?treeSeed={nsc["treeSeed"].replace(" ","_").replace("#","__")}'

def PrintTreeRecursion(nsc, tree=None):
    if tree is None:
        tree = nsc['RelationTree']
    result ='\n<li>\n'
    anchor = {'vorname':nsc['treeSeed'].split('#')[0].split(' ')[0],'nachname':nsc['treeSeed'].split('#')[0].split(' ')[1]}
    current = {'vorname':list(tree.keys())[0].split(' ')[0],'nachname':list(tree.keys())[0].split(' ')[1]}
    if nsc['vorname'] ==current['vorname'] and nsc['nachname'] ==current['nachname']:
        highlight = 'style="background-color:darkred;color:white;"'
    else:
        highlight = ''
    pwLvL =  int(nsc['treeSeed'].split('#')[1])+GetLevelInTree(anchor,nsc['RelationTree'])-GetLevelInTree(current,nsc['RelationTree'])
    result += f'<a {highlight} href={MakeLink(nsc,list(tree.keys())[0],pwLvL)}>{list(tree.keys())[0]}</a>'
    if len( list(tree.values())[0])>0:
        result += '<ul>\n' +'\n'.join([PrintTreeRecursion(nsc, subTree) for subTree in list(tree.values())[0] ])+'\n</ul>\n'
    return result +'\n</li>'

def PrintVampire(nsc, language):
    result = Header('Unleben', '', language, 3)
    result += PrintLineageTree(nsc) 
    return result + f' Hier entsteht eine Zusammenfassung über das Unleben von {nsc["vorname"]}:{Newline(language)} Erzeuger, Kinder, Guhle, Intrigen und mehr...{Newline(language)} {Newline(language)} Vorschläge gerne an mich!'


