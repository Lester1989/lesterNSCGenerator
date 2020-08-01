import hashlib
import random
from .NSCGenUtils import NameToSeed, DrawWithWeights
import json


with open('Kleidung.json', 'r', encoding='utf-8') as infile:
    Kleidung = json.load(infile)
with open('Kleidungsfaerbung.json', 'r', encoding='utf-8') as infile:
    Kleidungsfärbung = json.load(infile)
with open('Frisur.json', 'r', encoding='utf-8') as infile:
    Frisur = json.load(infile)
with open('Koerperbau.json', 'r', encoding='utf-8') as infile:
    Körperbau = json.load(infile)
with open('Merkmale.json', 'r', encoding='utf-8') as infile:
    Merkmale = json.load(infile)
with open('Kopf.json', 'r', encoding='utf-8') as infile:
    Kopf = json.load(infile)
with open('Augen.json', 'r', encoding='utf-8') as infile:
    Augen = json.load(infile)
with open('Haut.json', 'r', encoding='utf-8') as infile:
    Haut = json.load(infile)
with open('Zaehne.json', 'r', encoding='utf-8') as infile:
    Zähne = json.load(infile)

def MakeBeschreibung(beschreibung):
    NameToSeed(beschreibung['vorname']+' '+beschreibung['nachname'])
    beschreibung['beschreibungKleidung'] = DrawWithWeights(Kleidung)
    beschreibung['beschreibungKleidungsFarbe'] = DrawWithWeights(Kleidungsfärbung)
    beschreibung['beschreibungFrisur'] = DrawWithWeights(Frisur)
    beschreibung['beschreibungKörperbau'] = DrawWithWeights(Körperbau)
    beschreibung['beschreibungMerkmal'] = [random.choice(sorted(Merkmale))]
    beschreibung['beschreibungMerkmal'].append(random.choice(Merkmale[beschreibung['beschreibungMerkmal'][0]]))
    beschreibung['beschreibungKopf'] = DrawWithWeights(Kopf)
    beschreibung['beschreibungAugen'] = DrawWithWeights(Augen)
    additional = random.randint(0,4)
    if additional == 1:
        beschreibung['beschreibungHaut'] = DrawWithWeights(Haut)
    elif additional == 2:
        beschreibung['beschreibungZähne'] = DrawWithWeights(Zähne)
    return beschreibung

def PrintBeschreibung(beschreibung,Newline):
    result = f'{beschreibung["vorname"]} trägt {beschreibung["beschreibungKleidung"]}Kleidung in {beschreibung["beschreibungKleidungsFarbe"]} Farbtönen. '
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
