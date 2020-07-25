import random

haltungen = {
    'Überheblich': 'Breitbeinig zurückgelehnt, Arme auf den Lehnen. Vorsicht: Nur einsetzen, wenn du weißt, dass es für alle Beteiligten OK ist.',
    'Schüchtern': 'Fußspitzen nach innen, Hände im Schoß (mit gesenktem Kopf hochschauen).',
    'Streng': 'Gerader Rücken, Beine parallel, Hände auf den Beinen.',
    'Aufmerksam': 'Auf der Stuhlkante, nach vorne gelehnt, Ellenbogen auf dem Tisch. Varianionen: Kinn auf linke oder rechte Hand egstützt, oder auf beide.',
    'Gelangweilt': 'Auf eine Armlehne gestützt, Beine etwas breiter, die nicht abgestützte Hand auf einem Bein oder zwischen den Beinen.',
    'Verängstigt': 'Schultern hochgezogen, eine Hand hält das Handgelenk des anderen Armes.',
    'Hochnäsig': 'Wie der Name sagt: Kopf hoch erhoben. Für maximalen Effekt Brille auf die Nase schieben und durch die jetzt tiefere Brille schauen.',
    'Verspielt': 'Kopf zur Seite gelegt.',
    'Eindringen': 'Auf den Tisch stützen oder über den Tisch zu den Spielern hinuberbeugen. In den richtigen Situationen weiter nach vorne, um den Worten Nachdruck zu verleihen. Eher aggressiv (unter Druck setzen). Dringt in den Bereich des anderen ein. Vorsicht: Nur einsetzen, wenn du weißt, dass es für alle Beteiligten OK ist. Gerade Eindringen ist sehr aggressiv und kann entsprechende Gegenreaktionen provozieren oder Leute bleibend einschüchtern - also emotional verletzen.'
}

gestiken = {
    'Angriff': 'Zeigefinger aneinandergelegt, restliche Finger verschränkt: Pistole. Oft auf den Tisch gelegt. Zeigt auf den Angegriffenen.',
    'Wir müssen eine gemeinsame Lösung finden': 'Die Fingerspitzen zusammen. Immer nur kurz lösen. Steht für Verbindung der verschiedenen Interessen (wie finden wir etwas, das für alle passt?), aber dank Simpsons auch für Mr. Burns und dank Merkel für intrigante Politik aus dem Hintergrund :)',
    'Fromm': 'Handflächen zusammen oder Hände verschränkt, vor der Brust (im Schoß funktioniert nur, wenn wir nicht am Tisch sitzen, weil es die restliche Haltung zu wenig beeinflusst – vergleiche Schüchtern).',
    'Innere Spannung': 'Fäuste. Sollten sichtbar sein, z.B. auf dem Tisch liegend. Wenn die Anspannung steigt, können sie fester gespannt werden und auch mal auf den Tisch stoßen.',
    'Aktive Abwehr': 'Handflächen nach außen zu den SpielerInnen, Hände gerade, Finger aneinander. Immer wieder heben, wenn irgendwas den Charakter betreffen könnte.',
    'Abstand': 'Arme vor der Brust verschränkt. „Ich schau mir erstmal genau an, um was es geht, bevor ich entscheide, ob ich mich darauf einlasse.“',
    'Ausladend': 'Große Gesten, jeden Satz mit einer weit ausladenden Geste unterstreichen. Darf sich auch gerne widersprechen (meist hat der Körper recht; Beispiel: Da vorne dann nach links!, zeigt mit dem ganzen Arm nach rechts). Clichéhaft bei Südländern, ich habe es aber auch schon bei Bayern sehr plastisch erlebt.',
    'Eng': 'Die Hände immer zwischen den Schultern und nah am Körper lassen. Traut sich nicht, aus sich raus zu gehen. Kann sehr gut mit Essen verbunden werden (Hände parallel, berühren sich fast, Ellenbogen am Körper)',
    'Shaolin': 'Eine Hand vor der Brust, Zeige- und Mittelfinger zeigen nach oben, Ring- und kleiner Finger gebeugt. Die andere frei verwenden. Klassische Kampfsportlerhaltung in der Diskussion.',
    'Hände kneten': 'Beide Hände sichtbar. Eine Hand hält die andere, knetet sie. Unsicherheit.',
    'Festhalten': 'Am Stuhl festhalten, Beine überkreuzt. Ich gehe hier nicht weg.',
    'Deprimiert': 'Kopf hängenlassen, jede Reaktion schwach. Bewegungen zwischendrin abbrechen bringt ja eh nichts.'
}

mimiken = {
    'Schlaff': 'Mundwinkel hängen, Wangen schlaff, wenig Gesichtsbewegung beim Sprechen.',
    'Verkniffen': 'Mund zusammengekniffen, Gesicht angespannt, Lippen nach dem Sprechen immer wieder schnell schließen.',
    'Griesgram': 'Mundwinkel fast schon comicartig runtergezogen. Typischer deutscher Politiker :)',
    'Grinsekatze': 'Lächelt fast immer breit und selbst in den schlimmsten Situationen friert das Lächeln nur ein, verschwindet aber nicht.',
    'Übertrieben': 'Jeden Gesichtsausdruck überziehen. Hast du mal den Film Die Maske gesehen - oder einen anderen von Jim Carrey, z.B. Ace Ventura? Wenn nein, solltest du das Nachholen, bevor du so einen NSC nutzt :)',
    'Einseitig': 'Nur eine Gesichtshälfte bewegen, die andere fast unbewegt.'
}

grundstimmungen ={
    'traurig',
    'erschöpft',
    'euphorisch',
    'eifrig',
    'frostig',
    'ängstlich'
}

merkmal ={
    'frostig','täuschend','charmant','großzügig','stoisch','weinerlich','misstrauisch','ehrlich','leichtgläubig','nachgiebig','autoritär','ideologisch','rebellisch','fröhlich','ehrgeizig','puritanisch',
    'verführerisch','energisch','dreist','prahlerisch','lüstern','trauernd','rational','sorglosaalglatt','abergläubisch','anmutig','arrogant','aufopfernd','bescheiden','demütig','depressiv','derb',
    'dienstbeflissen','diplomatisch','direkt','durchschaubar','eifrig','eigenwillig','einfallsreich','eingebildet','eisig','elegant','emotional','entgegenkommend','enthaltsam','extravagant','faul',
    'findig','gebildet','gerissen','gesellig','gierig','grob','hinterlistig','höflich','ignorant','keck','konservativ','kontrollierend','korrupt','kühn','laut','leise','liederlich','mutig','raffiniert',
    'redegewandt','respektabel','rätselhaft','sarkastisch','schlau','schläfrig','schroff','selbstbewusst','selbstgefällig','selbstgerecht','selbstsüchtig','seltsam','stur','tratschsüchtig','traurig',
    'träge','übereifrig','unerschrocken','verbindlich','vergebend','vergnügt','verschlafen','vertrottelt','verwahrlost','verwegen','waghalsig','wechselhaft','weise','willkürlich','wütend','zerstreut'
}

def MakeSpielAnweisung():
    nsc = {}
    haltung = random.choice(list(haltungen))
    nsc['haltung'] = (haltung,haltungen[haltung])
    gestik = random.choice(list(gestiken))
    nsc['gestik'] = (gestik,gestiken[gestik])
    mimik = random.choice(list(mimiken))
    nsc['mimik'] = (mimik,mimiken[mimik])
    nsc['grundstimmung'] = random.choice(list(merkmal))
    return nsc