import random
from .kinfolkGen import GetRandomVorname, GetRandomNachname, BuildNSC, BuildBSD, BuildGarouPack, BuildBSDPack
from .baneGen import MakeBane
import time
from .Formatting import Bold, Newline, Header, ListLines, Table

# encounter = {name,text,nscConditions}
# nscCondition = {'sex':m/w,[beschreibungsname:[Möglichkeiten]]}

# tokens:
#  CHAR$ -> $ is index in nscConditions

tokens = ['CHAR', 'NEWLINE']

stadtEncounter = [
    {
        'name': 'Bettler',
        'text': 'Als die SC durch die Straßen gehen, entdecken sie in kurzer Entfernung einen Menschen (CHAR0) in unsauberer Kleidung, dieser hebt den Kopf und schaut in Richtung der SC. Nach einem kurzem Zögern wendet er sich komplett und geht auf die SC zu.NEWLINE'
                ' Er möchte nach etwas Geldfragen, um sich eine Fahrkarte zu seiner Tochter (CHAR1) zu kaufen, welche heute Geburtstag hat.NEWLINE'
                ' Er wird sich vermutlich schnell vertrösten lassen und sich neue Opfer suchen.',
        'nscConditions': [
            {
                'art': 'Human',
                'beschreibungKleidung': ['abgerissene ', 'alte ', 'verschmutzte ', 'verschlissene ', ],
                'NICHTbeschreibungFrisur': ['gefärbt', 'hochgestylt'],
                'NICHTalter': ['gerade Volljährig', 'ende 50', 'über 60']
            },
            {
                'art': 'Human',
                'pronomen': 'sie',
                'nachname': 'CHAR0.nachname'
            }

        ]
    },
    {
        'name': 'Ordnungsamt',
        'text': 'Die Beamten Herr (CHAR0) und Frau (CHAR1) vom Ordnungsamt kontrollieren die SC. Sie tragen dunkelblaue Jacken und Hosen, die Uniform.NEWLINE'
                ' Ist die Gruppe auffällig? Können sich die SC ausweisen? Wird nach ihnen gesucht?NEWLINE'
                ' Flieht die Gruppe: verfolgen die Beamten die SC bis zu 2 Straßenecken, danach ggf. Fahndung.',
        'nscConditions': [
            {
                'art': 'Human',
                'pronomen': 'er',
                'beschreibungKleidung': ['Arbeits-'],
                'beschreibungKleidungsFarbe': ['dunklen']
            },
            {
                'art': 'Human',
                'pronomen': 'sie',
                'beschreibungKleidung': ['Arbeits-'],
                'beschreibungKleidungsFarbe': ['dunklen']
            }
        ]
    },
    {
        'name': 'Ortsfremder Autofahrer',
        'text': 'Ein dunkler Geländewagen ist schon zweimal an den SC vorbeigefahren und kommt gerade das 3. mal an. Diesmal von Hinten. Und er wird langsamer. Er hält neben den SC an und öffnet das Fenster.NEWLINE'
                ' Im Geländewagen sitzt eine verzweifelt schauende Frau (CHAR0), welche ihren Sohn (CHAR1) zu dem Geburtstag von einem Freund (CHAR2) fahren wollte, aber das Navi geht nicht. Deshalb sucht sie schon fast eine Stunde.NEWLINE'
                ' Der Sohn quengelt derweil vor sich hin.',
        'nscConditions': [
            {
                'art': 'Human',
                'pronomen': 'sie',
                'NICHTbeschreibungKleidung': ['abgerissene ', 'alte ', 'verschmutzte ', 'verschlissene '],
            },
            {
                'art': 'Human',
                'pronomen': 'er',
                'nachname': 'CHAR0.nachname',
                'NICHTbeschreibungKleidung': ['abgerissene ', 'alte ', 'verschmutzte ', 'verschlissene '],
            },
            {
                'art': 'Human',
                'pronomen': 'er',
            }
        ]
    },
    {
        'name': 'Schläger',
        'text': 'Das Rudel wird von einer Straßengang eingekreist und überfallen. Dabei sind die SC erst in der Überzahl, merken jedoch erst zu spät, dass sie umzingelt sind.NEWLINE'
                ' Da dies jedoch nur Menschen sind, fliehen sie recht schnell und lassen sich auch schnell einschüchtern. Wenn die SC weniger werhaft aussehen, sind sie etwas mutiger.NEWLINE'
                '(Anzahl der Schläger variieren, hier ein paar Beispiele:)NEWLINE (CHAR0)NEWLINE (CHAR1)NEWLINE (CHAR2)NEWLINE (CHAR3)NEWLINE (CHAR4)NEWLINE (CHAR5)NEWLINE (CHAR6)NEWLINE (CHAR7)NEWLINE (CHAR8)NEWLINE (CHAR9)NEWLINE (CHAR10)',
        'nscConditions': [
            {
                'art': 'Human',
                'alter': ['gerade Volljährig', 'zwischen 20 und 30', 'anfang 30', 'mitte 30'],
                'Powerlevel': 3,
            },
            {
                'art': 'Human',
                'alter': ['gerade Volljährig', 'zwischen 20 und 30', 'anfang 30', 'mitte 30'],
            },
            {
                'art': 'Human',
                'alter': ['gerade Volljährig', 'zwischen 20 und 30', 'anfang 30', 'mitte 30'],
            },
            {
                'art': 'Human',
                'alter': ['gerade Volljährig', 'zwischen 20 und 30', 'anfang 30', 'mitte 30'],
            },
            {
                'art': 'Human',
                'alter': ['gerade Volljährig', 'zwischen 20 und 30', 'anfang 30', 'mitte 30'],
            },
            {
                'art': 'Human',
                'alter': ['gerade Volljährig', 'zwischen 20 und 30', 'anfang 30', 'mitte 30'],
            },
            {
                'art': 'Human',
                'alter': ['gerade Volljährig', 'zwischen 20 und 30', 'anfang 30', 'mitte 30'],
            },
            {
                'art': 'Human',
                'alter': ['gerade Volljährig', 'zwischen 20 und 30', 'anfang 30', 'mitte 30'],
            },
            {
                'art': 'Human',
                'alter': ['gerade Volljährig', 'zwischen 20 und 30', 'anfang 30', 'mitte 30'],
            },
            {
                'art': 'Human',
                'alter': ['gerade Volljährig', 'zwischen 20 und 30', 'anfang 30', 'mitte 30'],
            },
            {
                'art': 'Human',
                'alter': ['gerade Volljährig', 'zwischen 20 und 30', 'anfang 30', 'mitte 30'],
            },
        ]
    },
    {
        'name': 'Betrunkener',
        'text': 'Als die SC gerade an einer Haustür vorbeigeht, fliegt diese auf und ein Mann (CHAR0) stolpert gegen die SC und fällt mit einem SC zu Boden.NEWLINE'
                ' Er lallt nur Unverständliches. Dann richtet er sich auf und kramt in seiner Jackentasche. Er holt ein Schlüsselbund zum Vorschein und wirft dabei eine Schachtel Zigaretten auf den Boden. Ein unverständlicher Fluch und dann bückt der sich um sie aufzuheben. Erst beim zweiten Versuch gelingt es ihm.NEWLINE'
                ' Er lehnt sich an das hier parkende Auto. Dann beginnt er Schlüssel auszuprobieren um das Auto zu öffnen. Er stutzt kurz, sieht sich um und geht dann zum nächsten Auto. Dieses öffnet er und steigt ein.NEWLINE'
                ' Beim Ausparken streift er das andere Auto. Nach einiger Zeit hört man eine Vollbremsung und ein Scheppern.',
        'nscConditions': [
            {
                'art': 'Human',
                'pronomen': 'er',
                'NICHTbeschreibungKleidung': ['abgerissene ', 'alte ', 'verschlissene '],
            },
        ]
    },
    {
        'name': 'Verirrtes Kind',
        'text': 'Ein etwa dreijähriger Junge (CHAR0) steht plötzlich neben den SC und schaut sie erschreckt an. Dann fängt er an zu schluchzen und sieht sich hilfesuchend um.NEWLINE'
                ' Er hat seine Mama (CHAR1) verloren und sucht sie.',
        'nscConditions': [
            {
                'art': 'Human',
                'pronomen': 'er',
                'NICHTbeschreibungKleidung': ['abgerissene ', 'alte ', 'verschlissene '],
            },
            {
                'art': 'Human',
                'pronomen': 'sie',
                'nachname': 'CHAR0.nachname',
                'NICHTbeschreibungKleidung': ['abgerissene ', 'alte ', 'verschlissene '],
            },
        ]
    },
    {
        'name': 'Leiche',
        'text': 'Irgendetwas stimmt nicht. Tod. In einer Seitengasse liegt ein roter Stiefel. Der Absatz ist umgeknickt.NEWLINE'
                '(Hier bietet sich ein Wahrnehmungswurf an.) In einem Altpapiercontainer daneben liegt eine Frauenleiche (CHAR0). Sie hat hervor gequollene Augen und dunkle Lippen. Ihr Tanktop hängt nur noch so gerade eben an ihr und man kann ihren BH sehen. Billig und freizügig.NEWLINE'
                ' Ihr Minirock ist so kurz, dass man erkennt, das ihre Unterwäsche ein Set ist. Während ihr rechtes Bein noch im Stiefel steckt, ist ihr linkes nur noch von einer Netzstrumpfhose bedeckt.NEWLINE'
                ' Sie wurde von ihrem Zuhälter (CHAR1) getötet, da sie einen Freund (CHAR2) gefunden hatte und mit ihm weggehen wollte.',
        'nscConditions': [
            {
                'art': 'Human',
                'pronomen': 'sie',
                'NICHTbeschreibungKleidung': ['Militär-', 'alte ', 'verschlissene '],
            },
            {
                'art': 'Human',
                'pronomen': 'er',
                'NICHTbeschreibungKleidung': ['abgerissene ', 'alte ', 'verschlissene '],
            },
            {
                'art': 'Human',
                'pronomen': 'er',
            },
        ]
    },
    {
        'name': 'Bewusstlose Person',
        'text': 'Als ein SC den Blick zur Seite schweifen lässt, fällt ihr eine Hand auf, welche hinter einem Müllcontainer hervorragt; Ein junger Mann (CHAR0). Wenn das Rudel den jungen Mann untersucht (Medizinprobe) stellt es fest, dass er am Leben ist.NEWLINE'
                ' Er ist blass und an seinem Hemdkragen ist etwas Blut. Es sind jedoch keine Wunden zu entdecken.NEWLINE'
                ' Als er zu sich kommt erzählt er, dass er auf einer Party war und da einen echt heißen Typen kennengelernt hat. Allerdings ist die Party wohl ausgeufert und er hat zu viel getrunken. Er will nach Hause gehen um sich auszuschlafen.NEWLINE '
                ' Er wurde von einem Vampir (CHAR1) gebissen und liegen gelassen. Kann das Rudel die Verfolgung aufnehmen? Kommen sie überhaupt darauf, dass es ein Vampir war?',
        'nscConditions': [
            {
                'art': 'Human',
                'pronomen': 'er',
                'alter': ['gerade Volljährig', 'zwischen 20 und 30'],
            },
            {
                'art':'vampir',
            }
        ]
    },
    {
        'name': 'Vampir auf der Jagd',
        'text': 'Das Rudel kann die Spur von einem Vampir (CHAR0) auf der Jagd aufnehmen.NEWLINE'
                ' Stellen sie ihn zur Rede? Schlagen sie zu, bevor er trinken kann? Versucht er zu fliehen, oder zu verhandeln?NEWLINE'
                ' Trinkt er von einem Ghul (CHAR1), der sein Blut freiwillig gibt?NEWLINE'
                ' Vielleicht gibt er den SC auch noch Informationen zu den Geschehnissen in der Stadt.',
        'nscConditions': [
            {
                'art':'vampir',
            },
            {
                'art': 'Human',
            },
        ]
    },
    {
        'name': 'Gassi Geher',
        'text': 'Den SC kommt eine Frau (CHAR0) mittleren Alters entgegen. Sie hat einen Deutschen Schäferhund(Rex) und einen Terrier(Cindy) dabei. Cindy zerrt und springt in eure Richtung und kläfft die SC an(ggf. Zornwurf). Während Rex euch argwöhnisch fixiert.NEWLINE'
                ' Die Frau stämmt sich dagegen aber weicht nicht aus. Sie ruft, "keine Sorge, außer einer großen Klappe macht sie nix, (CINDY jetzt sei endlich mal still)".NEWLINE'
                ' Als plötzlich der Wind dreht und nun von den SC zu den Hunden weht ändert Cindy schlagartig ihre Meinung und will fliehen, während Rex sich klein macht und seine unterwürfigste Haltung einnimmt.NEWLINE'
                ' "Na also, so ists Brav, (CINDY KOMM)". Und so zieht sie ihre Hunde an vorbei.NEWLINE'
                ' (Dieses Verhalten von den Tieren kann Aufmerksamkeit auf die SC ziehen, je nachdem wie viel Druck erzeugt werden soll, bzw. wer nach den SC sucht.)',
        'nscConditions': [
            {
                'art': 'Human',
                'pronomen': 'sie',
                'NICHTalter': ['gerade Volljährig', 'zwischen 40 und 50', 'ende 50', 'über 60'],
            },
        ]
    },
    {
        'name': 'Flyer Verteiler',
        'text': 'Zwei Junge Frauen (CHAR0) und (CHAR1) mit großen Rucksäcken kommen auf das Rudel zu.NEWLINE'
                ' Die Blonde spricht zuerst: "Hey habt ihr kurz Zeit für mich?" und ohne Zeit für eine Antwort zu lassen "Es geht um eine kleine Umfrage. Ich krieg dafür dass ihr einen Fragebogen ausfüllt 5€. Könnt ihr mir dabei helfen mein Studium zu finanzieren? Es gibt auch für euch eine kleine Nettigkeit"NEWLINE'
                ' Sie und ihre Kollegin sind sehr aufdringlich und lassen sich nicht so einfach abwimmeln.NEWLINE'
                ' Falls die SC einwilligen muss jeder einen Fragebogen ausfüllen und bekommt dafür ein Tütchen mit Gummibären.NEWLINE'
                ' Falls sie nicht einwilligen wollen müssen sie sich Herausreden (Ausflüchte mit erhöhter Schwierigkeit).',
        'nscConditions': [
            {
                'art': 'Human',
                'pronomen': 'sie',
                'beschreibungFrisur': ['blond'],
                'alter': ['gerade Volljährig', 'zwischen 20 und 30'],
            },
            {
                'art': 'Human',
                'pronomen': 'sie',
                'alter': ['gerade Volljährig', 'zwischen 20 und 30'],
            },
        ]
    },
    {
        'name': 'Sexarbeiter',
        'text': 'Das Rudel hat sich auf den Straßenstrich verirrt und wird je nach Aussehen angegraben oder abwertend behandelt.NEWLINE'
                ' Um Spannungen einzuführen kann ein handgreiflicher, unfreundlicher Freier (CHAR0) eingeführt werden,NEWLINE'
                ' Oder ein Zuhälter (CHAR1),NEWLINE'
                ' oder minderjährige Sexarbeiter(CHAR2).NEWLINE'
                ' Lässt sich ein SC überreden? Greift das Rudel ein wenn ein Freier brutal wird? Wie reagieren die SC auf die Situation?',
        'nscConditions': [
            {
                'art': 'Human',
                'pronomen': 'er',
            },
            {
                'art': 'Human',
                'pronomen': 'er',
            },
            {
                'art': 'Human',
                'pronomen': 'sie',
                'alter': ['gerade Volljährig'],
            },
        ]
    },
    {
        'name': 'Dealer',
        'text': 'Die SC können beobachten, wie ein Dealer (CHAR0) Drogen verkauft.NEWLINE'
                ' Greifen die SC nicht ein, können sie vielleicht durch einen minderjährigen Kunden (CHAR1) dazu gebracht werden.NEWLINE'
                ' Stellen sie Käufer oder Kunden? Können sie den Verkäufer einschüchtern oder müssen sie ihn angreifen?',
        'nscConditions': [
            {
                'art': 'Human',
            },
            {
                'art': 'Human',
                'alter': ['gerade Volljährig'],
            },
        ]
    },
    {
        'name': 'Ehemaliger Lehrer / Mitschüler / Freund / Bekannter',
        'text': 'Ein Bekannter (CHAR0) aus dem früheren Leben eines SC begegnet dem Rudel und erkennt den SC wieder.NEWLINE'
                ' Was weiß er von dem Lebenswandel? Stellt er den SC zu Rede? Wurde der SC vermisst gemeldet? NEWLINE'
                ' (Mit dieser Begegnung kann die Hintergrundgeschichte des SC in die Story verwoben werden. Oder es wird zumindest gezeigt, dass die Welt größer ist, als dass was die SC sehen)',
        'nscConditions': [
            {
                'art': 'Human',
            },
        ]
    },
    {
        'name': 'Junggesellen Abschied',
        'text': 'Eine Gruppe laut gröhlender Männer nähert sich dem Rudel und bietet ihnen Alkohol an, wenn sie mitspielen.NEWLINE'
                '(Hier können jegliche Junggesellen-Aufgaben und Spiele eingebaut werden. ggf. Inklusive Sexueller Belästigung und/oder Schlägereien)NEWLINE'
                'Bräutigam: (CHAR0)NEWLINE'
                'Gäste:NEWLINE (CHAR1)NEWLINE (CHAR2)NEWLINE (CHAR3)NEWLINE (CHAR4)NEWLINE (CHAR5)NEWLINE (CHAR6)NEWLINE (CHAR7)NEWLINE (CHAR8)NEWLINE',
        'nscConditions': [
            {
                'art': 'Human',
                'pronomen': 'er',
            },
            {
                'art': 'Human',
                'pronomen': 'er',
            },
            {
                'art': 'Human',
                'pronomen': 'er',
            },
            {
                'art': 'Human',
                'pronomen': 'er',
            },
            {
                'art': 'Human',
                'pronomen': 'er',
            },
            {
                'art': 'Human',
                'pronomen': 'er',
            },
            {
                'art': 'Human',
                'pronomen': 'er',
            },
            {
                'art': 'Human',
                'pronomen': 'er',
            },
            {
                'art': 'Human',
                'pronomen': 'er',
            },
        ]
    },
]

