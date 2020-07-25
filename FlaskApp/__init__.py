
# A very simple Flask Hello World app for you to get started with...
# -*- coding: iso-8859-1 -*-

from flask import Flask
from webargs import fields
from webargs.flaskparser import use_args
from .kinfolkGen import *
from .baneGen import *
from .EncounterGen import *
from .gaben import *
from .EncounterGen import *
from .LookGen import *
from .PackNameGen import *
from .SpielHinweise import *
from .bsdFomorGen import *



headerPart ='''
<!DOCTYPE html>
<html>
<head>
<style>
body {
    background-color: whitesmoke;
    font-family:"Garamond";
    font-weight:500;
    padding: 15px;
    text-align: justify;
}
h1   {
    font-family:"Balthazar";
    font-size: 48px;
    text-shadow: 2px 2px 2px #AAAAAA;
    text-align:center;
}
h2   { font-family:"Balthazar";font-size: 36px;}
h3   { font-family:"Garamond"; color: darkred;font-variant: small-caps;border-top: 2px solid darkred;}
h4   { font-family:"Garamond"; color: darkred;font-variant: small-caps;border-top: 2px solid darkred;}
hr   { border: none; background: darkred; height:2px;}
div {border-style: none; padding:5px;}
a {
    font-weight:400;
}
a:hover{
    font-weight:800;
}
.button {
  display: inline-block;
  border-radius: 4px;
  background-color: darkred;
  border: none;
  color: #FFFFFF;
  text-align: center;
  font-size: 28px;
  padding: 20px;
  width: 250px;
  transition: all 0.5s;
  cursor: pointer;
  margin: 5px;
}

.button span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
}

.button span:after {
  content: '  >>';
  position: absolute;
  opacity: 0;
  top: 0;
  right: 0px;
  transition: 0.5s;
}

.button:hover span {
  padding-right: 25px;
}

.button:hover span:after {
  opacity: 1;
  right: 0;
}

.sidenav {
  height: 100%;
  width: 320px;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  background-color: whitesmoke;
  border-right: solid 4px darkred;
  overflow-x: hidden;
  padding-top: 00px;
}
.sidenav a {
  display: block;
  color: black;
  padding: 10px;
  text-decoration: none;
}

.sidenav a.active {
  background-color: darkred;
  color: white;
  font-weight:500;
}

.sidenav a:hover:not(.active) {
  background-color: #555;
  color: white;
  font-weight:400;
}
.sidenav a.mailTo {
  display: inline;
  color: black;
  padding: 0px;
  text-decoration: none;
}

div.content {
  margin-left: 320px;
  padding: 1px 16px;
}

@media screen and (max-width: 700px) {
  .sidenav {
    width: 100%;
    height: auto;
    position: relative;
    border-right: none;
    border-bottom: solid 4px darkred;
  }
  .sidenav a {float: left;}
  div.content {margin-left: 0;}

  .sidenav h4 {display:none;}
  .sidenav hr {display:none;}
  .sidenav p {display:none;}
  .sidenav img {display:none;}
}

@media screen and (max-width: 400px) {
  .sidenav {
    border-right: none;
    border-bottom: solid 4px darkred;
  }
  .sidenav a {
    text-align: center;
    float: none;
  }
  .sidenav h4 {display:none;}
  .sidenav hr {display:none;}
  .sidenav p {display:none;}
  .sidenav img {display:none;}
}
@media print
{

    body {margin: 0mm;}

    div.content {
        margin: 0;
    }

    body {
        background-color: white;
    }

    .no-print, .no-print *
    {
        display: none !important;
    }
}
</style>
</head>
'''

baseURL = 'http://v22018117165076045.happysrv.de'

