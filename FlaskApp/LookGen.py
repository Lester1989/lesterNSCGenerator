import hashlib
import random

Kleidung ={'abgerissene ','modische ','sportliche ', 'Arbeits-','Militär-','durchschnittliche ','zweckmäßige '}
Kleidungsfärbung = {'ausgeblichenen', 'bunten', 'gedeckten','tarnenden', 'extravaganten' ,'dunklen', 'hellen','braunen','grauen'}
Frisur={'hell','dunkel','blond','schwarz','rot','grau','gefärbt','bunt','dünn','fein','glatt','kraus','lockig','strähnig','zerzaust','gekämmt','gebürstet','kahl','hochgestylt','lang','kurz','in einem Zopf zusammengebunden'}
Körperbau ={'schlank','dünn','mager','groß','klein','schwach','stark','kräftig','stämmig','untersetzt','dick','muskulös','übergewichtig','durchtrainiert'}
Merkmale ={
    'eine Narbe':['im Gesicht','am Arm','an der Hand','auf der Brust','auf dem Rücken','am Hals'],
    'ein Muttermal':['im Gesicht','am Arm','an der Hand','auf der Brust','auf dem Rücken','am Hals'],
    'eine Warze':['im Gesicht','am Arm','an der Hand','auf der Brust','auf dem Rücken','am Hals'],
    'eine Tätowierung':['im Gesicht','am Arm','an der Hand','auf der Brust','auf dem Rücken','am Hals'],
    'ein Piercing':['in der Lippe','in der Nase','in der Braue','im Ohr'],
    'eine Brille':['im Gesicht','auf der Nasenspitze']
}
Kopf = {'abstehende Ohren','spitze Ohren','kleine Ohren','runde Ohren','Hakennase','Stupsnase','schiefe Nase','breite Nase','schielend','dichte Brauen','feine Brauen','volle Lippen','vorgeschobenes Kinn','breites Kinn','spitzes Kinn','hohe Wangenknochen'}
Augen = {'blau','grün','braun','stahlblau','blaugrau','blaubraun','grau','dunkelgrün','grünbraun','rot'}
Haut = {'wettergegerbt','faltig','blass','braungebrannt','unsauber','durchschnittlich'}
Zähne = {'gepflegt','gelblich','heruntergekommen','lückenhaft','strahlend weiß','dreckig'}

def NameToSeed(name):
    seed = int(hashlib.shake_256(name.encode('utf8')).hexdigest(10), 16)
    #print(f'{name}:{seed}')
    random.seed(seed)

def MakeBeschreibung(beschreibung):
    NameToSeed(beschreibung['vorname']+' '+beschreibung['nachname'])
    beschreibung['beschreibungKleidung'] = random.choice(sorted(Kleidung))
    beschreibung['beschreibungKleidungsFarbe'] = random.choice(sorted(Kleidungsfärbung))
    beschreibung['beschreibungFrisur'] = random.choice(sorted(Frisur))
    beschreibung['beschreibungKörperbau'] = random.choice(sorted(Körperbau))
    beschreibung['beschreibungMerkmal'] = [random.choice(sorted(Merkmale))]
    beschreibung['beschreibungMerkmal'].append(random.choice(Merkmale[beschreibung['beschreibungMerkmal'][0]]))
    beschreibung['beschreibungKopf'] = random.choice(sorted(Kopf))
    beschreibung['beschreibungAugen'] = random.choice(sorted(Augen))
    additional = random.randint(0,4)
    if additional == 1:
        beschreibung['beschreibungHaut'] = random.choice(sorted(Haut))
    elif additional == 2:
        beschreibung['beschreibungZähne'] = random.choice(sorted(Zähne))
    return beschreibung

def PrintBeschreibung(beschreibung,Newline):
    result = f'{beschreibung["vorname"]} tragt {beschreibung["beschreibungKleidung"]}Kleidung in {beschreibung["beschreibungKleidungsFarbe"]} Farbtönen. '
    result += f'Diese Kleidung lässt darunter einen Körper erkennen, der eher {beschreibung["beschreibungKörperbau"]} ist. '
    result += f'{beschreibung["possesivpronomen"][0].upper()+beschreibung["possesivpronomen"][1:]} Haare sind {beschreibung["beschreibungFrisur"]}'
    result += f' und {beschreibung["beschreibungMerkmal"][1]} trägt {beschreibung["pronomen"]} {beschreibung["beschreibungMerkmal"][0]}. '+Newline
    result += f'Beim Betrachten von {beschreibung["vorname"]}s Kopf fällt ein Detail in Auge: {beschreibung["beschreibungKopf"]} und {beschreibung["possesivpronomen"]} Augen sind {beschreibung["beschreibungAugen"]}. '
    if 'beschreibungHaut' in beschreibung:
        result += f'Die Haut sieht {beschreibung["beschreibungHaut"]} aus. '
    elif 'beschreibungZähne' in beschreibung:
        result += f'Wenn {beschreibung["vorname"]} den Mund öffnet kann man sehen, wie {beschreibung["beschreibungZähne"]} die Zähne sind. '
    result += Newline
    return result
