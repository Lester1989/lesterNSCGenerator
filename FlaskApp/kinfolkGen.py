# -*- coding: utf-8 -*-

import csv
import hashlib
import random
from .gaben import *
from .bsdFomorGen import *
from .PackNameGen import *
from .SpielHinweise import *
from .LookGen import *
from .Formatting import Bold,Newline,Header,ListLines,Table,StartCapital
import requests
import json
from bs4 import BeautifulSoup

baseURL='v22018117165076045.happysrv.de'
# =================================================================
# INIT TABLES
# =================================================================

hintergründe = {'Zeit': {'neu in der Gemeinschaft': 1, 'voll eingearbeitet': 3, 'seit langer Zeit dabei': 4, 'von Geburt an indoktriniert': 5}, 'Familie': {'Ledig': 3, 'Verheiratet (mit Kinfolk)': 1, 'Verheiratet (mit Garou)': 2, 'Verwitwet': 1, 'Geschieden': 1}, 'Alter': {'gerade Volljährig': 2, 'zwischen 20 und 30': 6, 'anfang 30': 4, 'mitte 30': 3, 'anfang 40': 2, 'mitte 40': 2, 'zwischen 40 und 50': 2, 'ende 50': 1, 'über 60': 1, }}
motivation = {'Persönlicher Machtgewinn': 1, 'Anerkennung': 3, 'Neugierde': 1, 'Familiengründung': 2, 'Beschützen': 3, 'Selbstlose Opferbereitschaft': 2, 'Angst vor Bösem/Weltuntergang': 1, 'Pflichtgefühl': 6, 'Rache': 1}
pläne = {'Rang aufstieg': 3, 'Vermögenszuwachs': 1, 'Partner finden und Kinder machen': 2, 'Nachforschungen': 1, 'Training (Fähigkeitssteigerung)': 2, 'auf Befehle warten': 4, 'Flucht': .5, 'Rache': 1}
richtlinien = {'Ich vor allem': 2, 'Familie vor allem': 4, 'Ehre vor allem': 1, 'Bedacht statt Übermut': 3, 'Für das höhere Wohl': 2, 'Gerechtigkeit für alle': 1, }
einstellung = {'Wyrm': {'Sofort vernichten': 6, 'Verstehen um zu vernichten': 5, 'Verstehen um zu verhindern': 2, 'Heilen/bekehren': 1}, 'Rangordnung': {'Unantastbar': 2, 'von Gaia gewollt': 2, 'nötig für das Überleben': 3, 'wie sie ist': 3, 'ein Relikt und Hindernis aus alter Zeit': 2, 'die Wurzel des Untergangs': .5}, 'Rudel': {'Liebevoll': .5, 'Freundlich': 1, 'Offen': 3, 'Neutral': 3, 'Verschlossen': 2, 'Misstrauisch': 1, 'Feindselig': .5, 'Hass': .25}}
wissen = {'volles Wissen und Verstehen': .5, 'Wissen und Ahnung über Bedeutung': 1, 'lückenhaftes Wissen': 2, 'wenig Ahnung': 2, 'nur Gerüchte gehört': 5, 'kein Wissen': 4, }
ausbildung = {'Art': {'im Nahkampf': 2, 'im Fernkampf': 4, 'in Selbstverteidigung': 2, 'im Handwerk': 3, 'als Führungsperson': 1, 'in Medizin': 3, 'über altes Wissen': .5}, 'Güte': {'exzellente': 2, 'fortgeschrittene': 5, 'grundlegende': 4, 'schlechte': 2, 'fehlerhafte': .5}, 'Anzahl': {1: 1, 2: 2, 3: 1, 4: .5}}
schwerpunkte = {'Attribute': {'Körperlich': 1, 'Sozial': 1, 'Geistig': 1}, 'Strategie': {'Offensiv': 1, 'Defensiv': 1, 'Passiv': 1}}
factor = {'exzellente': 3, 'fortgeschrittene': 2, 'grundlegende': 1, 'schlechte': 0, 'fehlerhafte': -2}
skills = {'im Nahkampf': ['Nahkampf', 'Widerstand'], 'im Fernkampf': ['Fernkampf', 'Wahrnehmen'], 'in Selbstverteidigung': ['Widerstand', 'Wille', 'Verstecken'], 'im Handwerk': ['Handwerk'], 'als Führungsperson': ['Wille', 'Lügen', 'Wahrnehmen'], 'in Medizin': ['Medizin'], 'über altes Wissen': ['Wahrnehmen']}
poolMaxes = {'Nahkampf': 7, 'Fernkampf': 7, 'Widerstand': 5, 'Wille': 3, 'Lügen': 6, 'Wahrnehmen': 6, 'Verstecken': 6, 'Handwerk': 6, 'Medizin': 6}
stämme = {'Fianna': 1, 'Glaswandler': 1, 'Kinder Gaias': 1, 'Knochenbeißer': 1, 'Nachfahren des Fenris': 1, 'Rote Klauen': 1, 'Schattenlords': 1, 'Schwarze Furien': 1, 'Silberfänge': 1, 'Sternenträumer': 1, 'Stillen Wanderer': 1, 'Uktena': 1, 'Wendigo': 1}
vorzeichen = {'Ragabash': 1, 'Theurge': 1, 'Philodox': 1, 'Galliard': 1, 'Ahroun': 1, }
bruten = {'Menschling':4,'Metis':1,'Lupus':1}

