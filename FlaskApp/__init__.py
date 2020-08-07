
# A very simple Flask Hello World app for you to get started with...
# -*- coding: iso-8859-1 -*-
from flask import Flask, request, render_template
from webargs import fields
from webargs.flaskparser import use_args
from datetime import datetime


from .kinfolkGen import PrintBSDPack, PrintPack, CreateRandom, CreateBSD, CreateFomor,BuildNSC,BuildBSD,BuildFomor,stämme,vorzeichen,bruten
from .Formatting import StartCapital
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





app = Flask(__name__)
app.config["DEBUG"] = True


with open(basePath+'/jsons/hintergruende.json', 'r', encoding='utf-8') as infile:
    hintergründe = json.load(infile)
with open(basePath+'/jsons/namedMotivation.json', 'r', encoding='utf-8') as infile:
    namedMotivation = json.load(infile)
with open(basePath+'/jsons/motivation.json', 'r', encoding='utf-8') as infile:
    motivation = json.load(infile)
with open(basePath+'/jsons/plaene.json', 'r', encoding='utf-8') as infile:
    pläne = json.load(infile)
with open(basePath+'/jsons/richtlinien.json', 'r', encoding='utf-8') as infile:
    richtlinien = json.load(infile)
with open(basePath+'/jsons/einstellung.json', 'r', encoding='utf-8') as infile:
    einstellung = json.load(infile)
with open(basePath+'/jsons/wissen.json', 'r', encoding='utf-8') as infile:
    wissen = json.load(infile)
with open(basePath+'/jsons/ausbildung.json', 'r', encoding='utf-8') as infile:
    ausbildung = json.load(infile)
with open(basePath+'/jsons/factor.json', 'r', encoding='utf-8') as infile:
    factor = json.load(infile)
with open(basePath+'/jsons/skills.json', 'r', encoding='utf-8') as infile:
    skills = json.load(infile)
with open(basePath+'/jsons/poolMaxes.json', 'r', encoding='utf-8') as infile:
    poolMaxes = json.load(infile)
# with open(basePath+'/jsons/staemme.json', 'r', encoding='utf-8') as infile:
#     stämme = json.load(infile)
# with open(basePath+'/jsons/vorzeichen.json', 'r', encoding='utf-8') as infile:
#     vorzeichen = json.load(infile)
# with open(basePath+'/jsons/bruten.json', 'r', encoding='utf-8') as infile:
#     bruten = json.load(infile)
with open(basePath+'/jsons/Raenge.json', 'r', encoding='utf-8') as infile:
    Ränge = json.load(infile)
with open(basePath+'/jsons/beziehungen.json', 'r', encoding='utf-8') as infile:
    beziehungen = json.load(infile)
with open(basePath+'/jsons/berufe.json', 'r', encoding='utf-8') as infile:
    berufe = json.load(infile)

@app.route('/test/')
def showClean():

    return render_template("probabilityForm.html",
        staemme=stämme,
        hintergruende=hintergründe,
        namedMotivation=namedMotivation,
        motivation=motivation,
        plaene=pläne,
        richtlinien=richtlinien,
        einstellung=einstellung,
        wissen=wissen,
        ausbildung=ausbildung,
        factor=factor,
        skills=skills,
        poolMaxes=poolMaxes,
        vorzeichen=vorzeichen,
        bruten=bruten,
        raenge=Ränge,
        beziehungen=beziehungen,
        berufe=berufe)



@app.route('/handle_data/', methods=['POST'])
def handle_data():
    print('BLA')
    print(list(request.form.items()))
    for stamm in stämme:
        if stamm in request.form:
            stämme[stamm] = int(request.form[stamm])
    for brut in bruten:
        if stamm in request.form:
            bruten[brut] = int(request.form[brut])
    for auspice in vorzeichen:
        if auspice in request.form:
            vorzeichen[auspice] = int(request.form[auspice])
    return render_template('nscView.html',nsc=BuildNSC(seed=-1, Art='Garou', Powerlevel=0, language='HTML' ))


@app.route('/nsc/bsdpack/')
@use_args({'packname': fields.Str(required=False)}, location="query")
def createBSDPackLinks(args):
    if 'packname' in args:
        return render_template('main.html',content =PrintBSDPack(args['packname']),link = 'bsdpack')
    else:
        return render_template('main.html',content =PrintBSDPack(),link = 'bsdpack')


@app.route('/nsc/garoupack/')
@use_args({'packname': fields.Str(required=False)}, location="query")
def createGarouPackLinks(args):
    if 'packname' in args:
        return render_template('main.html',content =PrintPack(args['packname']),link = 'garoupack')
    else:
        return render_template('main.html',content =PrintPack(),link = 'garoupack')