def MakePage(content,url=''):
    linkActivity = {
        'kinfolk':' class="active" ' if '/kinfolk/' in url.lower() else '',
        'garou':' class="active" ' if '/garou/' in url.lower() else '',
        'human':' class="active" ' if '/human/' in url.lower() else '',
        'bsd':' class="active" ' if '/bsd/' in url.lower() else '',
        'fomor':' class="active" ' if '/fomor/' in url.lower() else '',
        'bsdpack':' class="active" ' if '/bsdpack/' in url.lower() else '',
        'garoupack':' class="active" ' if '/garoupack/' in url.lower() else '',
        'bane':' class="active" ' if '/bane/' in url.lower() else '',
        'stadt':' class="active" ' if '/stadt/' in url.lower() else '',
        'wildnis':' class="active" ' if '/wildnis/' in url.lower() else '',
        'umbra':' class="active" ' if '/umbra/' in url.lower() else '',
        }
    encounterDisclaimer ='''
    <div class="no-print">
        Die erzeugten Zufallsbegegnungen sollen vor allem Inspiration sein, um die Welt für die Spieler belebter zu machen.
        Im Idealfall sind die Begegnungen jedoch auch relevant für den Plot, oder eröffnen Möglichkeiten um im Plot weiterzukommen oder die Charaktere zu entwickeln.
    </div>''' if 'encounter' in url else ''

    menuPart =f'''
    <div class="no-print sidenav">
        <h1 >Lesters NSC Generator</h1>
        <h4 >NSC</h4>
        <div>
            <a {linkActivity["kinfolk"]} href="{baseURL}/nsc/kinfolk/0/html"> Kinfolk </a>
            <a {linkActivity["garou"]} href="{baseURL}/nsc/garou/0/html"> Garou </a>
            <a {linkActivity["human"]} href="{baseURL}/nsc/Human/0/html"> Mensch </a>
            <a {linkActivity["bsd"]} href="{baseURL}/nsc/bsd/0/html"> Tänzer der schwarzen Spirale </a>
            <a {linkActivity["fomor"]} href="{baseURL}/nsc/fomor/0/html"> Fomor </a>
            <a {linkActivity["bsdpack"]} href="{baseURL}/nsc/bsdpack/"> Rudel Tänzer der schwarzen Spirale </a>
            <a {linkActivity["garoupack"]} href="{baseURL}/nsc/garoupack/"> Rudel Garou Nation </a>
            <a {linkActivity["bane"]} href="{baseURL}/nsc/bane/0/html/">  Plagengeist </a>
        </div>
        <h4 >zufällige Encounter</h4>
        <div >
            <a {linkActivity["stadt"]} href="{baseURL}/encounter/stadt/html/"> in der Stadt </a><br>
            <a {linkActivity["wildnis"]} href="{baseURL}/encounter/wildnis/html/"> in der Wildnis </a><br>
            <a {linkActivity["umbra"]} href="{baseURL}/encounter/umbra/html/"> im Umbra </a><br>
        </div>

        <hr>
        <p>Schicke Feedback oder Wünsche oder Vorschläge an mich <a class="mailTo" href="mailto:l.ester@gmx.de?Subject=[NSC Generator] Feedback" target="_top">&#x1f4e8; (l.ester@gmx.de) &#x1f4e8;</a>(l.ester@gmx.de)</p>
        <img src="https://hitcounter.pythonanywhere.com/count/tag.svg?url=http%3A%2F%2Flester89.pythonanywhere.com%2F" alt="Hits" >
    </div>
    '''


    result = headerPart+menuPart+'<div class="content">'+content+f'''
        <br>
            {encounterDisclaimer}
        <br>
        <button onclick="window.print()" class="button no-print" style="vertical-align:middle"><span>Ausdrucken </span></button>
    </div>
    '''
    return result



app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/nsc/bsdpack/')
@use_args({'packname': fields.Str(required=False)},location="query")
def createBSDPackLinks(args):
    if 'packname' in args:
        return MakePage( kinfolkGen.PrintBSDPack(args['packname']),'/nsc/bsdpack/')
    else:
        return MakePage(kinfolkGen.PrintBSDPack(),'/nsc/bsdpack/')


