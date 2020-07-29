
# A very simple Flask Hello World app for you to get started with...
# -*- coding: iso-8859-1 -*-
from flask import Flask, request, render_template
from webargs import fields
from webargs.flaskparser import use_args
from datetime import datetime


from .kinfolkGen import PrintBSDPack, PrintPack, CreateRandom, CreateBSD, CreateFomor
from .baneGen import CreateBane
from .EncounterGen import CreateEncounter
from .gaben import *
from .EncounterGen import *
from .LookGen import *
from .PackNameGen import *
from .SpielHinweise import *
from .bsdFomorGen import *
from .config import baseURL, basePath,feedbackLoginCode
from .htmlCSSStuff import headerPart, feedbackForm, feedbackResponse


def MakePage(content, url='', canPrintPage=True):
    linkActivity = {
        'kinfolk': ' class="active" ' if '/kinfolk/' in url.lower() else '',
        'garou': ' class="active" ' if '/garou/' in url.lower() else '',
        'human': ' class="active" ' if '/human/' in url.lower() else '',
        'vampir': ' class="active" ' if '/vampir/' in url.lower() else '',
        'bsd': ' class="active" ' if '/bsd/' in url.lower() else '',
        'fomor': ' class="active" ' if '/fomor/' in url.lower() else '',
        'bsdpack': ' class="active" ' if '/bsdpack/' in url.lower() else '',
        'garoupack': ' class="active" ' if '/garoupack/' in url.lower() else '',
        'bane': ' class="active" ' if '/bane/' in url.lower() else '',
        'stadt': ' class="active" ' if '/stadt/' in url.lower() else '',
        'wildnis': ' class="active" ' if '/wildnis/' in url.lower() else '',
        'umbra': ' class="active" ' if '/umbra/' in url.lower() else '',
    }
    encounterDisclaimer = '''
    <div class="no-print">
        Die erzeugten Zufallsbegegnungen sollen vor allem Inspiration sein, um die Welt für die Spieler belebter zu machen.
        Im Idealfall sind die Begegnungen jedoch auch relevant für den Plot, oder eröffnen Möglichkeiten um im Plot weiterzukommen oder die Charaktere zu entwickeln.
    </div>''' if 'encounter' in url else ''

    menuPart = f'''
    <div class="no-print sidenav">
        <h1 >Lesters NSC Generator</h1>
        <h4 >NSC</h4>
        <div>
            <a {linkActivity["kinfolk"]} href="{baseURL}/nsc/kinfolk/0/html"> Kinfolk </a>
            <a {linkActivity["garou"]} href="{baseURL}/nsc/garou/0/html"> Garou </a>
            <a {linkActivity["human"]} href="{baseURL}/nsc/Human/0/html"> Mensch </a>
            <a {linkActivity["vampir"]} href="{baseURL}/nsc/vampir/0/html"> Vampir </a>
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
        <p>Schicke Feedback oder Wünsche oder Vorschläge an mich via Mail<a class="mailTo" href="mailto:l.ester@gmx.de?Subject=[NSC Generator] Feedback" target="_top">&#x1f4e8; (l.ester@gmx.de) &#x1f4e8;</a>(l.ester@gmx.de)</p>
        <a href="{baseURL}/feedback/"> Feedback</a>
        <img src="https://hitcounter.pythonanywhere.com/count/tag.svg?url=http%3A%2F%2Flester89.pythonanywhere.com%2F" alt="Hits" >
    </div>
    '''

    result = headerPart+menuPart+'<div class="content">'+content+f'''
        <br>
            {encounterDisclaimer}
        <br>'''
    if canPrintPage:
        result += '''
        <button onclick="window.print()" class="button no-print" style="vertical-align:middle"><span>Ausdrucken </span></button>
        '''
    result += '''
    </div>
    '''
    return result


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/nsc/bsdpack/')
@use_args({'packname': fields.Str(required=False)}, location="query")
def createBSDPackLinks(args):
    if 'packname' in args:
        return MakePage(PrintBSDPack(args['packname']), '/nsc/bsdpack/')
    else:
        return MakePage(PrintBSDPack(), '/nsc/bsdpack/')


@app.route('/nsc/garoupack/')
@use_args({'packname': fields.Str(required=False)}, location="query")
def createGarouPackLinks(args):
    if 'packname' in args:
        return MakePage(PrintPack(args['packname']), '/nsc/garoupack/')
    else:
        return MakePage(PrintPack(), '/nsc/garoupack/')