@app.route('/nsc/<art>/<powerlevel>/<language>/')
@use_args({'packname': fields.Str(required=False), 'treeSeed': fields.Str(required=False)}, location="query")
def HandleNSCCalls(args, art, powerlevel, language):
    if art in ['kinfolk', 'garou', 'human']:
        return render_template('nscView.html',nsc=BuildNSC(seed=-1, Art=StartCapital(art), Powerlevel=int(powerlevel), language=language.upper(), packname=args,))
        #return MakePage(CreateRandom(seed=-1, Art=StartCapital(art), Powerlevel=int(powerlevel), language=language.upper(), packname=args, shortPrint=False), f'/nsc/{art}/')
    elif art in ['vampir']:
        return render_template('nscView.html',nsc=BuildNSC(seed=-1, Art=art, Powerlevel=int(powerlevel), language=language.upper(), packname=args,))
        #return MakePage(CreateRandom(-1, Art=art, Powerlevel=int(powerlevel), language=language.upper(), packname=args, shortPrint=False), f'/nsc/{art}/')
    elif art == 'bsd':
        return render_template('nscView.html',nsc=BuildBSD(seed=-1, Powerlevel=int(powerlevel), language=language.upper(), packname=args,))
        #return MakePage(str(CreateBSD(-1, Powerlevel=int(powerlevel), language=language.upper(), packname=args)), f'/nsc/{art}/')
    elif art == 'bane':
        return render_template('main.html',content =CreateBane(-1, Powerlevel=int(powerlevel), language=language.upper()),link = 'bane')
    elif art == 'fomor':
        return render_template('nscView.html',nsc=BuildFomor(seed=-1, Powerlevel=int(powerlevel), language=language.upper()))
        #return MakePage(str(CreateFomor(-1, Powerlevel=int(powerlevel), language=language.upper())), f'/nsc/{art}/')
    return 'TODO'


@app.route('/nsc/<art>/<powerlevel>/<language>/<seed>/')
@use_args({'packname': fields.Str(required=False), 'treeSeed': fields.Str(required=False)}, location="query")
def HandleNSCCallsWithSeed(args, art, powerlevel, language, seed):
    print(f'seed: {seed}')
    if art in ['kinfolk', 'garou', 'human']:
        return render_template('nscView.html',nsc=BuildNSC(seed=seed, Art=StartCapital(art), Powerlevel=int(powerlevel), language=language.upper(), packname=args,))
        #return MakePage(CreateRandom(seed=seed, Art=StartCapital(art), Powerlevel=int(powerlevel), language=language.upper(), packname=args, shortPrint=False), f'/nsc/{art}/')
    elif art in ['vampir']:
        return render_template('nscView.html',nsc=BuildNSC(seed=seed, Art=art, Powerlevel=int(powerlevel), language=language.upper(), packname=args,))
        #return MakePage(CreateRandom(seed, Art=art, Powerlevel=int(powerlevel), language=language.upper(), packname=args, shortPrint=False), f'/nsc/{art}/')
    elif art == 'bsd':
        return render_template('nscView.html',nsc=BuildBSD(seed=seed, Powerlevel=int(powerlevel), language=language.upper(), packname=args,))
        #return MakePage(str(CreateBSD(seed, Powerlevel=int(powerlevel), language=language.upper(), packname=args)), f'/nsc/{art}/')
    elif art == 'bane':
        return render_template('main.html',content =CreateBane(seed, Powerlevel=int(powerlevel), language=language.upper()),link = 'bane')
    elif art == 'fomor':
        return render_template('nscView.html',nsc=BuildFomor(seed=seed, Powerlevel=int(powerlevel), language=language.upper()))
        #return MakePage(str(CreateFomor(seed, Powerlevel=int(powerlevel), language=language.upper())), f'/nsc/{art}/')
    return 'TODO'


@app.route('/encounter/<gelaende>/<language>/')
def HandleEncounterCalls(gelaende, language):
    return render_template('encounterView.html',data = [gelaende,CreateEncounter(gelaende, language=language.upper())])


@app.route('/encounter/<gelaende>/<language>/<encounterName>')
def HandleNamedEncounterCalls(gelaende, language, encounterName):
    return render_template('encounterView.html',data = [gelaende,CreateEncounter(gelaende, language=language.upper(), encounterName=encounterName)])


@app.route('/feedback/')
@use_args({'bla': fields.Str(required=False)}, location="query")
def myview(args):
    count = len(open(basePath+'/feedBacks.csv', 'r', encoding='utf-8').readlines())
    return render_template('feedbackForm.html',count = count)


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
    return render_template('feedbackResponse.html',count = count)


 
@app.route('/Readfeedback/')
def readFeedbackAnonymous():
    LoginForm = '''    
    <form method="POST">
        <input type="text" name="pwLogin"/>
        <input type="submit"/>
    </form>
    '''
    return render_template('main.html',content =LoginForm,link = '')
    
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
    return render_template('main.html',content =response,link = '')


@app.route('/')
@app.route('/html')
@app.route('/latex')
def showpossibilites():
    return render_template('main.html',content ='',link = '')


if __name__ == '__main__':
    app.run()
