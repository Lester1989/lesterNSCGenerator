import random
import time
import json
from .kinfolkGen import GetRandomVorname, GetRandomNachname, BuildNSC, BuildBSD, BuildGarouPack, BuildBSDPack
from .baneGen import MakeBane
from .Formatting import Bold, Newline, Header, ListLines, Table

# encounter = {name,text,nscConditions}
# nscCondition = {'sex':m/w,[beschreibungsname:[Möglichkeiten]]}

# tokens:
#  CHAR$ -> $ is index in nscConditions

tokens = ['CHAR', 'NEWLINE']


with open('stadtEncounter.json', 'r', encoding='utf-8') as infile:
    stadtEncounter = json.load(infile)
with open('wildnisEncounter.json', 'r', encoding='utf-8') as infile:
    wildnisEncounter = json.load(infile)
with open('umbraEncounter.json', 'r', encoding='utf-8') as infile:
    umbraEncounter = json.load(infile)


def CheckNSCwithConditions(nsc, conditions, chars):
    ok = True
    for otherNSC in chars.values():
        if otherNSC['vorname'] == nsc['vorname'] and otherNSC['nachname'] == nsc['nachname']:
            return False
    for condition, value in conditions.items():
        if condition == 'art':
            continue
        if 'NICHT' in condition:
            condition = condition.replace('NICHT', '')
            if isinstance(value, list):
                thisCondition = nsc[condition] not in value
            else:
                thisCondition = nsc[condition] != value
        else:
            if isinstance(value, list):
                thisCondition = nsc[condition] in value
            else:
                thisCondition = nsc[condition] == value
        # print(f'checking {condition} for {value} (is: {nsc[condition]}): {thisCondition}')
        ok = ok and thisCondition
    return ok


def HandleSeed(encounter, nscNumber, chars, token, counter=0):
    seed = GetRandomVorname() + '_' + GetRandomNachname()
    if 'seed' in encounter['nscConditions'][nscNumber]:
        seed = encounter['nscConditions'][nscNumber]['seed']
    elif 'nachname' in encounter['nscConditions'][nscNumber]:
        if token in encounter['nscConditions'][nscNumber]['nachname']:
            tokenField = encounter['nscConditions'][nscNumber]['nachname'].split(
                '.')
            seed = GetRandomVorname() + '_' + \
                chars[tokenField[0]][tokenField[1]]
            encounter['nscConditions'][nscNumber]['nachname'] = chars[tokenField[0]][tokenField[1]]
        else:
            seed = GetRandomVorname() + '_' + \
                encounter['nscConditions'][nscNumber]['nachname']
    return seed