@app.route('/nsc/<art>/<powerlevel>/<language>/')
@use_args({'packname': fields.Str(required=False), 'treeSeed': fields.Str(required=False)}, location="query")
def HandleNSCCalls(args, art, powerlevel, language):
    if art in ['kinfolk', 'garou', 'Human']:
        return MakePage(CreateRandom(seed=-1, Art=art[0].upper()+art[1:], Powerlevel=int(powerlevel), language=language.upper(), packname=args, shortPrint=False), f'/nsc/{art}/')
    elif art in ['vampir']:
        return MakePage(CreateRandom(-1, Art=art, Powerlevel=int(powerlevel), language=language.upper(), packname=args, shortPrint=False), f'/nsc/{art}/')
    elif art == 'bsd':
        return MakePage(str(CreateBSD(-1, Powerlevel=int(powerlevel), language=language.upper(), packname=args)), f'/nsc/{art}/')
    elif art == 'bane':
        return MakePage(str(CreateBane(-1, Powerlevel=int(powerlevel), language=language.upper())), f'/nsc/{art}/')
    elif art == 'fomor':
        return MakePage(str(CreateFomor(-1, Powerlevel=int(powerlevel), language=language.upper())), f'/nsc/{art}/')
    return 'TODO'


@app.route('/nsc/<art>/<powerlevel>/<language>/<seed>/')
@use_args({'packname': fields.Str(required=False), 'treeSeed': fields.Str(required=False)}, location="query")
def HandleNSCCallsWithSeed(args, art, powerlevel, language, seed):
    print(f'seed: {seed}')
    if art in ['kinfolk', 'garou', 'human']:
        return MakePage(CreateRandom(seed=seed, Art=art[0].upper()+art[1:], Powerlevel=int(powerlevel), language=language.upper(), packname=args, shortPrint=False), f'/nsc/{art}/')
    elif art in ['vampir']:
        return MakePage(CreateRandom(seed=seed, Art=art, Powerlevel=int(powerlevel), language=language.upper(), packname=args, shortPrint=False), f'/nsc/{art}/')
    elif art == 'bsd':
        return MakePage(str(CreateBSD(seed=seed, Powerlevel=int(powerlevel), language=language.upper(), packname=args)), f'/nsc/{art}/')
    elif art == 'bane':
        return MakePage(str(CreateBane(seed=seed, Powerlevel=int(powerlevel), language=language.upper())), f'/nsc/{art}/')
    elif art == 'fomor':
        return MakePage(str(CreateFomor(seed=seed, Powerlevel=int(powerlevel), language=language.upper())), f'/nsc/{art}/')
    return 'TODO'


@app.route('/encounter/<gelaende>/<language>/')
def HandleEncounterCalls(gelaende, language):
    return MakePage(CreateEncounter(gelaende, language=language.upper())+f'''
    <br>
    <br>
    <a class="no-print" href="{baseURL}/encounter/{gelaende}/{language}"> Neu </a><br>
    ''', f'/encounter/{gelaende}/')


@app.route('/encounter/<gelaende>/<language>/<encounterName>')
def HandleNamedEncounterCalls(gelaende, language, encounterName):
    return MakePage(CreateEncounter(gelaende, language=language.upper(), encounterName=encounterName)+f'''
    <br>
    <br>
    <a class="no-print" href="{baseURL}/encounter/{gelaende}/{language}/{encounterName}"> Neu </a><br>
    ''', f'/encounter/{gelaende}/')


@app.route('/feedback/')
@use_args({'bla': fields.Str(required=False)}, location="query")
def myview(args):
    count = len(open(basePath+'/feedBacks.csv', 'r', encoding='utf-8').readlines())
    counterPart = f'''
    <p> Bisher wurde {count} mal Feedback abgegeben</p>
    '''
    return MakePage(feedbackForm + counterPart, '', False)


@app.route('/feedback/', methods=['POST'])
def my_form_post():
    submitter = request.form['Submitter']
    feedback = request.form['Feedback']
    contact = request.form['Contact']
    print(repr(feedback))
    if len(feedback) > 0:
        with open(basePath+'/feedBacks.csv', 'a', encoding='utf-8') as saveFile:
            saveFile.write(f'{datetime.now().strftime("%H:%M:%S")}";"{submitter}";"{contact}";"{repr(feedback)}')

    count = len(open(basePath+'/feedBacks.csv', 'r', encoding='utf-8').readlines())
    counterPart = f'''
    <p> Bisher wurde {count} mal Feedback abgegeben</p>
    '''
    return MakePage(feedbackResponse + counterPart, '', False)


 
@app.route('/Readfeedback/')
def readFeedbackAnonymous():
    LoginForm = '''    
    <form method="POST">
        <input type="text" name="pwLogin"/>
        <input type="submit"/>
    </form>
    '''
    return MakePage(LoginForm,'', False)
    
@app.route('/Readfeedback/',methods=['POST'])
def readFeedbackLogin():
    response = ''
    login = request.form['pwLogin']
    if login == feedbackLoginCode:
        with open(basePath+'/feedBacks.csv', 'r', encoding='utf-8') as fbFile:
            Lines = fbFile.readlines()
            for line in Lines:
                fields = line.split('";"')
                if len(fields)!=4:
                    print(line)
                    continue
                response += f'''
<hr>
<p>{fields[0]} - Von {fields[1]}</p>
<p>{fields[3]}</p>
<p>Antwort an: {fields[2]}</p>
<br>
'''
    else:
        response = 'under Construction'
    return MakePage(response,'', False)


@app.route('/')
@app.route('/html')
@app.route('/latex')
def showpossibilites():
    # TODO provide features
    return MakePage('')


if __name__ == '__main__':
    app.run()