Ränge = {-1:'Cliath',0:'Cliath',1:'Cliath',2:'Pflegling',3:'Pflegling',4:'Pflegling',5:'Adren',6: 'Adren',7: 'Athro',8:'Athro',9:'Ältester',10:'Ältester',11:'Ältester',12:'Legende'}


beziehungen = {'liebt','mag','lehrt','bewundert','beneidet','mag XX nicht','belächelt','bemitleidet','ist verwandt mit','würde das eigene Leben für XX opfern','rivalisiert mit','streitet häufig mit','vertraut XX blind'}

berufe = {
    'Maurer','Ingenieur','Hausmeister','Trainer','Lehrer','Grundschullehrer','Kindergärtner','Buchhalter','Wirtschaftspartner','Apotheker',
    'Chemiker','Architekt','Webdesigner','Produktdesigner','Babysitter','Hundesitter','Kosmetiker','Friseur','Hostess','Reiningskraft','Yogalehrer',
    'Optiker','Bäcker','Fleischer','Florist','Kassierer','Verkaufer','Store Manager','Banker','Kredithai','Beikoch','Kellner','Koch','Tellerwäscher',
    'Altenpfleger','Arzt','Zahnarzt','Krankenpfleger','Arzthelfer','Mechaniker','Gärtner','Heizungsbauer','Maler','Schneider','Steinmetz','Schmied',
    'Klempner','Schlosser','Monteur','Installateur','Schuster','Techniker','Tischler','Schlosser','Glaser','Zimmerer','Makler','Vermieter',
    'Elektroniker','Schleifer','Schweißer','Data Scientist','Programmierer','Empfangsmitarbeiter','Flugbegleiter','Fotograg','Model','Tänzer',
    'Schauspieler','Regisseur','Bauer','Erntehelfer','Influencer','Eventmanager','PR Manager','Flyerverteiler','Dreher','Maschinenenbauer',
    'Dolmetscher','Pressereferent','HR Manager','Anwalt','Richter','Notar','Detektiv','Türsteher','Busfahrer','Einkäufer','Fahrer','Lagerist',
    'Trucker','Postbote','Versicherungsmakler','Handelsvertreter','Archivar','Sekretär','Projekt Manager','Biologe','Geologe','Physiker',
}

names = {}
surnames = []
with open('/var/www/FlaskApp/FlaskApp/Vornamen_2018_Koeln.csv', 'r', encoding='utf8') as file:
    rawnames = csv.DictReader(file, delimiter=';')
    for nr, row in enumerate(rawnames):
        # print(dict(row))
        names[nr] = dict(row)
    print(f'Vornamen: {len(names)}')

with open('/var/www/FlaskApp/FlaskApp/us.txt', 'r') as file:
    for line in file:
        surnames.append(line[:-1])
    print(f'Nachnamen: {len(surnames)}')

# =================================================================
# RANDOM SELECTION METHODS
# =================================================================

def DrawWithWeightsUnique(possibilities, exceptions):
    draw = DrawWithWeights(possibilities)
    while (draw in exceptions and len(exceptions) < len(possibilities)):
        draw = DrawWithWeights(possibilities)
    return draw


def DrawWithWeights(possibilities):
    sumP = sum(possibilities.values())

    draw = random.uniform(0, sumP)
    counter = 0
    for choice in possibilities.keys():
        counter += possibilities[choice]
        if draw <= counter or counter == sumP:
            return choice

