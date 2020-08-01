# -*- coding: utf-8 -*-

import csv
import hashlib
import random
import requests
import json
from bs4 import BeautifulSoup

from .gaben import LookUpTexteByName, GetGaben, GetFomorGaben
from .bsdFomorGen import MakeBSD, MakeFomor
from .PackNameGen import GenerateRandomName
from .SpielHinweise import MakeSpielAnweisung
from .LookGen import MakeBeschreibung, PrintBeschreibung
from .Formatting import Bold, Newline, Header, ListLines, Table, StartCapital
from .config import baseURL, basePath
from .NSCGenUtils import NameToSeed, DrawWithWeightsUnique, DrawWithWeights, DrawKey, DrawKeyUnique
from .vampireGen import PrintVampire, MakeVampire
from .ImageGen import TextWithImage, GetFace
# =================================================================
# INIT TABLES
# =================================================================

# region INIT TABLES


# with open('baneType.json', 'w', encoding='utf-8') as outfile:
#     json.dump(baneType,outfile,indent=2)
# with open('hintergruende.json', 'r', encoding='utf-8') as infile:
#     hintergründe = json.load(infile)

with open(basePath+'/jsons/hintergruende.json', 'r', encoding='utf-8') as infile:
    hintergründe = json.load(infile)
with open(basePath+'/jsons/namedMotivation.json', 'r', encoding='utf-8') as infile:
    namedMotivation = json.load(infile)
with open(basePath+'/jsons/motivation.json', 'r', encoding='utf-8') as infile:
    motivation = json.load(infile)
with open(basePath+'/jsons/plaene.json', 'r', encoding='utf-8') as infile:
    pläne = json.load(infile)
with open(basePath+'/jsons/richtlinien.json', 'r', encoding='utf-8') as infile:
    richtlinien = json.load(infile)
with open(basePath+'/jsons/einstellung.json', 'r', encoding='utf-8') as infile:
    einstellung = json.load(infile)
with open(basePath+'/jsons/wissen.json', 'r', encoding='utf-8') as infile:
    wissen = json.load(infile)
with open(basePath+'/jsons/ausbildung.json', 'r', encoding='utf-8') as infile:
    ausbildung = json.load(infile)
with open(basePath+'/jsons/factor.json', 'r', encoding='utf-8') as infile:
    factor = json.load(infile)
with open(basePath+'/jsons/skills.json', 'r', encoding='utf-8') as infile:
    skills = json.load(infile)
with open(basePath+'/jsons/poolMaxes.json', 'r', encoding='utf-8') as infile:
    poolMaxes = json.load(infile)
with open(basePath+'/jsons/staemme.json', 'r', encoding='utf-8') as infile:
    stämme = json.load(infile)
with open(basePath+'/jsons/vorzeichen.json', 'r', encoding='utf-8') as infile:
    vorzeichen = json.load(infile)
with open(basePath+'/jsons/bruten.json', 'r', encoding='utf-8') as infile:
    bruten = json.load(infile)
with open(basePath+'/jsons/Raenge.json', 'r', encoding='utf-8') as infile:
    Ränge = json.load(infile)
with open(basePath+'/jsons/beziehungen.json', 'r', encoding='utf-8') as infile:
    beziehungen = json.load(infile)
with open(basePath+'/jsons/berufe.json', 'r', encoding='utf-8') as infile:
    berufe = json.load(infile)

names = {}
surnames = []
with open(basePath+'/FlaskApp/Vornamen_2018_Koeln.csv', 'r', encoding='utf8') as file:
    rawnames = csv.DictReader(file, delimiter=';')
    for nr, row in enumerate(rawnames):
        # print(dict(row))
        names[nr] = dict(row)
    print(f'Vornamen: {len(names)}')

with open(basePath+'/FlaskApp/us.txt', 'r') as file:
    for line in file:
        surnames.append(line[:-1])
    print(f'Nachnamen: {len(surnames)}')
# endregion

# =================================================================
# RANDOM SELECTION METHODS
# =================================================================


def GetRandomVorname(initSeed=0, sex=''):
    if initSeed != 0:
        random.seed(initSeed)
    nameData = names[random.randint(0, len(names)-1)]
    if sex != '':
        while nameData['geschlecht'] != sex:
            nameData = names[random.randint(0, len(names)-1)]
    return nameData['vorname'].replace('_', ' ')