wildnisEncounter = [
    {
        'name': 'Wilderer',
        'text': 'Das Rudel hört einen Schuss. Dabei wissen sie, dass der Jäger (CHAR0), welcher im hier zuständig ist (und auch Kinfolk ist), gerade nicht am Jagen ist.NEWLINE'
                ' Wenn sich die SC in Richtung des Schusses bewegen, dann stoßen sie recht schnell auf zwei Männer (CHAR1) und (CHAR2), welche sich einem angeschossenen Wildschwein nähern.NEWLINE'
                ' Das Tier ist noch nicht tot und zappelt noch. Der Schuss hat den Pansen und die Hüfte durchschlagen, abgesehen von dem Anblick sind sowohl das schmerzensröcheln, als auch der Gestank deutlich wahrnehmbar.NEWLINE'
                ' Die beiden Männer beratschlagen laut ob das Fleisch noch zu gebrauchen ist, oder ob sie lieber ein neues Schwein suchen (ggf. Zornwurf).NEWLINE'
                ' Beide tragen Gewehre, sind jedoch keine guten Schützen.',
        'nscConditions': [
            {
                'art': 'Kinfolk',
            },
            {
                'art': 'Human',
                'pronomen': 'er',
                'beschreibungKleidung': ['alte ', 'zweckmäßige '],
                'beschreibungKleidungsFarbe': ['braunen', 'tarnenden']
            },
            {
                'art': 'Human',
                'pronomen': 'er',
                'beschreibungKleidung': ['alte ', 'zweckmäßige '],
                'beschreibungKleidungsFarbe': ['braunen', 'tarnenden']
            }
        ]
    },
    {
        'name': 'Umweltsünder Spuren',
        'text': 'Das Rudel stößt im Wald auf einen großen Berg Müll. Hier hat jemand (CHAR0) einen gesamten Hänger abgeladen. Darunter sind einige Elektrogeräte und Farbeimer und vieles mehr.NEWLINE'
                ' Wenn das Rudel gründlich genug sucht(Nachforschen, erhöhter Schwierigkeit), können sie eine Adresse finden, welche jedoch aktuell nicht bewohnt ist.NEWLINE'
                ' Der vorherige Mieter wollte seinen Müll scheinbar nicht mitnehmen.NEWLINE'
                ' Je nachdem wieviel Zeit in dieser Begegnunge verbracht werden soll, kann das Rudel die neue Adresse ausfindig machen und sie befindet sich in Reichweite.',
        'nscConditions': [
            {
                'art': 'Human',
            },
        ]
    },
    {
        'name': 'Umweltsünder Täter',
        'text': 'Das Rudel hört einiges an Geschepper und Geklirr. Wenn sie dem Nachgehen, stoßen sie auf ein Paar (CHAR0) und (CHAR1), welches gerade einiges an Müll von einem Anhänger herunterwirft und schiebt. Mitten Im Wald.NEWLINE'
                ' Stellt das Rudel sie zu Rede? Eskaliert die Situation?',
        'nscConditions': [
            {
                'art': 'Human',
            },
            {
                'art': 'Human',
                'nachname': 'CHAR0.nachname'
            },
        ]
    },
    {
        'name': 'Pfadfinder',
        'text': 'Es ist Gesang zu hören. Die Ursache ist eine größere Gruppe von Pfadfindern(3 mal 7) aus jeweils einem Jugendlichen und 6 Kindern.  Jeder von den Kindern trägt einen Stock mit Nagel dran und die Jugendlichen ziehen jeweils einen Bollerwagen.NEWLINE'
                ' In den Wägen befindet sich schon einiges an Müll und die Kinder rennen umher und sammeln noch mehr ein.NEWLINE'
                ' Die Menschen befinden sich im Revier der Septe, jedoch sammeln sie Müll, was etwas gutes ist.NEWLINE'
                ' Können die SC die Pfadfinder freundlich in eine richtige Richtung lenken?NEWLINE'
                ' Die 3 Fähnleinführer sind (CHAR0), (CHAR1) und (CHAR2).NEWLINE'
                ' Von den Kindern treten die meisten nicht mit den SC in Kontakt, daher nur (CHAR3) und (CHAR4) als Beispiele.',
        'nscConditions': [
            {
                'art': 'Human',
                'alter': ['gerade Volljährig'],
            },
            {
                'art': 'Human',
                'alter': ['gerade Volljährig'],
            },
            {
                'art': 'Human',
                'alter': ['gerade Volljährig'],
            },
            {
                'art': 'Human',
                'pronomen': 'er',
                'alter': ['gerade Volljährig'],
            },
            {
                'art': 'Human',
                'pronomen': 'sie',
                'alter': ['gerade Volljährig'],
            },
        ]
    },
    {
        'name': 'Waldbrand',
        'text': '(Ein Wahrnehmungswurf könnte bestimmen, wie früh die SC den Brand bemerken)NEWLINE'
                ' Es ist ein größerer Waldbrand, der von dem Rudel allein nicht gelöscht und nur mit großen Anstrengungen eingegrenzt werden kann. Mögliche Herangehensweisen:NEWLINE'
                ' Schneise schlagen (Überleben um den besten Ort zu finden und Körperkraft und Widerstand, um genug Bäume zu fällen)NEWLINE'
                ' Hilfe (von der Septe) holen (Sportlichkeit um schnell genug zu sein)NEWLINE'
                ' Kontakt zu den Geistern aufnehmen (Geistersprache und ggf. Gnosis)NEWLINE'
                ' etc.',
        'nscConditions': []
    },
    {
        'name': 'Wanderer Pilzsucher',
        'text': '(Das Rudel stößt auf eine ältere Frau (CHAR0), mit einem Korb und einem Rucksack. In dem Korb liegt ein kleines Messer und ein Tuch.NEWLINE'
                ' Sie klettert suchend über Wurzeln und Böschungen. Sie sucht nach Pilzen und lässt sich von irgendwelchen Halbstarken nicht verbieten, tiefer in den Wald(in Richtung Caern zu gehen).NEWLINE'
                ' Wie können die SC sie davon abhalten, sich dem Caern weiter zu nähern.',
        'nscConditions': [
            {
                'art': 'Human',
                'pronomen': 'sie',
                'alter': ['zwischen 40 und 50', 'ende 50', 'über 60'],
            },
        ]
    },
]