def DrawKeyUnique(possibilities, exceptions):
    draw = DrawKey(possibilities)
    while (draw in exceptions and len(exceptions) < len(possibilities)):
        draw = DrawKey(possibilities)
    return draw

def DrawKey(theDict):
    return list(theDict.keys())[random.randint(0, len(theDict.keys()) - 1)]


def GetRandomVorname(initSeed=0,sex=''):
    if initSeed != 0:
        random.seed(initSeed)
    nameData = names[random.randint(0, len(names)-1)]
    if sex != '':
        while nameData['geschlecht']!=sex:
            nameData = names[random.randint(0, len(names)-1)]
    return nameData['vorname'].replace('_',' ')

def GetRandomNachname(initSeed=0):
    if initSeed != 0:
        random.seed(initSeed)
    return surnames[random.randint(0, len(surnames)-1)]


# =================================================================
# CREATION METHODS
# =================================================================

def NameToSeed(name):
    seed = int(hashlib.shake_256(name.encode('utf8')).hexdigest(10), 16)
    random.seed(seed)

def MakeValue(nsc):
    if 'ausbildung' not in nsc:
        print('Ausbildungen sollten erstellt werden, bevor Würfelpools erzeugt werden.')
        return nsc
    NameToSeed(nsc['vorname']+' '+nsc['nachname'])
    baseVal = (3 if nsc['art'] == 'Kinfolk' else 5) + int(nsc['Powerlevel'] / 2)
    charPools = {'Nahkampf': baseVal, 'Fernkampf': baseVal, 'Widerstand': baseVal, 'Wille': baseVal, 'Lügen': baseVal,
                 'Wahrnehmen': baseVal, 'Verstecken': baseVal, 'Handwerk': baseVal, 'Medizin': baseVal}
    badSkill = min(0, nsc['Powerlevel'] - 2)
    for i in range(-badSkill):
        charPools[DrawKey(charPools)] -= 1
    goodSkill = min(9, 2 + nsc['Powerlevel'])
    for i in range(goodSkill):
        charPools[DrawKey(charPools)] += 1
    for SkillArt, SkillGüte in nsc['ausbildung']:
        for skill in skills[SkillArt]:
            charPools[skill] += factor[SkillGüte]
    for idx, pool in enumerate(charPools):
        charPools[pool] = min(charPools[pool], poolMaxes[pool] + nsc['Powerlevel'])
        charPools[pool] = max(charPools[pool], 1)
    nsc['dicePools'] = charPools
    return nsc

def MakeDescriptions(nsc):
    NameToSeed(nsc['vorname']+' '+nsc['nachname'])
    nsc['alter'] = DrawWithWeights(hintergründe["Alter"])
    nsc['zeit'] = DrawWithWeights(hintergründe["Zeit"])
    nsc['familie'] = DrawWithWeights(hintergründe["Familie"]) if  nsc['art']=="Kinfolk"  else DrawWithWeightsUnique(hintergründe["Familie"],["Verheiratet (mit Garou)"])
    nsc['motivation'] = DrawWithWeights(motivation)
    nsc['pläne'] = DrawWithWeights(pläne)
    nsc['motto'] = DrawWithWeights(richtlinien)
    nsc['wyrm'] = DrawWithWeights(einstellung['Wyrm'])
    nsc['rangordnung'] = DrawWithWeights(einstellung['Rangordnung'])
    nsc['scRudel'] = DrawWithWeights(einstellung['Rudel'])
    nsc['plot'] = DrawWithWeights(wissen)
    nsc['reaktion'] = DrawWithWeights(schwerpunkte['Strategie'])
    return nsc

