import random
from  hashlib import md5


def NameToSeed(name):
    seed = int(md5(name.encode('utf8')).hexdigest(), 16)
    random.seed(seed)

def DrawWithWeightsUnique(possibilities,exceptions):
    draw = DrawWithWeights(possibilities)
    while(draw in exceptions and len(exceptions)<len(possibilities)):
        draw = DrawWithWeights(possibilities)
    return draw

def DrawWithWeights(possibilities):
    #Normalize
    sumP = sum(possibilities.values())

    draw = random.uniform(0, sumP)
    counter = 0
    for choice in possibilities.keys():
        counter += possibilities[choice]
        if draw <=counter or counter==sumP:
            return choice


def DrawKeyUnique(possibilities, exceptions):
    draw = DrawKey(possibilities)
    while (draw in exceptions and len(exceptions) < len(possibilities)):
        draw = DrawKey(possibilities)
    return draw

def DrawKey(theDict):
    return list(theDict.keys())[random.randint(0, len(theDict.keys()) - 1)]