umbraEncounter = [
    {
        'name': 'Plagengeist',
        'text': 'Das Umbra wirkt unfreundlicher. Karger. Die Unreinheit verzehrt einen Gnosispunkt bei den SC. Die Zeit vergeht langsamer oder die SC verlieren ihr Zeitgefühl.NEWLINE'
                ' Es riecht ungewohnt. Süßlich. Lecker.  Eine Spur Verwesung (Wahrnehmungswurf). Vor den SC erscheint ein Haufen von feinstem und wohlriechendem Essen.NEWLINE'
                ' Braten, Speck, Pizza, Paradiesäpfel, Schokoladeneiscreme, Torte, Waffeln. Direkt an dem Berg hockt eine kleine Gestalt mit dem Rücken zu den SC. Die Gestalt schaufelt Essen mit beiden Händen zum Kopf und man hört schmatzen.NEWLINE'
                ' Wenn sich das Rudel weiter nähert dreht sich die Gestalt ruckartig um und man sieht ein Gebilde wie bei einer Venusfliegenfalle.NEWLINE'
                ' Ein Plagenngeist(CHAR0) das ist jedoch nur der Kopf, welche an einem schlangenartigem Hals aus dem Haufen zu ragen scheint. Der Haufen beginnt zu beben und sich auf das Rudel zu zubewegen.NEWLINE'
                ' (ggf. die Stärke anpassen)',
        'nscConditions': [
            {
                'art': 'Plagengeist',
                'adjectiv': ['dröhnende', 'schändliche', 'höllische', 'fiese', 'ruchlose', 'aggressive', 'verfressene', 'verlockende', 'leckere'],
                'baneType': ['Plage der Völlerei', 'Schlaraffenplage', 'Fallenplage', 'Plage des Genusses', 'Plage der Sättigung', 'Plage der List'],
                'Powerlevel': 3
            },
        ]
    },
    {
        'name': 'Umbrawahnsinn',
        'text': 'Man hört eine Melodie. Trompeten, Marschtrommeln, Stampfende Füße.NEWLINE'
                ' Direkt vor den SC ploppt ein Rosa Elefant auf. Ihm folgen in kurzem Abstand einige Weitere. Die Elefanten marschieren im Kreis um das herum.NEWLINE'
                ' Jedes mal, wenn einer der SC aus dem Kreis ausbrechen will, versperren sie den Weg.NEWLINE'
                '(Handlungsvorschläge:)NEWLINE'
                'Angreifen -> Elefanten fliehen verärgert NEWLINE'
                'Einschüchtern -> Elefanten fliehenNEWLINE'
                'Verhandeln (Überreden/Manipulieren) -> Weg wird freigegebenNEWLINE'
                'Chiminage anbieten (ein Kunststück wie im Zirkus) -> Geleit für die Reise durch das Umbragebiet',
        'nscConditions': [
            {
                'art': 'Plagengeist',
                'adjectiv': ['dröhnende', 'schändliche', 'höllische', 'fiese', 'ruchlose', 'aggressive', 'verfressene', 'verlockende', 'leckere'],
                'baneType': ['Plage der Völlerei', 'Schlaraffenplage', 'Fallenplage', 'Plage des Genusses', 'Plage der Sättigung', 'Plage der List'],
                'Powerlevel': 3
            },
        ]
    },
    {
        'name': 'Wyrmkontakt',
        'text': 'Wenn die SC seit einiger Zeit im Umbra unterwegs sind: Die SC bekommen ein wages Gefühl, dass sich irgendetwas geändert hat.NEWLINE'
                '(Wahrnehmung und Okkultismus mit erhöhter Schwierigkeit)NEWLINE'
                'ab 3 Erfolge: Hintereingang in einen Wyrmbau NEWLINE'
                'Es sind keine Wyldnisgeister zu sehen. Aber auch keine Plagen. Seltsam. Nur einmal Blinzeln später erscheinen Schlieren in der Luft.NEWLINE'
                ' Etwas riesiges. Etwas riesiges Wyrm-verseuchtes. Und es ist auf dem Weg ins diesseits. Irgendetwas scheint es anzuziehen. In weniger als einer Stunde wird es ankommen.NEWLINE'
                ' Kiebitzen (der Todesgürtel ist hier extrem durchlässig): Man sieht 13 Tänzer in einem Raum sitzen, diese Tänzer sind über und über mit Blut beschmiert und mit Gedärmen behängt. In der Mitte ist ein Tänzer und die anderen sind in Spiralförmig um ihn herum angeordnet.NEWLINE'
                ' Der mittlere Tänzer hat vor sich 3 blutige bündel liegen. Aus einem Davon guckt eine winzige Hand heraus. Zwei Finger sind abgerissen. An jeder der vier Wände hängt je ein Mann und eine Frau, mit großen Gleisnägeln an die Wand geschlagen.NEWLINE'
                ' Die Gesichter sind gehäutet und die Brustkörbe sind aufgebrochen. In jeder Ecke des Raums brennt ein grünes Baalsfeuer.NEWLINE'
                ' Die Tänzer sind alle in Meditation versunken.NEWLINE NEWLINE'
                '1 Erfolg: Tänzerrudel im Diesseits NEWLINE'
                ' Es sind keine Wyldnisgeister zu sehen. Auch keine Weberspinnen. Etwas scheint das Umbra aus dem diesseits zu verseuchen: NEWLINE'
                ' Drei Tänzer sind gerade damit beschäftigt einen Menschen zu foltern und zu fressenNEWLINE NEWLINE'
                '(Es zählt nur der höchste Wahrnehmungswurf. Sollten die SC angreifen, können sie durch ihr überraschendes Auftreten die meisten Tänzer töten, bevor diese reagieren können.)NEWLINE'
                'Deshalb nur drei Tänzer als Beispiel:NEWLINE'
                '(CHAR0) NEWLINE (CHAR1) NEWLINE (CHAR2)',
        'nscConditions': [
            {
                'art': 'bsd',
                'Powerlevel': 3
            },
            {
                'art': 'bsd',
                'Powerlevel': 3
            },
            {
                'art': 'bsd',
                'Powerlevel': 3
            }
        ]
    },
    {
        'name': 'Weber gibt es auch',
        'text': 'Die Netze werden dichter. Die Zahl der Spinnengeister nimmt immer weiter zu. Die Netze werden noch dichter (Sportlichkeit zur fortbewegen nötig)NEWLINE'
                'Kiebitzen -> Baustelle von einem Umspannwerk, gerade kein Arbeiter da.NEWLINE'
                'Ein Weberrinnengeist versperrt den Weg. Viele andere Beobachten die SC von allen Seiten.NEWLINE'
                'Seitwärts wechseln -> Todesgürtelwert 9 NEWLINE'
                'Verhandeln: Chiminage für freies Geleit(Einige Kabel sind Total verheddert (Handwerkswurf) -> Hilfe im nächsten Kampf oder Verzeihen falls Netz beschädigt wurde.',
        'nscConditions': []
    },
    {
        'name': 'Auch andere Kämpfen',
        'text': 'Man hört Kampfrufe und Geheul. Als das Rudel näher kommt sieht es ein Gefecht zwischen 10 Garou und 3 Plagen.NEWLINE'
                'Die Garou sind auf kürzerer Distanz eindeutig in Tänzer und nicht Tänzer zu sortieren. Einer der nicht-Tänzer liegt bereits am Boden. NEWLINE'
                'Garou-Rudel: (CHAR0) NEWLINE'
                'Tänzer-Rudel: (CHAR1) NEWLINE'
                'Plagen: (CHAR2) (CHAR3) (CHAR4)',
        'nscConditions': [
            {
                'art': 'garouPack',
                'minMembers': 5,
                'maxMembers': 5,
            },
            {
                'art': 'bsdPack',
                'minMembers': 5,
                'maxMembers': 5,
            },
            {
                'art': 'Plagengeist',
            },
            {
                'art': 'Plagengeist',
            },
            {
                'art': 'Plagengeist',
            }
        ]
    },
    {
        'name': 'Feuer',
        'text': 'Vor den SC taucht ein Feuerelementar auf. Und noch ein Weiteres. Und dann noch viele mehr.NEWLINE'
                ' Kiebitzen -> Eine Feuerstelle in einem Wald. Niemand in der Nähe. Sehr viel trockenes Holz/Blätter in der Nähe.NEWLINE'
                ' Kann das Feuer vom Rudel gelöscht werden, bevor ein Waldbrand entsteht?',
        'nscConditions': []
    },
    {
        'name': 'Der Prototyp',
        'text': 'Ein Windgeist fliegt an dem Rudel vorbei. Ungefähr 5m vor ihnen verschwindet der Geist.NEWLINE'
                ' Ein weiterer Geist fliegt 3m neben den SC vorbei und verschwindet auf der gleichen Höhe.NEWLINE'
                ' Beide male mit einem lautem Zischen gefolgt von einem Knistern.NEWLINE'
                ' Ein Wasserelementar hält bei euch an und bewegt sich langsam vorwärts tastend. Ein leises Zischen und knistern und der Elementar taumelt zurück, wird durchscheinender.NEWLINE'
                ' Kiebitzen -> Eine Scheune. Mit Solarzellen auf dem Dach und zugenagelten Fenstern.NEWLINE'
                ' Der Wasserelementar spricht die SC (falls keiner Geistersprache beherrscht auf Garou) an.NEWLINE'
                ' "Ich bin geschwächt... Etwas vernichtet Geister... kein Schlummer... bitte Helft uns... Ich falle in den Schlummer... die Anderen sind für immer fort"NEWLINE'
                'In der Scheune arbeitet ein Wissenschaftler daran, ein Kraftfeld gegen Böse Geister zu entwickeln. Er heißt (CHAR0) und hat einen Doktortitel in Physik.NEWLINE'
                ' Vor 5 Jahren hat eine Plage (CHAR1) seinen Geist kontrolliert und einen Mord begangen. Seit dem versucht er sich dagegen zu wappnen.NEWLINE'
                ' In der Scheune baut er einen Prototypen zur Geisterabwehr. Gegenüber den Garou ist er misstrauisch aber nicht feindselig.NEWLINE'
                ' Er erklärt seine Motive und will eigentlich nur die bösen Geister vernichten.NEWLINE'
                ' Mögliche Herangehensweisen des Rudels:NEWLINE'
                ' Überreden den Prototypen nie wieder zu benutzen, abschalten des Apparats: (Sehr schwierige Probe, ggf. lügt er um den Apparat später wieder zu benutzen oder weiter zu verbessern.)NEWLINE'
                ' Überreden mit Blutgeschwistern zusammen zu arbeiten um ihn auf die Richtige Seite zu ziehen: (normale Probe, ggf. bietet sich hier Potential für weitere Abenteuer oder die Septe entschließt sich ihn zu bewachen.)NEWLINE'
                ' Töten: wenn er genug Vorwarnung bekommt, versucht er zu fliehen und setzt dabei einen Flammenwerfer und Sprengsätze ein. Ansonsten stirbt er wie ein normaler Mensch sehr schnell.NEWLINE'
                ' Einschüchtern: (erhöhte Schwierigkeit, ggf. setzt er seine Arbeit an einem anderen Ort fort)',
        'nscConditions': [
            {
                'art': 'Human',
                'NICHTalter': ['gerade Volljährig'],
                'pronomen': 'er',
                'scRudel': 'Misstrauisch',
                'motivation': 'Angst vor Bösem/Weltuntergang',
                'pläne': 'Nachforschungen',
            },
            {
                'art': 'Plagengeist',
            }
        ]
    },
    {
        'name': 'Menschenwerk',
        'text': 'Das Rudel entdeckt einen Dachsgeist. Dieser zappelt und schlägt wild um sich.NEWLINE'
                ' (In der Stofflichen Welt) Ein Dachs hat sich in einer Schlinge verfangen und kommt nicht mehr frei.NEWLINE'
                'Den Dachs im Diesseits befreien:  zuerst Beruhigen (Tierkunde) und danach die Schlinge entfernen (Handwerk)NEWLINE'
                'Den Dachs beruhigen im Umbra (Empathie) und danach die Schlinge im diesseits entfernenNEWLINE'
                'Den Dachs Töten / ErlösenNEWLINE '
                '(Ein Zeitlimit erhöht die Spannung.NEWLINE'
                ' Falls die Zeit abgelaufen ist, oder das Befreien fehlschlägt, stirbt der Dachs und der Geist beginnt in Schlummer zu verfallen, da er dies nicht möchte, ist er bereit, sich in einen Fetisch bannen zu lassen.NEWLINE'
                ' Wenn das Befreien erfolgreich ist, gibt der Dachsgeist jedem SC ein Haar: "Solltet ihr jemals graben müssen, könnt ihr mich mit diesen Haaren rufen."',
        'nscConditions': []
    },
]


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
    #random.seed(int(time.strftime("%H%M%S", time.localtime())) + counter)
    # seed = kinfolkGen.GetRandomVorname(initSeed=initVal)  + '_' + kinfolkGen.GetRandomNachname(initSeed=initVal)
    # random.seed()
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
    # print(result)

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
                nscNumber = int(
                    encounterText[tokenStart + len(token):encounterText.find(')', tokenStart)])
                if encounter['nscConditions'][nscNumber]['art'] in ['Human', 'Kinfolk', 'Garou', 'Ragabash', 'Theurge', 'Philodox', 'Galliard', 'Ahroun','vampir']:
                    #result += f'TRYING: {HandleSeed(encounter,nscNumber,chars,token)}'
                    nsc = BuildNSC(
                        seed=HandleSeed(encounter, nscNumber, chars, token),
                        language=language,
                        Art=encounter['nscConditions'][nscNumber]['art'],
                        Stamm='' if 'stamm' not in encounter['nscConditions'][
                            nscNumber] else encounter['nscConditions'][nscNumber]['stamm'],
                        Powerlevel=0 if 'Powerlevel' not in encounter['nscConditions'][
                            nscNumber] else encounter['nscConditions'][nscNumber]['Powerlevel'],
                        packname='' if 'packname' not in encounter['nscConditions'][
                            nscNumber] else encounter['nscConditions'][nscNumber]['packname'],
                        occupation='' if 'occupation' not in encounter['nscConditions'][
                            nscNumber] else encounter['nscConditions'][nscNumber]['occupation'],
                        brut='' if 'brut' not in encounter['nscConditions'][
                            nscNumber] else encounter['nscConditions'][nscNumber]['brut']
                    )
                    counter = 0
                    while not CheckNSCwithConditions(nsc, encounter['nscConditions'][nscNumber], chars):
                        counter += 1
                        #print(f'Encounter "{encounter["name"]}" CHAR{nscNumber} retrying ({nsc["vorname"]+" "+nsc["nachname"]} was unfitting): {counter} to fit Condition: {list(encounter["nscConditions"][nscNumber].items())}')

                        #result += f'RETRYING: {HandleSeed(encounter,nscNumber,chars,token,counter)}'
                        nsc = BuildNSC(
                            seed=HandleSeed(encounter, nscNumber,
                                            chars, token, counter),
                            Art=encounter['nscConditions'][nscNumber]['art'],
                            language=language,
                            Stamm='' if 'stamm' not in encounter['nscConditions'][
                                nscNumber] else encounter['nscConditions'][nscNumber]['stamm'],
                            Powerlevel=0 if 'Powerlevel' not in encounter['nscConditions'][
                                nscNumber] else encounter['nscConditions'][nscNumber]['Powerlevel'],
                            packname='' if 'packname' not in encounter['nscConditions'][
                                nscNumber] else encounter['nscConditions'][nscNumber]['packname'],
                            occupation='' if 'occupation' not in encounter['nscConditions'][
                                nscNumber] else encounter['nscConditions'][nscNumber]['occupation'],
                            brut='' if 'brut' not in encounter['nscConditions'][
                                nscNumber] else encounter['nscConditions'][nscNumber]['brut']
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
                        powerlevel=0 if 'Powerlevel' not in encounter['nscConditions'][
                            nscNumber] else encounter['nscConditions'][nscNumber]['Powerlevel']
                    )
                    chars[f'{token}{nscNumber}'] = bane
                    encounterText = encounterText.replace(
                        f'({token}{nscNumber})', f'({bane["link"]})')
                    pass
                elif encounter['nscConditions'][nscNumber]['art'] == 'bsd':
                    nsc = BuildBSD(
                        seed=HandleSeed(encounter, nscNumber, chars, token),
                        language=language,
                        Powerlevel=0 if 'Powerlevel' not in encounter['nscConditions'][
                            nscNumber] else encounter['nscConditions'][nscNumber]['Powerlevel'],
                        packname='' if 'packname' not in encounter['nscConditions'][
                            nscNumber] else encounter['nscConditions'][nscNumber]['packname'],
                    )
                    counter = 0
                    while not CheckNSCwithConditions(nsc, encounter['nscConditions'][nscNumber], chars):
                        counter += 1
                        # print(f'Encounter "{encounter["name"]}" CHAR{nscNumber} retrying: {counter}')
                        nsc = BuildNSC(
                            seed=HandleSeed(
                                encounter, nscNumber, chars, token),
                            language=language,
                            Powerlevel=0 if 'Powerlevel' not in encounter['nscConditions'][
                                nscNumber] else encounter['nscConditions'][nscNumber]['Powerlevel'],
                            packname='' if 'packname' not in encounter['nscConditions'][
                                nscNumber] else encounter['nscConditions'][nscNumber]['packname'],
                        )
                    # print(f'YAY: {nsc["vorname"]} {nsc["nachname"]} erfüllt alle Bedingungen für {token}{nscNumber}')
                    chars[f'{token}{nscNumber}'] = nsc
                    encounterText = encounterText.replace(
                        f'({token}{nscNumber})', f'({nsc["link"]})')
                    pass
                elif encounter['nscConditions'][nscNumber]['art'] == 'garouPack':
                    pack = BuildGarouPack(
                        seed=-
                        1 if 'seed' not in encounter['nscConditions'][
                            nscNumber] else encounter['nscConditions'][nscNumber]['seed'],
                        limitTribes=[] if 'limitTribes' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['limitTribes'],
                        limitBreeds=[] if 'limitBreeds' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['limitBreeds'],
                        minMembers=3 if 'minMembers' not in encounter['nscConditions'][
                            nscNumber] else encounter['nscConditions'][nscNumber]['minMembers'],
                        maxMembers=6 if 'maxMembers' not in encounter['nscConditions'][
                            nscNumber] else encounter['nscConditions'][nscNumber]['maxMembers'],
                    )
                    chars[f'{token}{nscNumber}'] = pack
                    encounterText = encounterText.replace(
                        f'({token}{nscNumber})', f'({pack["link"]})')
                    pass
                elif encounter['nscConditions'][nscNumber]['art'] == 'bsdPack':
                    pack = BuildBSDPack(
                        seed=-
                        1 if 'seed' not in encounter['nscConditions'][
                            nscNumber] else encounter['nscConditions'][nscNumber]['seed'],
                        limitBreeds=[] if 'limitBreeds' not in encounter['nscConditions'][nscNumber] else encounter['nscConditions'][nscNumber]['limitBreeds'],
                        minMembers=3 if 'minMembers' not in encounter['nscConditions'][
                            nscNumber] else encounter['nscConditions'][nscNumber]['minMembers'],
                        maxMembers=6 if 'maxMembers' not in encounter['nscConditions'][
                            nscNumber] else encounter['nscConditions'][nscNumber]['maxMembers'],
                    )
                    chars[f'{token}{nscNumber}'] = pack
                    encounterText = encounterText.replace(
                        f'({token}{nscNumber})', f'({pack["link"]})')
                    pass
                else:
                    pass
            pass
        elif token == 'NEWLINE':
            encounterText = encounterText.replace(
                'NEWLINE ', f'{Newline(language)}').replace('NEWLINE', f'{Newline(language)}')
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