@app.route('/nsc/garoupack/')
@use_args({'packname': fields.Str(required=False)},location="query")
def createGarouPackLinks(args):
    if 'packname' in args:
        return MakePage(kinfolkGen.PrintPack(args['packname']),'/nsc/garoupack/')
    else:
        return MakePage(kinfolkGen.PrintPack(),'/nsc/garoupack/')

@app.route('/nsc/<art>/<powerlevel>/<language>/')
@use_args({'packname': fields.Str(required=False)},location="query")
def HandleNSCCalls(args,art,powerlevel,language):
    if art in ['kinfolk','garou','Human']:
        return MakePage(kinfolkGen.CreateRandom(seed=-1,Art=art[0].upper()+art[1:],Powerlevel=int(powerlevel),language=language.upper(),packname=args,shortPrint=False),f'/nsc/{art}/')
    elif art == 'bsd':
        return MakePage(str(kinfolkGen.CreateBSD(-1,Powerlevel=int(powerlevel),language=language.upper(),packname=args)),f'/nsc/{art}/')
    elif art == 'bane':
        return MakePage(str(baneGen.CreateBane(-1,Powerlevel=int(powerlevel),language=language.upper())),f'/nsc/{art}/')
    elif art == 'fomor':
        return MakePage(str(kinfolkGen.CreateFomor(-1,Powerlevel=int(powerlevel),language=language.upper())),f'/nsc/{art}/')
    return 'TODO'

@app.route('/nsc/<art>/<powerlevel>/<language>/<seed>')
@use_args({'packname': fields.Str(required=False)},location="query")
def HandleNSCCallsWithSeed(args,art,powerlevel,language,seed):
    if art in ['kinfolk','garou','human']:
        return MakePage(kinfolkGen.CreateRandom(seed=seed,Art=art[0].upper()+art[1:],Powerlevel=int(powerlevel),language=language.upper(),packname=args,shortPrint=False),f'/nsc/{art}/')
    elif art == 'bsd':
        return MakePage(str(kinfolkGen.CreateBSD(seed=seed,Powerlevel=int(powerlevel),language=language.upper(),packname=args)),f'/nsc/{art}/')
    elif art == 'bane':
        return MakePage(str(baneGen.CreateBane(seed=seed,Powerlevel=int(powerlevel),language=language.upper())),f'/nsc/{art}/')
    elif art == 'fomor':
        return MakePage(str(kinfolkGen.CreateFomor(seed=seed,Powerlevel=int(powerlevel),language=language.upper())),f'/nsc/{art}/')
    return MakePage(menuPart,f'/nsc/{art}/')




@app.route('/encounter/<gelaende>/<language>/')
def HandleEncounterCalls(gelaende,language):
    return MakePage(EncounterGen.CreateEncounter(gelaende,language=language.upper())+f'''
    <br>
    <br>
    <a class="no-print" href="{baseURL}/encounter/{gelaende}/{language}"> Neu </a><br>
    ''',f'/encounter/{gelaende}/')

@app.route('/encounter/<gelaende>/<language>/<encounterName>')
def HandleNamedEncounterCalls(gelaende,language,encounterName):
    return MakePage(EncounterGen.CreateEncounter(gelaende,language=language.upper(),encounterName=encounterName)+f'''
    <br>
    <br>
    <a class="no-print" href="{baseURL}/encounter/{gelaende}/{language}/{encounterName}"> Neu </a><br>
    ''',f'/encounter/{gelaende}/')


@app.route('/test/')
@use_args({'bla': fields.Str(required=False)},location="query")
def myview(args):
    if 'bla' in args:
        bla = args['bla']
    else:
        bla = f'no arg found:{args}'
    return str(f'''<h1>{bla}</h1>''')

@app.route('/')
@app.route('/html')
@app.route('/latex')
def showpossibilites():
    #TODO provide features
    return MakePage('')


if __name__ == '__main__':
    app.run()

