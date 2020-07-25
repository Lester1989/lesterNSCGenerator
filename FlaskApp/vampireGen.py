from .Formatting import Bold, Newline, Header, ListLines

unleben = {
    'Vernichtung des Erzeugers':'',
    'Zeugen eines Kindes':'', 
    'Starre':'',
    'Lossagung vom Erzeuger':'',
    'Umzug in neue Domäne':'',
    'Konflikt mit anderem Vampir':'',
    'Wechsel der Sekte':'',
    'selbst Blutsgebunden':'',
    'jemanden Blutsgebunden':'',

}

def MakeVampire(nsc):
    nsc['Unleben'] = []    
    nsc['Kuss'] = {}
    nsc['Erzeuger'] = {}
    nsc['Kinder'] = []
    nsc['Gouhle'] = []

def PrintVampire(nsc,language):    
    result = Header('Unleben', '', language, 3)
    return result + f' Hier entsteht eine Zusammenfassung über das Unleben von {nsc["vorname"]}:{Newline(language)} Erzeuger, Kinder, Guhle, Intrigen und mehr...{Newline(language)} {Newline(language)} Vorschläge gerne an mich!'