def MakeBreed(nsc,brut=''):
    NameToSeed(nsc['vorname']+' '+nsc['nachname'])
    if nsc['art'] != 'Kinfolk' and nsc['art'] != 'Vampir' and nsc['art'] != 'Human' and nsc['art'] != 'Fomor':
        nsc['brut'] = DrawWithWeights(bruten) if brut =='' else brut
        #print(f'{nsc["vorname"]} {nsc["nachname"]}, {nsc["art"]} {nsc["brut"]} {nsc["stamm"]}')
        nsc['gaben'] = {}
        for i in range(3+nsc['Powerlevel']):
            if nsc['Powerlevel']<-1:
                nsc['rang'] = 'Cliath'
            elif nsc['Powerlevel']>11:
                nsc['rang'] = 'Legende'
            else:
                nsc['rang'] = Ränge[nsc['Powerlevel']]
            gabe = LookUpTexteByName(DrawKeyUnique(GetGaben(nsc['brut'], nsc['art'], nsc['stamm'], nsc['rang']),nsc['gaben']))
            nsc['gaben'][gabe['name']] = gabe
    if nsc['art'] == 'Fomor':
        nsc['gaben'] = {}
        if random.random()>.2:
            nsc['gaben']['Immunität gegen das Delirium'] = LookUpTexteByName('Immunität gegen das Delirium')
        if random.random()>.66:
            nsc['gaben']['Berserker'] = gaben.LookUpTexteByName('Berserker')
        for i in range(max(1,min(nsc['Powerlevel'],4))):
            gabe = LookUpTexteByName(DrawKeyUnique(GetFomorGaben(),nsc['gaben']))
            nsc['gaben'][gabe['name']] = gabe
            pass
    return nsc

def MakeExpertise(nsc):
    NameToSeed(nsc['vorname']+' '+nsc['nachname'])
    nrAusbildung = DrawWithWeights(ausbildung['Anzahl']) + (0 if nsc['art'] == "Kinfolk" else 1)
    nscAusbildungen = []
    nscGüte = []
    for ausCounter in range(nrAusbildung):
        nscAusbildungen.append(DrawWithWeightsUnique(ausbildung['Art'], nscAusbildungen))
        nscGüte.append(DrawWithWeightsUnique(ausbildung['Güte'], [] if nsc['art'] == "Kinfolk" else ['fehlerhafte']))
    nsc['ausbildung'] = list(zip(nscAusbildungen,nscGüte))
    return nsc

def MakePlayAdvise(nsc):
    NameToSeed(nsc['vorname']+' '+nsc['nachname'])
    nsc.update(MakeSpielAnweisung())
    return nsc


def MakeBase(seed=-1, Art='Kinfolk', Stamm='',Powerlevel=0,occupation=''):
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
        print(f'{seed}, {Art}, {Stamm}, {Powerlevel}, {occupation}')
        return MakeBase(-1, Art,Stamm,Powerlevel,occupation)
    nsc= {
        'vorname':nameData['vorname'].replace('_',' '),
        'nachname':surname,
        'pronomen':'er' if nameData['geschlecht'] == 'm' else 'sie',
        'possesivpronomen':'seine' if nameData['geschlecht'] == 'm' else 'ihre',
        'Powerlevel':Powerlevel,
        'occupation':occupation,
        'job':random.sample(berufe,1)[0]
    }
    if Art == 'Human':
        nsc['art'] = Art
        return nsc

    NameToSeed(nsc['vorname']+' '+nsc['nachname'])
    if Art != 'Kinfolk':
        drawnArt = DrawWithWeights(vorzeichen)
        if Art == 'Garou':
            nsc['art'] = drawnArt
        else:
            nsc['art'] = Art
    else:
        nsc['art'] = Art
    if Art == 'Fomor':
        nsc.update(MakeFomor(seed))
        return nsc
    if Stamm == '':
        nsc['stamm'] = DrawWithWeights(stämme)
    elif Stamm == 'Tänzer der schwarzen Spirale':
        nsc['stamm'] = 'Tänzer der schwarzen Spirale'
        nsc.update(MakeBSD(seed))
    else:
        nsc['stamm'] = Stamm
    return nsc

def TextWithImage(text,imageURL):
    if imageURL == 'https://cdn.pixabay.com/photo/2020/06/05/16/27/excuse-me-5263696_960_720.jpg':
        return f'''
    <figure style="float:left;margin-right: 10px;margin-top:0px;margin-left:0px">
    <img src="{imageURL}"  width="300" height="200" title=" Source: Pixabay.com" style="filter: grayscale(75%); ">
      <figcaption>Generated.Photos is not whitelisted by Pythonanywhere yet </figcaption>
    </figure>
    <p style="min-height:200px;">{text}</p><br>'''

    return f'''
    <figure style="float:left;margin-right: 10px;margin-top:0px;margin-left:0px">
    <img src="{imageURL}"  width="256" height="256" title="AI Generated Image, Source: Generated Photos" style="filter: grayscale(75%); ">
      <figcaption>Photo by <a href="https://generated.photos">Generated Photos</a></figcaption>
    </figure>
    <p style="min-height:200px;">{text}</p><br>
    </p><br>

    '''
    pass


