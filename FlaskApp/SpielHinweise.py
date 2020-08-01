import random
import json
from .NSCGenUtils import  DrawWithWeights
from .config import basePath


with open(basePath+'/jsons/haltungen.json', 'r', encoding='utf-8') as infile:
    haltungen = json.load(infile)
with open(basePath+'/jsons/gestiken.json', 'r', encoding='utf-8') as infile:
    gestiken = json.load(infile)
with open(basePath+'/jsons/mimiken.json', 'r', encoding='utf-8') as infile:
    mimiken = json.load(infile)
with open(basePath+'/jsons/merkmal.json', 'r', encoding='utf-8') as infile:
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