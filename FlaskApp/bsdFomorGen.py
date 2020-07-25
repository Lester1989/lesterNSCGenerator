# -*- coding: utf-8 -*-

import random
from .NSCGenUtils import DrawWithWeights,DrawWithWeightsUnique


# =================================================================
# BSD CHOICES
# =================================================================
Entstellung = {
    'Anzahl':{
        0:4,
        1:6,
        2:2,
        3:1,
    },
    'Art':{
        'ist ein Albino':1,
        'hat Anfälle':1,
        'hat einen Buckel':1,
        'ist Haarlos':1,
        'hat Hörner':1,
        'hat eine Verwachsene Nase':1,
        'hat keinen Schwanz':1,
        'hat einen missgebildeten Arm':.5,
        'hat ein missgebildetes Bein':.5,
        'ist am Husten/Keuchen':1,
        'wirkt Wahnsinnig':1,
        'hat ledrige Haut':1,
    }
}
Mutation = {
    'Anzahl': {
        0:1,
        1:2,
        2:6,
        3:2,
        4:1,
        5:.3,
    },
    'Art': {
        'Tierisch':1,
        'Verderbnis':1,
        'Verzerrung':1,
    },
    'Merkmal': {
        'Die Haut':1,
        'Der Schädel':1,
        'Das Maul':1,
        'Das eine Ohr':1,
        'Eine Hand':1,
        'Ein Arm':1,
        'Ein Bein':1,
        'Die Haare':1,
        'Die Augen':1,
        'Die Nase':1
    },
    'Tierisch':{
        'einem Affe':1,
        'einem Bär':1,
        'einem Elefant':1,
        'einem Fisch':1,
        'einer Katze':1,
        'einem Elch':1,
        'einem Lama':1,
        'einer Ziege':1,
        'einem Insekt':1,
        'einer Ratte':1,
        'einem Frosch':1,
        'einem Krokodil':1,
        'einer Schlange':1,
        'einem Schwein':1,
        'einem Vogel':1,
        'einer Fledermaus':1,
        'einem Pferd':1,
        'einem Nashorn':1,
        'einer Schnecke':1,
    },
    'Verderbnis':{
        'schleimig':1,
        'blass':1,
        'grünlich':1,
        'gelblich':1,
        'fahl':1,
        'blasig':1,
    },
    'Verzerrung':{
        'zu größ':1,
        'zu klein':1,
        'unformig':1,
        'aufgebläht':1,
    }
}
Geistesstörung = {
    'Grad':{
        'kaum wahrnehmbare':3,
        'leichte':7,
        'stets präsente':3,
        'offensichtliche':2,
        'gravierende':1
    },
    'Art':{
        'n Filmrissen':1,
        'r Hysterie':1,
        'r Persönlichkeitsspaltung':1,
        'n Obsessionen':1,
        'r Paranoia':1,
        'r Schizophrenie':1,
    }
}
Abstammung = {
    'geborener Tänzer der Schwarzen Spirale':8,
    'urprünglich von den Fianna':1,
    'urprünglich von den Glaswandler':1,
    'urprünglich von den Kinder Gaias':1,
    'urprünglich von den Knochenbeißer':1,
    'urprünglich von den Nachfahren des Fenris':1,
    'urprünglich von den Rote Klauen':2,
    'urprünglich von den Schattenlords':1,
    'urprünglich von den Schwarze Furien':1,
    'urprünglich von den Silberfängen':1,
    'urprünglich von den Sternenträumer':1,
    'urprünglich von den Wanderer':1,
    'urprünglich von den Uktena':1,
    'urprünglich von den Wendigo':2,
}
Gaben = {}


def MakeBSD(seed):
    random.seed(seed)
    bsd = {
        'Abstammung':DrawWithWeights(Abstammung),
        'Geistesstörung':{'Grad':DrawWithWeights(Geistesstörung['Grad']),'Art':DrawWithWeights(Geistesstörung['Art'])},
        'Entstellungen':[],
        'Mutationen':{},
    }
    nrEntstellungen = DrawWithWeights(Entstellung['Anzahl'])
    for _ in range(nrEntstellungen):
        bsd['Entstellungen'].append(DrawWithWeightsUnique(Entstellung['Art'],bsd['Entstellungen']))
    nrMutationen = DrawWithWeights(Mutation['Anzahl'])
    for _ in range(nrMutationen):
        art = DrawWithWeights(Mutation['Art'])
        bsd['Mutationen'][DrawWithWeightsUnique(Mutation['Merkmal'],list(bsd['Mutationen'].keys()))] = [art,DrawWithWeights(Mutation[art])]
    return bsd


# =================================================================
# FOMORI CHOICES
# =================================================================

Ausprägung = {}
PrägendeSünde = {
    'Götzenanbetung':1,
    'Auflehnung gegen die Eltern':1,
    'Töten':1,
    'Meineid':1,
    'Völlerei':1,
    'Vernachlässigung der Verwandten':1,
    'Wolllust':1,
    'Gier':1,
    'Veruntreuung':1,
    'Lügen':1,
    'Hochmut':1,
    'Arroganz':1,
    'Rauschmittel (Alkoholische Getränke und Drogen)':1,
    'Diebstahl und Raub':1,
    'Ungerechtes Verhalten':1,
    'Erpressung':1,
    'Korruption':1,
    'Unreinheit':1,
    'Angeberei':1,
    'Vernichten von Wissen':1,
    'Verrat':1,
    'Vorhaltungen machen':1,
    'Das gegenseitige Bespitzeln und Ausspionieren':1,
    'Verbreiten von Gerede, Klatsch, Tratsch und Gerüchten':1,
    'Betrug':1,
    'Überheblichkeit und Respektlosigkeit':1,
    'Übertriebene emotionale Ausbrüche':1,
    'Unterdrückung der Schwachen':1,
    'Belästigung':1,
    'Vortäuschen':1,
    'Habgier':1,
    'Neid':1,
    'Heuchelei':1,
    'Verachtung':1,
    'Geiz':1,
    'Trägheit':1,
    'Eitelkeit':1,
    'Übermut':1,
    'Zorn':1,
    'Wut':1,
    'Rachsucht':1,
    'Stolz':1,
    'Maßlosigkeit':1,
    'Selbstsucht':1,
    'Eifersucht':1,
    'Missgunst':1,
    'Faulheit':1,
    'Feigheit':1,
    'Ignoranz':1,
    'Überdruss':1,
}

def MakeFomor(seed):
    random.seed(seed)
    fomor = {
        'Mutationen':{},
        'Sünde':DrawWithWeights(PrägendeSünde)
    }
    nrMutationen = max(0,DrawWithWeights(Mutation['Anzahl'])-1)
    for _ in range(nrMutationen):
        art = DrawWithWeights(Mutation['Art'])
        fomor['Mutationen'][DrawWithWeightsUnique(Mutation['Merkmal'],list(fomor['Mutationen'].keys()))] = [art,DrawWithWeights(Mutation[art])]
    return fomor