def GetFace(nsc):
    NameToSeed(nsc['vorname']+' '+nsc['nachname'])
    url = "https://api.generated.photos/api/v1/faces?api_key=9431GheN9YeSBMHadx2bow"
    if nsc['alter'] in ['gerade Volljährig','zwischen 20 und 30']:
        bildAlter = 'young-adult'
    elif nsc['alter'] in ['anfang 30','mitte 30','anfang 40','mitte 40']:
        bildAlter = 'adult'
    else:
        bildAlter = 'elderly'
    if nsc["scRudel"] in ['Liebevoll', 'Freundlich', 'Offen']:
        bildEmotion = 'joy'
    else:
        bildEmotion = 'neutral'
    gender='male'if nsc['pronomen'] =='er' else 'female'
    try:
        url = f'https://generated.photos/faces/{bildAlter}/{bildEmotion}/{gender}'
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        imgs = []
        for post in soup.findAll('div', {'class': 'card-image'}):
            imgs.append(str(post.find('img')).split('"')[-2])
        return random.choice(imgs)
    except:
        pass
    return 'https://cdn.pixabay.com/photo/2020/06/05/16/27/excuse-me-5263696_960_720.jpg'

    pass

def PrintNSC(nsc,packname,language='Plain',shortPrint=False):
    result = Header(nsc['vorname'],nsc['nachname'],language)

    #Rudel
    if packname is not None and 'packname' in packname:
        result += PrintPack(packname['packname'],nsc['vorname'])
        packString = f'?packname={packname["packname"]}'
    else:
        packString = ''

    #Rang und Rolle
    if 'rang' in nsc:
        result += f'{nsc["rang"]} '

    result += f'{nsc["art"]}'
    if 'stamm' in nsc:
        result +=f' {nsc["stamm"]}'
    if 'brut' in nsc and len(nsc['brut'])>0:
        result += f' ({nsc["brut"]})'+Newline(language)
    else:
        result += Newline(language)
    if 'stamm' in nsc and nsc['stamm'] == 'Tänzer der schwarzen Spirale':
        result +=f'{nsc["Abstammung"]}'+Newline(language)

    #Rollenspiel
    result += Header('Rollenspiel', 'Vorschläge', language, 3)
    result += f'Ein Persönlichkeitsmerkmal ist {Bold(nsc["grundstimmung"],language)}'+Newline(language)
    result += 'Körperhaltung: '+Bold(nsc["haltung"][0],language)+((f' ({nsc["haltung"][1]})'+Newline(language)) if not shortPrint else Newline(language))
    result += 'Gestik: '+Bold(nsc["gestik"][0],language)+((f' ({nsc["gestik"][1]})'+Newline(language)) if not shortPrint else Newline(language))
    result += 'Mimik: '+Bold(nsc["mimik"][0],language)+((f' ({nsc["mimik"][1]})'+Newline(language)) if not shortPrint else Newline(language))

    #Aussehen
    result += Header('Aussehen','',language,3)
    result += TextWithImage(PrintBeschreibung(nsc,Newline(language)),GetFace(nsc))

    #Beschreibung
    result += Header('Beschreibung:', '', language, 3)
    result += f'{nsc["vorname"]} ({nsc["alter"]}), ist {nsc["zeit"]} und aktuell {Bold(nsc["familie"],language)}. {StartCapital(nsc["pronomen"])} arbeitet(e) als {nsc["job"]}. {Newline(language)}'
    result += f'{nsc["possesivpronomen"][0].upper()+nsc["possesivpronomen"][1:]} eigentliche Motivation ist {nsc["motivation"]} und der zur Zeit verfolgte Plan hat {nsc["pläne"]} als Ziel.{Newline(language)}'
    result += f'Die Handlungen sind geprägt durch das Motto {Bold(nsc["motto"],language)}'
    if nsc['art'] == 'Human':
        result += '.'+Newline(language)+f'Gegenüber dem SC Rudel ist {nsc["pronomen"]} {Bold(nsc["scRudel"],language)}.'
    else:
        if 'stamm' in nsc and nsc['stamm'] == 'Tänzer der schwarzen Spirale':
            result += f'. Die Rangordnung ist {nsc["rangordnung"]} für {nsc["pronomen"] if nsc["pronomen"]=="sie" else "ihn"}. {Newline(language)}'
            pass
        else:
            result += f' und über den Wyrm denkt {nsc["pronomen"]}: {nsc["wyrm"]}.{Newline(language)}'
            result += f'Die Rangordnung ist für {nsc["pronomen"] if nsc["pronomen"]=="sie" else "ihn"} {nsc["rangordnung"]} und gegenüber dem SC Rudel ist {nsc["pronomen"]} {Bold(nsc["scRudel"],language)}. '
    result += f'Über den {Bold("Plot",language)} hat {nsc["vorname"]} {nsc["plot"]}.'
    result += f'In Konflikten reagiert {nsc["pronomen"]} meist {Bold(nsc["reaktion"],language)}.{Newline(language)}'
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
            if len(nsc['Mutationen'])==0:
                result += 'keine erkennbare Entstellung'
    if nsc['art'] == 'Fomor':
        result += f'Die prägende Sünde von {nsc["vorname"]} ist {Bold(nsc["Sünde"],language)}. {Newline(language)} '
        result += f'{Bold("Äußere Merkmale:",language)}{Newline(language)}'
        if len(nsc['Mutationen'])>0:
            for merkmal in nsc['Mutationen']:
                if nsc['Mutationen'][merkmal][0] == 'Tierisch':
                    result += f' {merkmal} wie von {nsc["Mutationen"][merkmal][1]}{Newline(language)}'
                elif nsc['Mutationen'][merkmal][0] == 'Verderbnis':
                    result += f' {merkmal} {"sehen" if merkmal =="Die Augen" else "sieht"} {nsc["Mutationen"][merkmal][1]} aus{Newline(language)}'
                elif nsc['Mutationen'][merkmal][0] == 'Verzerrung':
                    result += f' {merkmal} {"wirken" if merkmal =="Die Augen" else "wirkt"} {nsc["Mutationen"][merkmal][1]}{Newline(language)}'
        else:
            result += 'keine körperlichen Entstellungen'


    #Arbeit oder Amt
    if len(nsc['occupation'])>0:
        if nsc['art'] != 'Kinfolk':
            result += f'In der Septe hat {nsc["vorname"]} folgende Ämter: {Bold(nsc["occupation"],language)}'+Newline(language)
        else:
            result += f'In der Siedlung arbeitet {nsc["vorname"]} als {Bold(nsc["occupation"],language)}'+Newline(language)

    #ausbildung
    if not shortPrint:
        result += f'Um einen Platz in der Gesellschaft einzunehmen gab es {len(nsc["ausbildung"])} Ausbildung{"en" if len(nsc["ausbildung"])>1 else ""} für {nsc["pronomen"] if nsc["pronomen"]=="sie" else "ihn"}:{Newline(language)}'
        result += ListLines([f'{güte} Ausbildung {Bold(ausb,language)}' for ausb,güte in nsc["ausbildung"]], language)

    #Würfelpools
    result += Header('Würfelpools',language,3)
    result += Table(6,[f'{cell}' for pool in nsc['dicePools'] for cell in [pool,nsc["dicePools"][pool]]], language)

    #Gaben
    if nsc['art'] != 'Kinfolk' and 'gaben' in nsc:
        result += Header('Gaben','Vorschläge',language,3)
        if not shortPrint:
            result += ListLines([Bold(gabe,language)+':'+nsc['gaben'][gabe]['fluffText']+Newline(language)+Bold('System: ',language)+nsc['gaben'][gabe]['systemText'] for gabe in nsc['gaben']], language)
        else:
            result += ListLines([Bold(gabe,language) for gabe in nsc['gaben']], language)


    if not shortPrint:
        baseLink = Newline("HTML")+f'<a class="no-print" href="http://{baseURL}/nsc/'
        art = nsc["art"].lower() if nsc["art"] == "Kinfolk" or nsc["art"] == "Human" or nsc["art"] == "Fomor" else "garou"
        if 'stamm' in nsc and nsc['stamm'] == 'Tänzer der schwarzen Spirale':
            art = 'bsd'
        seed =(nsc["vorname"]+" "+nsc["nachname"]).replace(" ","_")

        result += baseLink + f'{art}/{nsc["Powerlevel"]}/{language.lower()}/{seed}{packString}">Dieser NCS ({nsc["vorname"]+" "+nsc["nachname"]})</a>'
        result += baseLink + f'{art}/{nsc["Powerlevel"]+1}/{language.lower()}/{seed}{packString}">Stärker</a>'
        result += baseLink + f'{art}/{nsc["Powerlevel"]-1}/{language.lower()}/{seed}{packString}">Schwächer</a>{Newline("HTML")}'
        if language == 'HTML':
            result += baseLink+f'{art}/{nsc["Powerlevel"]}/latex/{seed}{packString}">Dieser NCS ({seed}) als LaTeX Subsection</a>'
        else:
            result += baseLink+f'{art}/{nsc["Powerlevel"]}/html/{seed}{packString}">Dieser NCS ({seed}) als HTML Subsection</a>'
        result += baseLink+f'{art}/{nsc["Powerlevel"]}/{language.lower()}">Zufall neu</a>'
    return result

