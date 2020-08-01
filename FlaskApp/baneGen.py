
import hashlib
import random
from .Formatting import Bold,Newline,Header,ListLines
from .gaben import LookUpTexteByName
from .config import baseURL, basePath
from .NSCGenUtils import NameToSeed
import json




with open(basePath+'jsons/baneType.json', 'r', encoding='utf-8') as infile:
    baneType = json.load(infile)
with open(basePath+'jsons/adjektiv.json', 'r', encoding='utf-8') as infile:
    adjektiv = json.load(infile)
with open(basePath+'jsons/spiritPower.json', 'r', encoding='utf-8') as infile:
    spiritPower = json.load(infile)
with open(basePath+'jsons/powerlevelLookUp.json', 'r', encoding='utf-8') as infile:
    powerlevelLookUp = json.load(infile)
with open(basePath+'jsons/spiritSpells.json', 'r', encoding='utf-8') as infile:
    spiritSpells = json.load(infile)


def MakeBane(seed=-1,powerlevel=0):
    if (seed != -1):
        seed = seed.replace('_',' ')
        NameToSeed(seed)
    else:
        random.seed()
        seed = f'{random.sample(adjektiv,1)[0]} Plage {random.sample(baneType,1)[0]}'
        NameToSeed(seed)
    if powerlevel<len(powerlevelLookUp):
        if powerlevel<0:
            strength = powerlevelLookUp[0]
        else:
            strength = powerlevelLookUp[powerlevel]
    else:
        strength = powerlevelLookUp[-1]
    spirit = {'Name':seed,'Essenz':random.randint(spiritPower[strength][0],spiritPower[strength][1]),'powerlevel':powerlevel}
    spirit['Zorn'] = max(1,powerlevel+random.randint(int(spirit['Essenz']/3.25),int(spirit['Essenz']/2.25)))
    spirit['Gnosis'] = max(1,powerlevel+random.randint(int(spirit['Essenz']/3.25),int(spirit['Essenz']/2.25)))
    spirit['Willenskraft'] = max(1,powerlevel+random.randint(int(spirit['Essenz']/3.25),int(spirit['Essenz']/2.25)))
    spirit['Essenz'] = max(3,int((1+2*random.random())*(powerlevel+spirit['Essenz'])))
    spirit['Machtstufe'] = strength

    if strength == 'Gaffling':
        if random.random()>.5:
            spells = ['Besessenheit', 'Verderbnis']
        else:
            spells = random.sample(['Besessenheit', 'Verderbnis'],1)
    else:
        spells = ['Besessenheit', 'Verderbnis']
    spells += random.sample(spiritSpells['häufig'],1 if powerlevel<4 else 4)
    spells += random.sample(spiritSpells['besonders'],min(len(spiritSpells['besonders']),spiritPower[strength][2]))
    spirit['Zauber'] = spells
    spirit['link'] = f'<a href="{baseURL}/nsc/bane/{spirit["powerlevel"]}/html/{spirit["Name"].replace(" ","_")}"> {spirit["Name"]} </a>'
    return spirit

def PrintBane(bane,language='HTML'):
    result = Header(bane['Name'][0].upper()+bane['Name'][1:],f'({bane["Machtstufe"]})',language,3)
    result += Bold('Essenz: ',language)+str(bane['Essenz']) +Newline(language)
    result += Bold('Zorn: ',language)+str(bane['Zorn'])+Bold('  Gnosis: ',language)+str(bane['Gnosis'])+Bold('  Willenskraft: ',language)+str(bane['Willenskraft']) +Newline(language)
    result += ListLines([f'{Bold(spell,language)}: {LookUpTexteByName(spell)["fluffText"]}' for spell in bane['Zauber']],language)
    result += f'Da Plagen extrem unterschiedlich und oft abstrakt sind, ist hier keine feste Beschreibung, '
    result += f'sondern nur die Empfehlung über den Namen {bane["Name"].split(" ")[-1]} eine Umschreibung für die Spieler zu finden.'+Newline(language)
    result += f'Vergiss nicht die Gefühle der Charaktere anzusprechen. Das Adjektiv {bane["Name"].split(" ")[0]} kann hierbei '
    result += f'als Inspiration dienen. Versuche dir auch einen Geruch und ein Geräusch zu dieser Plage zu überlegen.'+Newline(language)

    result += Newline(language)+bane['link']
    result += Newline(language)+f'<a href="{baseURL}/nsc/bane/{bane["powerlevel"]+1}/{language.lower()}/{bane["Name"].replace(" ","_")}"> stärker </a>'
    result += Newline(language)+f'<a href="{baseURL}/nsc/bane/{bane["powerlevel"]-1}/{language.lower()}/{bane["Name"].replace(" ","_")}"> schwächer </a>'
    result += Newline(language)+Newline(language)+f'<a href="{baseURL}/nsc/bane/{bane["powerlevel"]}/{language.lower()}/"> zufällige Plage </a>'

    return result


def CreateBane(seed=-1,Powerlevel=0,language='Plain'):
    return PrintBane(MakeBane(seed,Powerlevel),language)



