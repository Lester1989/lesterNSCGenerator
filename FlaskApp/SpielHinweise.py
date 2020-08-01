import random
import json
from .NSCGenUtils import  DrawWithWeights


with open('haltungen.json', 'r', encoding='utf-8') as infile:
    haltungen = json.load(infile)
with open('gestiken.json', 'r', encoding='utf-8') as infile:
    gestiken = json.load(infile)
with open('mimiken.json', 'r', encoding='utf-8') as infile:
    mimiken = json.load(infile)
with open('merkmal.json', 'r', encoding='utf-8') as infile:
    merkmal = json.load(infile)

def MakeSpielAnweisung():
    nsc = {}
    haltung = random.choice(list(haltungen))
    nsc['haltung'] = (haltung,haltungen[haltung])
    gestik = random.choice(list(gestiken))
    nsc['gestik'] = (gestik,gestiken[gestik])
    mimik = random.choice(list(mimiken))
    nsc['mimik'] = (mimik,mimiken[mimik])
    nsc['grundstimmung'] = DrawWithWeights(merkmal)
    return nsc