def BuildNSC(seed=-1, Art='Kinfolk', Stamm='', Powerlevel=0, language='Plain',packname='',occupation='',brut = '',shortPrint = True):
    nsc = MakeBase(seed, Art, Stamm, Powerlevel, occupation)
    nsc = MakeBeschreibung(nsc)
    nsc = MakeBreed(nsc,brut)
    nsc = MakePlayAdvise(nsc)
    nsc = MakeExpertise(nsc)
    nsc = MakeDescriptions(nsc)
    nsc = MakeValue(nsc)
    art = nsc["art"].lower() if nsc["art"] == "Kinfolk" or nsc["art"] == "Human" else "garou"
    seed =(nsc["vorname"]+" "+nsc["nachname"]).replace(" ","_")
    if packname != '' and 'packname' in packname:
        packString = f'?packname={packname["packname"]}'
    else:
        packString =''
    nsc['link'] = f'<a href="http://{baseURL}/nsc/{art}/{nsc["Powerlevel"]}/{language.lower()}/{seed}{packString}">{nsc["vorname"]+" "+nsc["nachname"]}</a>'


    return nsc

def BuildBSD(seed=-1,Powerlevel=0, language='Plain',packname=None):
    bsd = MakeBase(seed,'Garou','Tänzer der schwarzen Spirale', Powerlevel)
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
    bsd['motto'] = DrawWithWeightsUnique(richtlinien, ['Bedacht statt Übermut'])
    seed =(bsd["vorname"]+" "+bsd["nachname"]).replace(" ","_")
    if packname is not None and 'packname' in packname:
        packString = f'?packname={packname["packname"]}'
    else:
        packString =''
    bsd['link'] = f'<a href="http://{baseURL}/nsc/bsd/{bsd["Powerlevel"]}/{language.lower()}/{seed}{packString}">{bsd["vorname"]+" "+bsd["nachname"]}</a>'
    return bsd