def BuildEncounter(encounter, gelaende, language):
    result = Header(encounter['name'], '', language, 1)

    if gelaende == 'stadt':
        imgURL = random.choice([
            ('https://cdn.pixabay.com/photo/2016/10/28/13/09/usa-1777986_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2015/07/27/22/55/alley-863687_960_720.jpg', 240, 360),
            ('https://cdn.pixabay.com/photo/2017/08/10/01/30/alley-2616862_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2013/05/21/14/06/paris-112438_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2020/03/09/08/12/rose-4914938_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2019/11/24/05/08/urban-4648574_960_720.jpg', 360, 200),
            ('https://cdn.pixabay.com/photo/2019/11/08/20/23/industry-4612432_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2015/03/26/09/39/building-690043_960_720.jpg', 340, 500),
            ('https://cdn.pixabay.com/photo/2014/07/31/22/22/brickwork-407020_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2019/12/25/18/31/plant-4719061_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2013/12/07/01/47/new-york-224392_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2015/12/31/09/32/building-1115401_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2017/07/22/18/39/factory-2529579_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2014/03/24/21/59/factory-295815_960_720.jpg', 360, 270),
        ])
    elif gelaende == 'wildnis':
        imgURL = random.choice([
            ('https://cdn.pixabay.com/photo/2016/03/09/11/45/forest-1246219_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2016/03/09/15/17/forest-1246572_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2016/08/07/16/15/forest-1576524_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2016/11/01/21/21/landscape-1789703_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2017/05/10/15/05/yosemite-2301047_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2019/12/12/05/30/river-4689820_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2014/04/05/11/21/sunlight-315420_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2019/04/05/09/31/yosemite-national-park-4104634_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2019/10/10/18/42/lake-4540262_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2015/07/13/14/37/woods-843215_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2014/03/17/14/38/jungle-289137_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2019/08/11/16/30/forest-4399318_960_720.jpg', 360, 240),
        ])
    else:
        imgURL = random.choice([
            ('https://cdn.pixabay.com/photo/2016/04/25/18/44/fractal-1352598_960_720.jpg', 270, 360),
            ('https://cdn.pixabay.com/photo/2019/06/07/04/45/space-4257486_960_720.jpg', 360, 360),
            ('https://cdn.pixabay.com/photo/2016/09/29/13/08/planet-1702788_960_720.jpg', 360, 220),
            ('https://cdn.pixabay.com/photo/2017/08/06/12/21/web-2592005_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2018/10/06/19/14/abstract-3728498_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2015/10/10/02/14/spider-web-980272_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2015/07/09/19/43/playground-838308_960_720.jpg', 360, 270),
            ('https://cdn.pixabay.com/photo/2016/03/26/05/17/fractal-1280081_960_720.jpg', 360, 260),
            ('https://cdn.pixabay.com/photo/2016/03/26/05/17/fractal-1280080_960_720.jpg', 360, 360),
            ('https://cdn.pixabay.com/photo/2017/09/05/15/23/city-2718016_960_720.jpg', 360, 190),
            ('https://cdn.pixabay.com/photo/2017/06/14/11/15/meadow-2401893_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2016/01/29/15/26/abstract-1168134_960_720.jpg', 360, 240),
            ('https://cdn.pixabay.com/photo/2013/12/06/00/16/spider-223982_960_720.jpg', 360, 240),
        ])

    encounterText = f'''
    <p style="min-height:{imgURL[2]}px;">
    <img src="{imgURL[0]}"  width="{imgURL[1]}" height="{imgURL[2]}" title="Royality Free Image, Source: Pixabay.com" style="filter: grayscale(75%);float: left; margin: 10px">
    {encounter["text"]}
    </p>'''
    for token in tokens:
        #print(f'handling {token}')
        if token == 'CHAR':
            chars = {}
            while token in encounterText:
                tokenStart = encounterText.find(token)
                nscNumber = int(encounterText[tokenStart + len(token):encounterText.find(')', tokenStart)])
                if encounter['nscConditions'][nscNumber]['art'] in ['Human', 'Kinfolk', 'Garou', 'Ragabash', 'Theurge', 'Philodox', 'Galliard', 'Ahroun', 'vampir']:
                    #result += f'TRYING: {HandleSeed(encounter,nscNumber,chars,token)}'
                    nsc = BuildNSC(
                        seed=HandleSeed(encounter, nscNumber, chars, token),
                        language=language,
                        Art=encounter['nscConditions'][nscNumber]['art'],
                        Stamm='' if 'stamm' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['stamm'],
                        Powerlevel=0 if 'Powerlevel' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['Powerlevel'],
                        packname='' if 'packname' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['packname'],
                        occupation='' if 'occupation' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['occupation'],
                        brut='' if 'brut' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['brut']
                    )
                    counter = 0
                    while not CheckNSCwithConditions(nsc, encounter['nscConditions'][nscNumber], chars):
                        counter += 1
                        #print(f'Encounter "{encounter["name"]}" CHAR{nscNumber} retrying ({nsc["vorname"]+" "+nsc["nachname"]} was unfitting): {counter} to fit Condition: {list(encounter["nscConditions"][nscNumber].items())}')
                        nsc = BuildNSC(
                            seed=HandleSeed(encounter, nscNumber, chars, token, counter),
                            Art=encounter['nscConditions'][nscNumber]['art'],
                            language=language,
                            Stamm='' if 'stamm' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['stamm'],
                            Powerlevel=0 if 'Powerlevel' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['Powerlevel'],
                            packname='' if 'packname' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['packname'],
                            occupation='' if 'occupation' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['occupation'],
                            brut='' if 'brut' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['brut']
                        )
                    #print( f'YAY: {nsc["vorname"]} {nsc["nachname"]} erfüllt alle Bedingungen für {token}{nscNumber}')
                    chars[f'{token}{nscNumber}'] = nsc
                    encounterText = encounterText.replace(
                        f'({token}{nscNumber})', f'({nsc["link"]})')
                    pass
                elif encounter['nscConditions'][nscNumber]['art'] == 'Plagengeist':
                    bane = MakeBane(
                        seed=-1 if 'adjectiv' not in encounter['nscConditions'][nscNumber] else random.choice(
                            encounter['nscConditions'][nscNumber]['adjectiv']) + '_' + random.choice(encounter['nscConditions'][nscNumber]['baneType']),
                        powerlevel=0 if 'Powerlevel' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['Powerlevel']
                    )
                    chars[f'{token}{nscNumber}'] = bane
                    encounterText = encounterText.replace(
                        f'({token}{nscNumber})', f'({bane["link"]})')
                    pass
                elif encounter['nscConditions'][nscNumber]['art'] == 'bsd':
                    nsc = BuildBSD(
                        seed=HandleSeed(encounter, nscNumber, chars, token),
                        language=language,
                        Powerlevel=0 if 'Powerlevel' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['Powerlevel'],
                        packname='' if 'packname' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['packname'],
                    )
                    counter = 0
                    while not CheckNSCwithConditions(nsc, encounter['nscConditions'][nscNumber], chars):
                        counter += 1
                        # print(f'Encounter "{encounter["name"]}" CHAR{nscNumber} retrying: {counter}')
                        nsc = BuildNSC(
                            seed=HandleSeed(encounter, nscNumber, chars, token),
                            language=language,
                            Powerlevel=0 if 'Powerlevel' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['Powerlevel'],
                            packname='' if 'packname' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['packname'],
                        )
                    # print(f'YAY: {nsc["vorname"]} {nsc["nachname"]} erfüllt alle Bedingungen für {token}{nscNumber}')
                    chars[f'{token}{nscNumber}'] = nsc
                    encounterText = encounterText.replace(f'({token}{nscNumber})', f'({nsc["link"]})')
                    pass
                elif encounter['nscConditions'][nscNumber]['art'] == 'garouPack':
                    pack = BuildGarouPack(
                        seed=- 1 if 'seed' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['seed'],
                        limitTribes=[] if 'limitTribes' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['limitTribes'],
                        limitBreeds=[] if 'limitBreeds' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['limitBreeds'],
                        minMembers=3 if 'minMembers' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['minMembers'],
                        maxMembers=6 if 'maxMembers' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['maxMembers'],
                    )
                    chars[f'{token}{nscNumber}'] = pack
                    encounterText = encounterText.replace(f'({token}{nscNumber})', f'({pack["link"]})')
                    pass
                elif encounter['nscConditions'][nscNumber]['art'] == 'bsdPack':
                    pack = BuildBSDPack(
                        seed=- 1 if 'seed' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['seed'],
                        limitBreeds=[] if 'limitBreeds' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['limitBreeds'],
                        minMembers=3 if 'minMembers' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['minMembers'],
                        maxMembers=6 if 'maxMembers' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['maxMembers'],
                    )
                    chars[f'{token}{nscNumber}'] = pack
                    encounterText = encounterText.replace(f'({token}{nscNumber})', f'({pack["link"]})')
                    pass
                else:
                    pass
            pass
        elif token == 'NEWLINE':
            encounterText = encounterText.replace('NEWLINE ', f'{Newline(language)}').replace('NEWLINE', f'{Newline(language)}')
    result += encounterText
    return result


