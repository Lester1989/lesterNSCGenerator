import random
import json
from .config import basePath

namensArt = ['die NomenVerb', 'die adjektiv NomenVerb','die Verb von Nomen', 'weird']

with open(basePath+'/jsons/nomen.json', 'r', encoding='utf-8') as infile:
    nomen = json.load(infile)
with open(basePath+'/jsons/verben.json', 'r', encoding='utf-8') as infile:
    verben = json.load(infile)
with open(basePath+'/jsons/adjektive.json', 'r', encoding='utf-8') as infile:
    adjektive = json.load(infile)
with open(basePath+'/jsons/weirds.json', 'r', encoding='utf-8') as infile:
    weirds = json.load(infile)

def GenerateRandomName(seed = -1):
    if seed != -1:
        random.seed(seed)
    art = random.choice(namensArt[:-1])
    if art == 'die NomenVerb':
        sentiment = random.choice(list(nomen))
        nom = random.choice(list(nomen[sentiment]))
        sentiment = random.choice(list(verben))
        verb = random.choice(list(verben[sentiment])).lower()
        return f'Die {nom}{verb}'
    elif art == 'die adjektiv NomenVerb':
        sentiment = random.choice(list(nomen))
        nom = random.choice(list(nomen[sentiment]))
        sentiment = random.choice(list(verben))
        verb = random.choice(list(verben[sentiment])).lower()
        sentiment = random.choice(list(adjektive))
        adjektiv = random.choice(list(adjektive[sentiment]))
        return f'Die {adjektiv} {nom}{verb}'
    elif art == 'die Verb von Nomen':
        sentiment = random.choice(list(nomen))
        nom = random.choice(list(nomen[sentiment]))
        sentiment = random.choice(list(verben))
        verb = random.choice(list(verben[sentiment]))
        return f'Die {verb} von {nom}'
    else:
        return random.choice(weirds)