def GetRandomNachname(initSeed=0):
    if initSeed != 0:
        random.seed(initSeed)
    return surnames[random.randint(0, len(surnames)-1)]


# =================================================================
# CREATION METHODS
# =================================================================


def MakeValue(nsc):
    if 'ausbildung' not in nsc:
        print('Ausbildungen sollten erstellt werden, bevor Würfelpools erzeugt werden.')
        return nsc
    NameToSeed(nsc['vorname']+' '+nsc['nachname'])
    baseVal = (3 if nsc['art'] == 'Kinfolk' or nsc['art'] == 'Human' else 5) + int(nsc['Powerlevel'] / 2)
    charPools = {'Nahkampf': baseVal, 'Fernkampf': baseVal, 'Widerstand': baseVal, 'Wille': baseVal, 'Lügen': baseVal,
                 'Wahrnehmen': baseVal, 'Verstecken': baseVal, 'Handwerk': baseVal, 'Medizin': baseVal}
    badSkill = min(0, nsc['Powerlevel'] - 2)
    for _ in range(-badSkill):
        charPools[DrawKey(charPools)] -= 1
    goodSkill = min(9, 2 + nsc['Powerlevel'])
    for _ in range(goodSkill):
        charPools[DrawKey(charPools)] += 1
    for SkillArt, SkillGüte in nsc['ausbildung']:
        for skill in skills[SkillArt]:
            charPools[skill] += factor[SkillGüte]
    for pool in charPools:
        charPools[pool] = min(charPools[pool], poolMaxes[pool] + nsc['Powerlevel'])
        charPools[pool] = max(charPools[pool], 1)
    nsc['dicePools'] = charPools
    return nsc


def MakeDescriptions(nsc):
    NameToSeed(nsc['vorname']+' '+nsc['nachname'])
    nsc['alter'] = DrawWithWeights(hintergründe["Alter"])
    nsc['zeit'] = DrawWithWeights(hintergründe["Zeit"])
    nsc['familie'] = DrawWithWeights(hintergründe["Familie"])
    nsc['motivation'] = DrawWithWeights(motivation)
    nsc['pläne'] = DrawWithWeights(pläne)
    mottos = namedMotivation['Alle']
    if nsc['art'] in vorzeichen:
        mottos.update(namedMotivation['Garou'])
    if nsc['art'] == 'vampir':
        mottos.update(namedMotivation['Vampire'])
    nsc['motto'] = random.choice(list(mottos.items()))
    nsc['wyrm'] = DrawWithWeights(einstellung['Wyrm'])
    nsc['rangordnung'] = DrawWithWeights(einstellung['Rangordnung'])
    nsc['scRudel'] = DrawWithWeights(einstellung['Rudel'])
    nsc['plot'] = DrawWithWeights(wissen)
    return nsc


def MakeBreed(nsc, brut=''):
    NameToSeed(nsc['vorname']+' '+nsc['nachname'])
    if nsc['art'] in vorzeichen:
        nsc['brut'] = DrawWithWeights(bruten) if brut == '' else brut
        #print(f'{nsc["vorname"]} {nsc["nachname"]}, {nsc["art"]} {nsc["brut"]} {nsc["stamm"]}')
        nsc['gaben'] = {}
        for _ in range(3+nsc['Powerlevel']):
            if nsc['Powerlevel'] < -1:
                nsc['rang'] = 'Cliath'
            elif nsc['Powerlevel'] > 11:
                nsc['rang'] = 'Legende'
            else:
                nsc['rang'] = Ränge[nsc['Powerlevel']]
            gabe = LookUpTexteByName(DrawKeyUnique(GetGaben(nsc['brut'], nsc['art'], nsc['stamm'], nsc['rang']), nsc['gaben']))
            nsc['gaben'][gabe['name']] = gabe
    if nsc['art'] == 'Vampir':
        nsc['Disziplinen'] = {}
        # TODO add Disziplinen
    if nsc['art'] == 'Fomor':
        nsc['gaben'] = {}
        if random.random() > .2:
            nsc['gaben']['Immunität gegen das Delirium'] = LookUpTexteByName('Immunität gegen das Delirium')
        if random.random() > .66:
            nsc['gaben']['Berserker'] = LookUpTexteByName('Berserker')
        for _ in range(max(1, min(nsc['Powerlevel'], 4))):
            gabe = LookUpTexteByName(DrawKeyUnique(GetFomorGaben(), nsc['gaben']))
            nsc['gaben'][gabe['name']] = gabe
            pass
    return nsc


