import json

import codecs
import os
from .config import basePath


gabenTexte = json.load(codecs.open(basePath+'/FlaskApp/gabenTexte.json', 'r', 'utf-8-sig'))

with open(basePath+'jsons/Raenge.json', 'r', encoding='utf-8') as infile:
    Ränge = list(set(json.load(infile).keys()))
with open(basePath+'jsons/BrutGabenNamen.json', 'r', encoding='utf-8') as infile:
    BrutGabenNamen = json.load(infile)
with open(basePath+'jsons/VorzeichenGabenNamen.json', 'r', encoding='utf-8') as infile:
    VorzeichenGabenNamen = json.load(infile)
with open(basePath+'jsons/StammGabenNamen.json', 'r', encoding='utf-8') as infile:
    StammGabenNamen = json.load(infile)
with open(basePath+'jsons/FomoriGabenName.json', 'r', encoding='utf-8') as infile:
    FomoriGabenName = json.load(infile)

def LookUpTexteByName(needle):
    for gabe in gabenTexte['alleGabenTexte']:
        if gabe['name'].replace(' ','') == needle.replace(' ',''):
            return gabe
    return {'name':needle,'fluffText':'nicht gefunden','systemText':'nicht gefunden'}

def GetGaben(Brut,Vorzeichen,Stamm,Rang='Cliath'):
    result = []
    for i in range(len(Ränge)):
        RangIdx = Ränge[i]
        if Stamm=='Tänzer der schwarzen Spirale':
            for gabenName in BrutGabenNamen[Brut+' des Wyrms'][RangIdx]:
                result.append(LookUpTexteByName(gabenName))
            for gabenName in VorzeichenGabenNamen[Vorzeichen+' des Wyrms'][RangIdx]:
                result.append(LookUpTexteByName(gabenName))
            for gabenName in StammGabenNamen[Stamm][RangIdx]:
                result.append(LookUpTexteByName(gabenName))
        else:
            for gabenName in BrutGabenNamen[Brut][RangIdx]:
                result.append(LookUpTexteByName(gabenName))
            for gabenName in VorzeichenGabenNamen[Vorzeichen][RangIdx]:
                result.append(LookUpTexteByName(gabenName))
            for gabenName in StammGabenNamen[Stamm][RangIdx]:
                result.append(LookUpTexteByName(gabenName))
        if RangIdx == Rang:
            break
    return {gabe['name']:{'fluffText':gabe['fluffText'],'systemText':gabe['systemText']} for gabe in result}

def GetFomorGaben():
    result = [LookUpTexteByName(gabenName) for gabenName in FomoriGabenName]
    return {gabe['name']: {'fluffText': gabe['fluffText'], 'systemText': gabe['systemText']} for gabe in result}











