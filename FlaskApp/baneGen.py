
import hashlib
import random
from Formatting import Bold,Newline,Header,ListLines
import gaben


baneType = {'der Eitelkeit','des Geizes','der Wolllust','des Jähzorn',' der Völlerei','des Neid','der Ignoranz','der Arroganz','der Selbstgerechtigkeit','des Hochmuts',
             'des Wuchers','der Raffgier','der Habsucht','der Begierde','der Lüsternheit','der Empörung','der Entrüstung','der Verstimmung','der Unbeherrschtheit','des Grolls',
             'der Zecherei','der Zügellosigkeit','des Hasses','der Eifersucht','der Bosheit','des Gräuels','der Niedertracht','der Scheinheiligkeit','der Hinterhältigkeit',
            'der Dummheit','der Unvernunft','der Verständnislosigkeit','der Bereicherung','der Vernichtung','des Zerfalls','des Verderbens','des Massakers','der Zersetzung',
            'der Zerstörung','des Unheils','des Chaos','der Unruhe','der Leere','der Armut','des Unglücks','der Unwahrheit','der Spirale','des Egoismus','der Lüge','des Schwindels',
            'der List','der Verzerrung','der Verfälschung','des Spottes','der Anmaßung','der Beleidigung','der Erniedrigung','der Schmach','der Verachtung','der Verwirrung',
            'des Zwiespalts','der Schwäche','des Mangels','der Angst','der Panik','der Hysterie','aus Scherben','aus Schrott','der Befleckung','der Verunreinigung',
            'des Gebrechens','der Qual','der Verwesung','des Siechtums','aus Schleim','aus Müll','aus Abfall','aus Unrat','aus Schweröl','aus Giftmüll','der Strahlung',
            'des Baalsfeuers','des Smogs','der Krankheit','der Seuche','des Eiters',
}

adjektiv = {'stinkende','dröhnende','stechende','schwehlende','farblose','schmutzige','schändliche','brutale',
            'widerwärtige','hässliche','faulige','grausame','entsetzliche','grässliche','schaurige','höllische',
            'grausige','ätzende','abstoßende','ruchlose','fiese','angrifflustige','aufgebrachte','aggressive',
            'erboste','verlockende','verfressene'}

spiritPower = {'Gaffling':[9,18,1],'Zackling':[19,30,2],'Incarna-Avatar':[45,80,4],'Incarna':[120,200,20]}

powerlevelLookUp =['Gaffling','Gaffling','Zackling','Zackling','Zackling','Zackling','Incarna-Avatar','Incarna-Avatar','Incarna-Avatar','Incarna']

spiritSpells ={
    'häufig':['Airtensinn','Materialisieren','Neubildung','Reichsinn'],
    'besonders':['Aufwind','Einfrieren','Elektrische Systeme kontrollieren','Entladung','Erleuchten','Feuer erzeugen','Fluten','Gestaltwandel','Glas zerschlagen','Heilung','Kiebitzen','Kurzschluss','Mondbrücke öffnen','Rüstung','Schandfleck reinigen','Schnellflug','Spurenlesen','Umbrabeben','Wind erzeugen'],
    'plagenzauber':['Besessenheit','Berührung der Fäulnis','Raserei hervorrufen','Verderbnis']
}


def NameToSeed(name):
    seed = int(hashlib.shake_256(name.encode('utf8')).hexdigest(10), 16)
    random.seed(seed)

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
    spirit['link'] = f'<a href="http://lester89.pythonanywhere.com/nsc/bane/{spirit["powerlevel"]}/html/{spirit["Name"].replace(" ","_")}"> {spirit["Name"]} </a>'
    return spirit
    pass

def PrintBane(bane,language='HTML'):
    result = Header(bane['Name'][0].upper()+bane['Name'][1:],f'({bane["Machtstufe"]})',language,3)
    result += Bold('Essenz: ',language)+str(bane['Essenz']) +Newline(language)
    result += Bold('Zorn: ',language)+str(bane['Zorn'])+Bold('  Gnosis: ',language)+str(bane['Gnosis'])+Bold('  Willenskraft: ',language)+str(bane['Willenskraft']) +Newline(language)
    result += ListLines([f'{Bold(spell,language)}: {gaben.LookUpTexteByName(spell)["fluffText"]}' for spell in bane['Zauber']],language)
    result += f'Da Plagen extrem unterschiedlich und oft abstrakt sind, ist hier keine feste Beschreibung, '
    result += f'sondern nur die Empfehlung über den Namen {bane["Name"].split(" ")[-1]} eine Umschreibung für die Spieler zu finden.'+Newline(language)
    result += f'Vergiss nicht die Gefühle der Charaktere anzusprechen. Das Adjektiv {bane["Name"].split(" ")[0]} kann hierbei '
    result += f'als Inspiration dienen. Versuche dir auch einen Geruch und ein Geräusch zu dieser Plage zu überlegen.'+Newline(language)

    result += Newline(language)+bane['link']
    result += Newline(language)+f'<a href="http://lester89.pythonanywhere.com/nsc/bane/{bane["powerlevel"]+1}/{language.lower()}/{bane["Name"].replace(" ","_")}"> stärker </a>'
    result += Newline(language)+f'<a href="http://lester89.pythonanywhere.com/nsc/bane/{bane["powerlevel"]-1}/{language.lower()}/{bane["Name"].replace(" ","_")}"> schwächer </a>'
    result += Newline(language)+Newline(language)+f'<a href="http://lester89.pythonanywhere.com/nsc/bane/{bane["powerlevel"]}/{language.lower()}/"> zufällige Plage </a>'
    result += Newline(language)+f'<a href="http://lester89.pythonanywhere.com/"> home </a>'

    return result


def CreateBane(seed=-1,Powerlevel=0,language='Plain'):
    return PrintBane(MakeBane(seed,Powerlevel),language)