def MakeExpertise(nsc):
    NameToSeed(nsc['vorname']+' '+nsc['nachname'])
    nrAusbildung = int(DrawWithWeights(ausbildung['Anzahl'])) + (0 if nsc['art'] == "Kinfolk" else 1)
    nscAusbildungen = []
    nscGüte = []
    for _ in range(nrAusbildung):
        nscAusbildungen.append(DrawWithWeightsUnique(ausbildung['Art'], nscAusbildungen))
        nscGüte.append(DrawWithWeightsUnique(ausbildung['Güte'], [] if nsc['art'] == "Kinfolk" else ['fehlerhafte']))
    nsc['ausbildung'] = list(zip(nscAusbildungen, nscGüte))
    return nsc


def MakePlayAdvise(nsc):
    NameToSeed(nsc['vorname']+' '+nsc['nachname'])
    nsc.update(MakeSpielAnweisung())
    return nsc


def MakeBase(seed=-1, Art='Kinfolk', Stamm='', Powerlevel=0, occupation=''):
    nameData = {}
    #print(f'Seed: {seed}')
    if seed == -1:
        nameData = names[random.randint(0, len(names)-1)]
        surname = surnames[random.randint(0, len(surnames)-1)]
    else:
        vorname = seed[:seed.rfind('_')]
        surname = seed[seed.rfind('_') + 1:]
        for ndNr in names:
            if vorname == names[ndNr]['vorname']:
                nameData = names[ndNr]
                break
    if 'vorname' not in nameData:
        print(f'VORNAME not recognised returning random ({seed})')
        return MakeBase(-1, Art, Stamm, Powerlevel, occupation)

    NameToSeed(nameData['vorname'].replace('_', ' ')+' '+surname)

    nsc = {
        'vorname': nameData['vorname'].replace('_', ' '),
        'nachname': surname,
        'pronomen': 'er' if nameData['geschlecht'] == 'm' else 'sie',
        'possesivpronomen': 'seine' if nameData['geschlecht'] == 'm' else 'ihre',
        'Powerlevel': Powerlevel,
        'occupation': occupation,
        'job': random.sample(berufe, 1)[0]
    }

    nsc['art'] = Art
    if Art in ['Human', 'vampir']:
        return nsc
    if Art == 'Fomor':
        nsc.update(MakeFomor(seed))
        return nsc
    #if Art == 'Kinfolk':
    if Art in vorzeichen:
        nsc['art'] = 'Garou'
        nsc['vorzeichen'] = Art
    if Art == 'Garou':
        nsc['vorzeichen'] = DrawWithWeights(vorzeichen)
    if Stamm == '':
        nsc['stamm'] = DrawWithWeights(stämme)
    elif Stamm == 'Tänzer der schwarzen Spirale':
        nsc['stamm'] = 'Tänzer der schwarzen Spirale'
        nsc.update(MakeBSD(seed))
    else:
        nsc['stamm'] = Stamm
    return nsc


