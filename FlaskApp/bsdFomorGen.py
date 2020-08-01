# -*- coding: utf-8 -*-

import random
from .NSCGenUtils import DrawWithWeights,DrawWithWeightsUnique
from .config import basePath
import json



with open(basePath+'/jsons/Entstellung.json', 'r', encoding='utf-8') as infile:
    Entstellung = json.load(infile)
with open(basePath+'/jsons/Mutation.json', 'r', encoding='utf-8') as infile:
    Mutation = json.load(infile)
with open(basePath+'/jsons/Abstammung.json', 'r', encoding='utf-8') as infile:
    Abstammung = json.load(infile)
with open(basePath+'/jsons/Geistesstoerung.json', 'r', encoding='utf-8') as infile:
    Geistesstörung = json.load(infile)
with open(basePath+'/jsons/PraegendeSuende.json', 'r', encoding='utf-8') as infile:
    PrägendeSünde = json.load(infile)


def MakeBSD(seed):
    random.seed(seed)
    bsd = {
        'Abstammung':DrawWithWeights(Abstammung),
        'Geistesstörung':{'Grad':DrawWithWeights(Geistesstörung['Grad']),'Art':DrawWithWeights(Geistesstörung['Art'])},
        'Entstellungen':[],
        'Mutationen':{},
    }
    nrEntstellungen = int(DrawWithWeights(Entstellung['Anzahl']))
    for _ in range(nrEntstellungen):
        bsd['Entstellungen'].append(DrawWithWeightsUnique(Entstellung['Art'],bsd['Entstellungen']))
    nrMutationen = int(DrawWithWeights(Mutation['Anzahl']))
    for _ in range(nrMutationen):
        art = DrawWithWeights(Mutation['Art'])
        bsd['Mutationen'][DrawWithWeightsUnique(Mutation['Merkmal'],list(bsd['Mutationen'].keys()))] = [art,DrawWithWeights(Mutation[art])]
    return bsd





def MakeFomor(seed):
    random.seed(seed)
    fomor = {
        'Mutationen':{},
        'Sünde':DrawWithWeights(PrägendeSünde)
    }
    nrMutationen = max(0,int(DrawWithWeights(Mutation['Anzahl']))-1)
    for _ in range(nrMutationen):
        art = DrawWithWeights(Mutation['Art'])
        fomor['Mutationen'][DrawWithWeightsUnique(Mutation['Merkmal'],list(fomor['Mutationen'].keys()))] = [art,DrawWithWeights(Mutation[art])]
    return fomor