def CreateEncounter(gelände='stadt', language='LATEX', encounterName=''):
    if encounterName != '':
        if encounterName in [enc['name'] for enc in stadtEncounter]:
            return BuildEncounter(encounter=next(enc for enc in stadtEncounter if enc['name'] == encounterName), gelaende=gelände, language=language)
        elif encounterName in [enc['name'] for enc in wildnisEncounter]:
            return BuildEncounter(encounter=next(enc for enc in wildnisEncounter if enc['name'] == encounterName), gelaende=gelände, language=language)
        elif encounterName in [enc['name'] for enc in umbraEncounter]:
            return BuildEncounter(encounter=next(enc for enc in umbraEncounter if enc['name'] == encounterName), gelaende=gelände, language=language)
        else:
            return 'Encounter nicht gefunden'

    if gelände == 'stadt':
        encounter = random.choice(stadtEncounter)
    elif gelände == 'wildnis':
        encounter = random.choice(wildnisEncounter)
    elif gelände == 'umbra':
        encounter = random.choice(umbraEncounter)
    else:
        return 'invalid gelände'
    return BuildEncounter(encounter=encounter, gelaende=gelände, language=language)


def TestAll():
    print(f'STARTING TEST')
    for e in stadtEncounter + wildnisEncounter + umbraEncounter:
        print(f'{e["name"]}')
        # print(BuildEncounter(e,'Plain'))
        BuildEncounter(e, '', 'Plain')
        pass
    print(f'DONE')