def PrintNSC(nsc, packname, language='Plain', shortPrint=False):
    result = Header(nsc['vorname'], nsc['nachname'], language)

    # Rudel
    if packname is not None and 'packname' in packname:
        result += PrintPack(packname['packname'], nsc['vorname'])
        packString = f'?packname={packname["packname"]}'
    else:
        packString = ''

    # Rang und Rolle
    if 'rang' in nsc:
        result += f'{nsc["rang"]} '

    if 'Clan' in nsc:
        result += f'{nsc["Clan"]} {nsc["Generation"]}. Generation'
    else:
        result += f'{nsc["art"].upper()}'

    if 'stamm' in nsc:
        result += f' {nsc["stamm"]}'
    if 'brut' in nsc and len(nsc['brut']) > 0:
        result += f' ({nsc["brut"]})'
    else:
        result += Newline(language)
    if 'stamm' in nsc and nsc['stamm'] == 'Tänzer der schwarzen Spirale':
        result += f'{nsc["Abstammung"]}'

    # Kurzform Wesen
    result += f' ({nsc["motto"][0]}) '+Newline(language)

    # Rollenspiel
    result += Header('Rollenspiel', 'Vorschläge', language, 3)
    result += f'Ein Persönlichkeitsmerkmal ist {Bold(nsc["grundstimmung"],language)}'+Newline(language)
    result += 'Körperhaltung: '+Bold(nsc["haltung"][0], language)+((f' ({nsc["haltung"][1]})'+Newline(language)) if not shortPrint else Newline(language))
    result += 'Gestik: '+Bold(nsc["gestik"][0], language)+((f' ({nsc["gestik"][1]})'+Newline(language)) if not shortPrint else Newline(language))
    result += 'Mimik: '+Bold(nsc["mimik"][0], language)+((f' ({nsc["mimik"][1]})'+Newline(language)) if not shortPrint else Newline(language))

    # Aussehen
    result += Header('Aussehen', '', language, 3)
    result += TextWithImage(PrintBeschreibung(nsc, Newline(language)), GetFace(nsc))

    # Beschreibung
    result += '<div class="clearfix"></div>'
    result += Header('Beschreibung:', '', language, 3)
    result += f'{nsc["vorname"]} ({nsc["alter"]}), ist {nsc["zeit"]} und aktuell {Bold(nsc["familie"],language)}. {StartCapital(nsc["pronomen"])} arbeitet(e) als {nsc["job"]}. {Newline(language)}'
    result += f'{nsc["possesivpronomen"][0].upper()+nsc["possesivpronomen"][1:]} eigentliche Motivation ist {nsc["motivation"]} und der zur Zeit verfolgte Plan hat {nsc["pläne"]} als Ziel.{Newline(language)}'
    result += f'{nsc["vorname"]} {nsc["motto"][1]}'
    if nsc['art'] == 'Human':
        result += Newline(language) + f'Gegenüber dem SC Rudel ist {nsc["pronomen"]} {Bold(nsc["scRudel"],language)}.'
    elif nsc['art'] == 'vampir':
        pass
    else:
        if 'stamm' in nsc and nsc['stamm'] == 'Tänzer der schwarzen Spirale':
            result += f' Die Rangordnung ist {nsc["rangordnung"]} für {nsc["pronomen"] if nsc["pronomen"]=="sie" else "ihn"}. {Newline(language)}'
            pass
        else:
            result += f' Über den Wyrm denkt {nsc["pronomen"]}: {nsc["wyrm"]}.{Newline(language)}'
            result += f'Die Rangordnung ist für {nsc["pronomen"] if nsc["pronomen"]=="sie" else "ihn"} {nsc["rangordnung"]} und gegenüber dem SC Rudel ist {nsc["pronomen"]} {Bold(nsc["scRudel"],language)}. '

    result += f'Über den {Bold("Plot",language)} hat {nsc["vorname"]} {nsc["plot"]}. {Newline(language)}'

    if 'stamm' in nsc and nsc['stamm'] == 'Tänzer der schwarzen Spirale':
        result += f'{nsc["vorname"]} leidet an {nsc["Geistesstörung"]["Grad"]}{nsc["Geistesstörung"]["Art"]}{Newline(language)}'
        result += f'{Bold("Äußere Merkmale:",language)}{Newline(language)}'
        for merkmal in nsc['Mutationen']:
            if nsc['Mutationen'][merkmal][0] == 'Tierisch':
                result += f' {merkmal} wie von {nsc["Mutationen"][merkmal][1]}{Newline(language)}'
            elif nsc['Mutationen'][merkmal][0] == 'Verderbnis':
                result += f' {merkmal} {"sehen" if merkmal =="Die Augen" else "sieht"} {nsc["Mutationen"][merkmal][1]} aus{Newline(language)}'
            elif nsc['Mutationen'][merkmal][0] == 'Verzerrung':
                result += f' {merkmal} {"wirken" if merkmal =="Die Augen" else "wirkt"} {nsc["Mutationen"][merkmal][1]}{Newline(language)}'
        if (len(nsc['Entstellungen'])) > 0:
            result += f'{Bold(nsc["vorname"],language)} {nsc["Entstellungen"][0]}'
            for entstellung in nsc['Entstellungen'][1:]:
                result += f' und {entstellung}'
        else:
            if len(nsc['Mutationen']) == 0:
                result += 'keine erkennbare Entstellung'
    if nsc['art'] == 'Fomor':
        result += f'Die prägende Sünde von {nsc["vorname"]} ist {Bold(nsc["Sünde"],language)}. {Newline(language)} '
        result += f'{Bold("Äußere Merkmale:",language)}{Newline(language)}'
        if len(nsc['Mutationen']) > 0:
            for merkmal in nsc['Mutationen']:
                if nsc['Mutationen'][merkmal][0] == 'Tierisch':
                    result += f' {merkmal} wie von {nsc["Mutationen"][merkmal][1]}{Newline(language)}'
                elif nsc['Mutationen'][merkmal][0] == 'Verderbnis':
                    result += f' {merkmal} {"sehen" if merkmal =="Die Augen" else "sieht"} {nsc["Mutationen"][merkmal][1]} aus{Newline(language)}'
                elif nsc['Mutationen'][merkmal][0] == 'Verzerrung':
                    result += f' {merkmal} {"wirken" if merkmal =="Die Augen" else "wirkt"} {nsc["Mutationen"][merkmal][1]}{Newline(language)}'
        else:
            result += 'keine körperlichen Entstellungen'

    # Arbeit oder Amt
    if len(nsc['occupation']) > 0:
        if nsc['art'] != 'Kinfolk':
            result += f'In der Septe hat {nsc["vorname"]} folgende Ämter: {Bold(nsc["occupation"],language)}'+Newline(language)
        else:
            result += f'In der Siedlung arbeitet {nsc["vorname"]} als {Bold(nsc["occupation"],language)}'+Newline(language)

    # ausbildung
    if nsc['art'] != 'vampir':
        if not shortPrint:
            result += f'Um einen Platz in der Gesellschaft einzunehmen gab es {len(nsc["ausbildung"])} Ausbildung{"en" if len(nsc["ausbildung"])>1 else ""} für {nsc["pronomen"] if nsc["pronomen"]=="sie" else "ihn"}:{Newline(language)}'
            result += ListLines([f'{güte} Ausbildung {Bold(ausb,language)}' for ausb, güte in nsc["ausbildung"]], language)
    else:
        result += PrintVampire(nsc, language)

    # Würfelpools
    result += Header('Würfelpools', '', language, 3)
    result += Table(6, [f'{cell}' for pool in nsc['dicePools'] for cell in [pool, nsc["dicePools"][pool]]], language)

    # Gaben
    if nsc['art'] != 'Kinfolk' and 'gaben' in nsc:
        result += Header('Gaben', 'Vorschläge', language, 3)
        if not shortPrint:
            result += ListLines([Bold(gabe, language)+':'+nsc['gaben'][gabe]['fluffText']+Newline(language) +
                                 Bold('System: ', language)+nsc['gaben'][gabe]['systemText'] for gabe in nsc['gaben']], language)
        else:
            result += ListLines([Bold(gabe, language) for gabe in nsc['gaben']], language)

    if not shortPrint:
        baseLink = Newline("HTML") + f'<a class="no-print" href="{baseURL}/nsc/'
        art = nsc["art"].lower() if nsc["art"] in ["Kinfolk", "Human", "Fomor", "vampir"] else "garou"
        if 'stamm' in nsc and nsc['stamm'] == 'Tänzer der schwarzen Spirale':
            art = 'bsd'
        seed = (nsc["vorname"]+" "+nsc["nachname"]).replace(" ", "_")

        result += baseLink + f'{art}/{nsc["Powerlevel"]}/{language.lower()}/{seed}{packString}">Dieser NCS ({nsc["vorname"]+" "+nsc["nachname"]})</a>'
        if nsc["Powerlevel"] < 12:
            result += baseLink + f'{art}/{nsc["Powerlevel"]+1}/{language.lower()}/{seed}{packString}">Stärker</a>'
        if nsc["Powerlevel"] > -1:
            result += baseLink + f'{art}/{nsc["Powerlevel"]-1}/{language.lower()}/{seed}{packString}">Schwächer</a>{Newline("HTML")}'
        # if language == 'HTML':
        #     result += baseLink + f'{art}/{nsc["Powerlevel"]}/latex/{seed}{packString}">Dieser NCS ({seed}) als LaTeX Subsection</a>'
        # else:
        #     result += baseLink + f'{art}/{nsc["Powerlevel"]}/html/{seed}{packString}">Dieser NCS ({seed}) als HTML Subsection</a>'
        result += baseLink + f'{art}/{nsc["Powerlevel"]}/{language.lower()}">Zufall neu</a>'
    return result