def BuildFomor(seed,Powerlevel,language):
    fomor = MakeBase(seed,Art='Fomor',Powerlevel=Powerlevel)
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
    fomor['motto'] = DrawWithWeightsUnique(richtlinien, ['Bedacht statt Übermut'])
    return fomor

def CreateRandom(seed=-1, Art='Kinfolk', Stamm='', Powerlevel=0, language='Plain',packname=None,occupation='',brut = '',shortPrint = True):
    return PrintNSC(BuildNSC(seed, Art, Stamm, Powerlevel, language, packname,occupation,brut,shortPrint),packname,language,shortPrint)


def CreateBSD(seed=-1,Powerlevel=0, language='Plain',packname=None):
    return PrintNSC( BuildBSD(seed,Powerlevel,language,packname), language=language,packname=packname)

def CreateFomor(seed=-1,Powerlevel=0, language='Plain'):
    return PrintNSC(BuildFomor(seed,Powerlevel,language),language=language,packname=None)



def BuildGarouPack(seed=-1,limitTribes = [],limitBreeds = [],minMembers =3,maxMembers =6):
    if seed == -1:
        packname = GenerateRandomName()
    else:
        packname = seed
    seed = int(hashlib.shake_256(f'{packname}'.encode('utf8')).hexdigest(10), 16)
    random.seed(seed)
    packMember = random.randint(minMembers,maxMembers)
    pack = []
    for i in range(packMember):
        nsc = BuildNSC(
            seed=-1,
            Art='Garou',
            packname=packname
        )
        while (len(limitTribes)>0 and nsc['stamm'] in limitTribes) or (len(limitBreeds)>0 and nsc['brut'] in limitBreeds):# or nsc['art'] !='Galliard':
            nsc = BuildNSC(
                seed=-1,
                Art='Garou',
                packname=packname
            )
        pack.append(nsc)
    return {'packname': packname,'pack':pack,'link':f'<a href="http://{baseURL}/nsc/garoupack/?packname={packname}">Rudel: {packname.replace("_"," ")}</a>'}

