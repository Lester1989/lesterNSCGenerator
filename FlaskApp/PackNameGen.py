import random

namensArt = ['die NomenVerb', 'die adjektiv NomenVerb','die Verb von Nomen', 'weird']

nomen = {
    'gut':['Mond','Luna','Wyldnis','Wolf','Mutter','Herz','Ernte','Kind'],
    'gewalt':['Blut','Schlacht','Ende','Feuer','Klaue','Zahn','Wut','Rache','Knochen','Maul','Blitz','Fang','Schlag'],
    'neutral':['Ruf','Geist','Schwanz','Pfote','Fell','Vater','Schrei','Dunkel','Fleisch','Auge','Makel'],
    'böse':['Wyrm','Alptraum','Hölle','Baal','Fallout','Feind','Dämonen','Tod','Tänzer','Spiralen','Gift'],
}

verben = {
    'gut':['Retter',],
    'gewalt':['Reißer','Brecher','Sprenger','Brenner','Schlachter','Rufer','Fresser','Schläger','Töter'],
    'neutral':['Bringer','Träumer'],
    'böse':['Tänzer','Zerstörer','Verschlinger','Vergifter','Rächer'],
}

adjektive = {
    'gut': ['weisen','klugen'],
    'gewalt': ['schnellen','starken','blutigen','reißenden','wutenden','rächenden'],
    'neutral': ['neuen'],
    'böse': ['stinkenden', 'blutenden', 'tanzenden', 'rasenden'],
}

weirds = ['Ratzupaltuff','Cowabunga','YippiKaYay']

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