def BuildNSC(seed=-1, Art='Kinfolk', Stamm='', Powerlevel=0, language='HTML', packname='', occupation='', brut='', shortPrint=True):
    nsc = MakeBase(seed, Art, Stamm, Powerlevel, occupation)

    packString = ''
    treeSeed = ''
    nsc['treeSeed'] = -1
    if packname != '' and 'packname' in packname:
        packString = f'?packname={packname["packname"]}'
    elif packname != '' and 'treeSeed' in packname:
        treeSeed = f'?treeSeed={packname["treeSeed"]}'
        nsc['treeSeed'] = packname["treeSeed"].replace("__", "#").replace("_", " ")

    nsc = MakeBeschreibung(nsc)
    nsc = MakeBreed(nsc, brut)
    nsc = MakePlayAdvise(nsc)
    nsc = MakeExpertise(nsc)
    nsc = MakeDescriptions(nsc)
    nsc = MakeValue(nsc)
    if nsc['art'] == 'vampir':
        nsc = MakeVampire(nsc)
    art = nsc["art"].lower() if nsc["art"] in ["Kinfolk", "Human", 'vampir'] else "garou"
    seed = (nsc["vorname"]+" "+nsc["nachname"]).replace(" ", "_")
    nsc['link'] = f'<a href="{baseURL}/nsc/{art}/{nsc["Powerlevel"]}/{language.lower()}/{seed}{packString}{treeSeed}">{nsc["vorname"]+" "+nsc["nachname"]}</a>'

    return nsc


