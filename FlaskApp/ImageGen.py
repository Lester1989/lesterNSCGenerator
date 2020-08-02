
from .NSCGenUtils import NameToSeed
import requests
import json
from bs4 import BeautifulSoup
import random

def TextWithImage( imageURL):
    if imageURL == 'https://cdn.pixabay.com/photo/2020/06/05/16/27/excuse-me-5263696_960_720.jpg':
        return f'''
    <figure style="float:left;margin-right: 10px;margin-top:0px;margin-left:0px">
    <img src="{imageURL}"  width="300" height="200" title=" Source: Pixabay.com" style="filter: grayscale(75%); ">
      <figcaption>Leider ist ein Fehler aufgetreten.</figcaption>
    </figure>
    '''

    return f'''
    <figure style="float:left;margin-right: 10px;margin-top:0px;margin-left:0px">
    <img src="{imageURL}"  width="256" height="256" title="AI Generated Image, Source: Generated Photos" style="filter: grayscale(75%); ">
      <figcaption>Photo by <a href="https://generated.photos">Generated Photos</a></figcaption>
    </figure>
    '''


def GetFace(nsc):
    NameToSeed(nsc['vorname']+' '+nsc['nachname'])
    url = "https://api.generated.photos/api/v1/faces?api_key=9431GheN9YeSBMHadx2bow"
    if nsc['alter'] in ['gerade Volljährig', 'zwischen 20 und 30']:
        bildAlter = 'young-adult'
    elif nsc['alter'] in ['anfang 30', 'mitte 30', 'anfang 40', 'mitte 40']:
        bildAlter = 'adult'
    else:
        bildAlter = 'elderly'
    if nsc["scRudel"] in ['Liebevoll', 'Freundlich', 'Offen']:
        bildEmotion = 'joy'
    else:
        bildEmotion = 'neutral'
    if nsc['beschreibungFrisur'] in ['blond','hell']:
        bildHaare = 'blond-hair/'
    elif nsc['beschreibungFrisur'] in ['dunkel','schwarz']:
        bildHaare = 'black-hair/'
    elif nsc['beschreibungFrisur'] in ['grau']:
        bildHaare = 'gray-hair/'
    elif nsc['beschreibungFrisur'] in ['braun']:
        bildHaare = 'brown-hair/'
    elif nsc['beschreibungFrisur'] in ['lang']:
        bildHaare = 'long/'
    else:
        bildHaare = ''
    gender = 'male'if nsc['pronomen'] == 'er' else 'female'
    print(f'getting Image for ({gender}) {nsc["vorname"]+" "+nsc["nachname"]}')
    try:
        url = f'https://generated.photos/faces/{bildAlter}/{bildHaare}{gender}'
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        imgs = []
        for post in soup.findAll('div', {'class': 'card-image'}):
            imgs.append(str(post.find('img')).split('"')[-2])
        return random.choice(imgs)
    except Exception as e:
        print(bildAlter)
        print(bildEmotion)
        print(bildHaare)
        print(gender)
        print(e)
        pass
    return 'https://cdn.pixabay.com/photo/2020/06/05/16/27/excuse-me-5263696_960_720.jpg'