def BuildBSDPack(seed=-1,limitBreeds = [],minMembers =3,maxMembers =6):
    if seed == -1:
        packname = GenerateRandomName()
    else:
        packname = seed
    seed = int(hashlib.shake_256(f'{packname}'.encode('utf8')).hexdigest(10), 16)
    random.seed(seed)
    packMember = random.randint(minMembers,maxMembers)
    pack = []
    for i in range(packMember):
        nsc = BuildBSD(
            seed=-1,
            packname=packname
        )
        while (len(limitBreeds)>0 and nsc['brut'] in limitBreeds):# or nsc['art'] !='Galliard':
            nsc = BuildBSD(
                seed=-1,
                packname=packname
            )
        pack.append(nsc)
    return {'packname': packname,'pack':pack,'link':f'<a href="http://{baseURL}/nsc/bsdpack/?packname={packname}">Rudel: {packname.replace("_"," ")}</a>'}


def PrintPack(seed=-1,memberName='',language = 'HTML',limitTribes = [],limitBreeds = [],minMembers =3,maxMembers =6):
    pack = BuildGarouPack(seed,limitTribes,limitBreeds,minMembers,maxMembers)

    result = Header(pack['packname'],'',language,2) if memberName =='' else Header(pack['link'],'',language,3)
    packMemberNames = []
    for nsc in pack['pack']:
        packMemberNames.append(f'{nsc["vorname"]} {nsc["nachname"]}')
        if language == 'HTML':
            result += f'{Newline(language)}<a href="http://{baseURL}/nsc/garou/0/html/{nsc["vorname"]+"_"+nsc["nachname"]}?packname={pack["packname"]}">{nsc["vorname"]} {nsc["nachname"]} ({nsc["art"]} von den {nsc["stamm"]})</a>'
        else:
            result += f'{nsc["vorname"]} {nsc["nachname"]} ({nsc["art"]} von den {nsc["stamm"]})'+Newline(language)
    result += BuildRelationships(packMemberNames,memberName,language)
    return result

def PrintBSDPack(seed=-1,limitBreeds = [],memberName='',minMembers =3,maxMembers =6,language = 'HTML'):
    pack = BuildBSDPack(seed,limitBreeds,minMembers,maxMembers)
    result = Header(pack['packname'],'',language,2) if memberName =='' else Header(pack['link'],'',language,3)
    packMemberNames = []
    for nsc in pack['pack']:
        packMemberNames.append(f'{nsc["vorname"]} {nsc["nachname"]}')
        if language == 'HTML':
            result += f'{Newline(language)}<a href="http://{baseURL}/nsc/bsd/0/html/{nsc["vorname"]+"_"+nsc["nachname"]}?packname={pack["packname"]}">{nsc["vorname"]} {nsc["nachname"]} ({nsc["art"]} von den {nsc["stamm"]})</a>'
        else:
            result += f'{nsc["vorname"]} {nsc["nachname"]} ({nsc["art"]} von den {nsc["stamm"]})'+Newline(language)
    result += BuildRelationships(packMemberNames, memberName, language)
    return result

def BuildRelationships(pack,activeName='',language='HTML'):
    result = Header('Beziehungen' 'innerhalb des Rudels:',language,3)
    vornamen = {name.split(' ')[0] for name in pack}
    if len(vornamen)==len(pack):
        pack = vornamen
    for member in pack:
        relations = random.sample(beziehungen,2)
        others = random.sample([m for m in pack if m != member],2)
        #print(relations)
        #print(others)
        relString = [(relation +' '+ other) if 'XX' not in relation else (relation.replace('XX',other)) for relation,other in zip(relations,others)]
        result += f'{Newline(language)}{member} {relString[0]} und {relString[1]}.'
    if activeName=='':
        return result
    else:
        return result.replace(f'{activeName} ',f'{Bold(activeName,language)} ')