def BuildBSD(seed=-1, Powerlevel=0, language='Plain', packname=None):
    bsd = MakeBase(seed, 'Garou', 'Tänzer der schwarzen Spirale', Powerlevel)
    bsd = MakeBeschreibung(bsd)
    bsd = MakeBreed(bsd)
    bsd = MakeExpertise(bsd)
    bsd = MakePlayAdvise(bsd)
    bsd = MakeExpertise(bsd)
    bsd = MakeDescriptions(bsd)
    bsd = MakeValue(bsd)
    tänzerMotivationen = {'Wahnsinn': 5}
    tänzerMotivationen.update(motivation)
    bsd['motivation'] = DrawWithWeights(tänzerMotivationen)
    seed = (bsd["vorname"]+" "+bsd["nachname"]).replace(" ", "_")
    if packname is not None and 'packname' in packname:
        packString = f'?packname={packname["packname"]}'
    else:
        packString = ''
    bsd['link'] = f'<a href="{baseURL}/nsc/bsd/{bsd["Powerlevel"]}/{language.lower()}/{seed}{packString}">{bsd["vorname"]+" "+bsd["nachname"]}</a>'
    return bsd


def BuildFomor(seed, Powerlevel, language):
    fomor = MakeBase(seed, Art='Fomor', Powerlevel=Powerlevel)
    fomor = MakeBeschreibung(fomor)
    fomor = MakeBreed(fomor)
    fomor = MakeExpertise(fomor)
    fomor = MakePlayAdvise(fomor)
    fomor = MakeExpertise(fomor)
    fomor = MakeDescriptions(fomor)
    fomor = MakeValue(fomor)
    tänzerMotivationen = {'Wahnsinn': 5}
    tänzerMotivationen.update(motivation)
    fomor['motivation'] = DrawWithWeights(tänzerMotivationen)
    return fomor


def CreateRandom(seed=-1, Art='Kinfolk', Stamm='', Powerlevel=0, language='Plain', packname=None, occupation='', brut='', shortPrint=True):
    return PrintNSC(BuildNSC(seed, Art, Stamm, Powerlevel, language, packname, occupation, brut, shortPrint), packname, language, shortPrint)


def CreateBSD(seed=-1, Powerlevel=0, language='Plain', packname=None):
    return PrintNSC(BuildBSD(seed, Powerlevel, language, packname), language=language, packname=packname)


def CreateFomor(seed=-1, Powerlevel=0, language='Plain'):
    return PrintNSC(BuildFomor(seed, Powerlevel, language), language=language, packname=None)


def BuildGarouPack(seed=-1, limitTribes=[], limitBreeds=[], minMembers=3, maxMembers=6):
    if seed == -1:
        packname = GenerateRandomName()
    else:
        packname = seed
    seed = int(hashlib.md5(f'{packname}'.encode('utf8')).hexdigest(), 16)
    random.seed(seed)
    packMember = random.randint(minMembers, maxMembers)
    pack = []
    for _ in range(packMember):
        nsc = BuildNSC(seed=-1,
                       Art='Garou',
                       packname=packname
                       )
        # or nsc['art'] !='Galliard':
        while (len(limitTribes) > 0 and nsc['stamm'] in limitTribes) or (len(limitBreeds) > 0 and nsc['brut'] in limitBreeds):
            nsc = BuildNSC(seed=-1,
                           Art='Garou',
                           packname=packname
                           )
        pack.append(nsc)
    return {'packname': packname, 'pack': pack, 'link': f'<a href="{baseURL}/nsc/garoupack/?packname={packname}">Rudel: {packname.replace("_"," ")}</a>'}


def BuildBSDPack(seed=-1, limitBreeds=[], minMembers=3, maxMembers=6):
    if seed == -1:
        packname = GenerateRandomName()
    else:
        packname = seed
    seed = int(hashlib.md5(f'{packname}'.encode('utf8')).hexdigest(), 16)
    random.seed(seed)
    packMember = random.randint(minMembers, maxMembers)
    pack = []
    for _ in range(packMember):
        nsc = BuildBSD(seed=-1,
                       packname=packname
                       )
        # or nsc['art'] !='Galliard':
        while (len(limitBreeds) > 0 and nsc['brut'] in limitBreeds):
            nsc = BuildBSD(seed=-1,
                           packname=packname
                           )
        pack.append(nsc)
    return {'packname': packname, 'pack': pack, 'link': f'<a href="{baseURL}/nsc/bsdpack/?packname={packname}">Rudel: {packname.replace("_"," ")}</a>'}


def PrintPack(seed=-1, memberName='', language='HTML', limitTribes=[], limitBreeds=[], minMembers=3, maxMembers=6):
    pack = BuildGarouPack(seed, limitTribes, limitBreeds,
                          minMembers, maxMembers)

    result = Header(pack['packname'], '', language, 2) if memberName == '' else Header(pack['link'], '', language, 3)
    packMemberNames = []
    for nsc in pack['pack']:
        packMemberNames.append(f'{nsc["vorname"]} {nsc["nachname"]}')
        if language == 'HTML':
            result += f'{Newline(language)}<a href="{baseURL}/nsc/garou/0/html/{nsc["vorname"]+"_"+nsc["nachname"]}?packname={pack["packname"]}">{nsc["vorname"]} {nsc["nachname"]} ({nsc["art"]} von den {nsc["stamm"]})</a>'
        else:
            result += f'{nsc["vorname"]} {nsc["nachname"]} ({nsc["art"]} von den {nsc["stamm"]})'+Newline(language)
    result += BuildRelationships(packMemberNames, memberName, language)
    return result


def PrintBSDPack(seed=-1, limitBreeds=[], memberName='', minMembers=3, maxMembers=6, language='HTML'):
    pack = BuildBSDPack(seed, limitBreeds, minMembers, maxMembers)
    result = Header(pack['packname'], '', language, 2) if memberName == '' else Header(pack['link'], '', language, 3)
    packMemberNames = []
    for nsc in pack['pack']:
        packMemberNames.append(f'{nsc["vorname"]} {nsc["nachname"]}')
        if language == 'HTML':
            result += f'{Newline(language)}<a href="{baseURL}/nsc/bsd/0/html/{nsc["vorname"]+"_"+nsc["nachname"]}?packname={pack["packname"]}">{nsc["vorname"]} {nsc["nachname"]} ({nsc["art"]} von den {nsc["stamm"]})</a>'
        else:
            result += f'{nsc["vorname"]} {nsc["nachname"]} ({nsc["art"]} von den {nsc["stamm"]})'+Newline(language)
    result += BuildRelationships(packMemberNames, memberName, language)
    return result


def BuildRelationships(pack, activeName='', language='HTML'):
    result = Header('Beziehungen' 'innerhalb des Rudels:', language, 3)
    vornamen = {name.split(' ')[0] for name in pack}
    if len(vornamen) == len(pack):
        pack = vornamen
    for member in pack:
        relations = random.sample(beziehungen, 2)
        others = random.sample([m for m in pack if m != member], 2)
        # print(relations)
        # print(others)
        relString = [(relation + ' ' + other) if 'XX' not in relation else (relation.replace('XX', other)) for relation, other in zip(relations, others)]
        result += f'{Newline(language)}{member} {relString[0]} und {relString[1]}.'
    if activeName == '':
        return result
    else:
        return result.replace(f'{activeName} ', f'{Bold(activeName,language)} ')
