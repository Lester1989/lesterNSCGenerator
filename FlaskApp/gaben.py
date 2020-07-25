import json

import codecs
import os

print('Aktueller Pfad: '+os.getcwd())

gabenTexte = json.load(codecs.open('/var/www/FlaskApp/FlaskApp/gabenTexte.json', 'r', 'utf-8-sig'))


print(f'{len(gabenTexte["alleGabenTexte"])} Gaben geladen')

Namen = {
    'Primatendaumen',
    'Stadtläufer',
    'HerrüberdasFeuer',
    'Überzeugungskraft',
    'GeruchdesMenschen',
    'Technologiestören',
    'MaldesWolfs',
    'Weltsprache',
    'Niederstarren',
    'BeruhigendeswildenTieres',
    'Kugelneinschüchtern',
    'Unruhe',
    'Gegenstandumformen',
    'Körperveränderung',
    'DenWolfbegraben',
    'Kokon',
    'SchutzzeichengegenGeister',
    'Einordnung',
    'Übermenschlich',
    'DenSchleierteilen',
    'Abstreifen',
    'Elementerschaffen',
    'Rattenkopf',
    'Urwut',
    'Wyrmgespür',
    'FluchdesHasses',
    'Graben',
    'HerrschaftüberdieGestalt',
    'Silbergespür',
    'Chamäleon',
    'GeistigeUnterredung',
    'Katzenaugen',
    'Schutzhülle',
    'BissderKlapperschlange',
    'GabedesStachelschweins',
    'Gliedmaßenverdorrenlassen',
    'ZornigerSchlag',
    'Totemgabe',
    'Vielgestaltigkeit',
    'Wahnsinn',
    'ArsenaldesRaubtiers',
    'AxisMundi',
    'Beuteaufspüren',
    'Beutedenken',
    'GeschärfteSinne',
    'Hasensprung',
    'Adlerauge',
    'Geistbenennen',
    'Geruchssicht',
    'Affenschwanz',
    'GaiasKraft',
    'Katzenpfoten',
    'KnebelfürdieWeberin',
    'Unnatürlichesfühlen',
    'Beißen',
    'FauchendesSchreckenswolfs',
    'GaiasSchrei',
    'Tierleben',
    'Elementargabe',
    'LieddesGroßenTiers',
    'AnsteckendesLachen',
    'GeruchdesfließendenWassers',
    'Lügengesicht',
    'Siegelöffnen',
    'VerschwimmenvordemTrübenAuge',
    'Beutegespür',
    'DiebstahldesVergessenen',
    'SeligeUnwissenheit',
    'Spinnenlied',
    'GlaubhafteLügen',
    'Gremlins',
    'Mondbrückeöffnen',
    'Pfadfinder',
    'LunasSegen',
    'VerbannunginsUmbra',
    'Welpenkörper',
    'KrallenderdiebischenElster',
    'TausendGestalten',
    'Feuerbringer',
    'BerührungderMutter',
    'Geisterfalle',
    'Geistersprache',
    'Umbraleine',
    'BefehligenderGeister',
    'Kampfmandala',
    'DasZweiteGesicht',
    'Exorzismus',
    'Netzwandler',
    'PulsdesUnsichtbaren',
    'Umbratarnung',
    'BeschlagenerSpiegel',
    'ErfassendesJenseitigen',
    'Essenzraub',
    'FormbarerGeist',
    'TierischesWesen',
    'UltimativeslogischesArgument',
    'WieimAnfang',
    'FängedesRichtspruchs',
    'GaiasWahrheit',
    'GeruchderwahrenGestalt',
    'Schmerzwiderstehen',
    'BefehligenderVersammlung',
    'KönigderTiere',
    'RufzurPflicht',
    'Zielbewusstsein',
    'GeruchdesEidbrechers',
    'Gleichgewichtsgespür',
    'SchwacherArm',
    'WeisheitderAltenWege',
    'AnnehmenderwahrenGestalt',
    'AufdenRücken',
    'GeruchdesJenseitigen',
    'Geas',
    'Granitwand',
    'Bandebrechen',
    'ExakteErinnerung',
    'GeistigeVerständigung',
    'RufderWyldnis',
    'Tiersprache',
    'Ablenkungen',
    'NächtlichesGeheul',
    'RufdesWyrms',
    'Traumsprache',
    'AugederKobra',
    'Heldenlied',
    'LieddesZorns',
    'Sirenengesang',
    'Brückengänger',
    'GabederTräume',
    'SchattenamFeuer',
    'Gedankenspiele',
    'GewebedesGeistes',
    'FällendeBerührung',
    'Inspiration',
    'Rasiermesserklauen',
    'Rudeltaktiken',
    'Spornklauen',
    'Kampfgeist',
    'WahreFurcht',
    'Zornschild',
    'HerzderWut',
    'Kampfheilung',
    'Silberklauen',
    'Windklauen',
    'AnfachenderbrennendenWut',
    'EisernerKiefer',
    'LichtdesVollmondes',
    'KussdesHelios',
    'Willensstärke',
    'UnaufhaltsamerKrieger',
    'Feenlicht',
    'Giftwiderstehen',
    'ZweiZungen',
    'Flammentanz',
    'GeheulderTodesfee',
    'GeheuldesUnsichtbaren',
    'Schlangenzunge',
    'Feenverwandte',
    'Glückskind',
    'Leylinien',
    'BalorsBlick',
    'Trugbild',
    'GabedesSpriggans',
    'NebelüberdemMoor',
    'RufderWildenJagd',
    'Diagnose',
    'EinfacheMaschinekontrollieren',
    'PlugandPlay',
    'Trickschuss',
    'Cybersinne',
    'HändevollerDonner',
    'Spannungsspitze',
    'Stahlfell',
    'Eindringen',
    'Elektroschock',
    'Elementargunst',
    'KomplexeMaschinekontrollieren',
    'Doppelgänger',
    'Einstimmung',
    'Funkwellenreiter',
    'Technobabbel',
    'Netzspinnebeschwören',
    'OrdnungimChaos',
    'Barmherzigkeit',
    'GeruchdesBruders',
    'Waffeblockieren',
    'ArsenaldesEinhorns',
    'BerührungderGroßmutter',
    'LunasRüstung',
    'ParaBellum',
    'Ruhe',
    'Geisterfreund',
    'LiebendeBerührung',
    'Überwältigen',
    'FreiwiederWindseitdemerstenTag',
    'Gelassenheit',
    'SchlaginsLeere',
    'Korona',
    'DerlebendeWald',
    'Kochen',
    'KraftderVerzweiflung',
    'SchätzeimMüll',
    'SüßerHonigduft',
    'AbscheulicherGestank',
    'Hundetarnung',
    'IndenRitzen',
    'WildheitderindieEckegedrängtenRatte',
    'GabederTermite',
    'GabedesStinktiers',
    'LachenderHyäne',
    'Rostruf',
    'Blinzeln',
    'Verseuchen',
    'Aufstand',
    'Überlebenskünstler',
    'BlitzschnelleReflexe',
    'FratzedesFenris',
    'FängedesNordens',
    'DieFluchtdesFeiglingshemmen',
    'KnurrendesRaubtiers',
    'Trollhaut',
    'Giftblut',
    'Schmerzumleiten',
    'ThorsMacht',
    'FelsinderBrandung',
    'HerzdesBerges',
    'FenrisBiss',
    'HeimdallsAusdauer',
    'WalhallasHorden',
    'Fenrisrufen',
    'AugedesJägers',
    'VerborgenerMörder',
    'WölfevordenToren',
    'TierischeInstinkte',
    'SchattendesImpergiums',
    'PfadloseEinöde',
    'Revier',
    'Gedankenschnelle',
    'Rudelfütterung',
    'DievielenAugendesRaubtiers',
    'Krokodilspakt',
    'Zerlegen',
    'GeheuldesTodes',
    'Schlingen',
    'Treibsand',
    'GaiasRache',
    'LykaonsFluch',
    'Schorfwandlerfluch',
    'GaiasSchild',
    'AuraderZuversicht',
    'LauscheranderWand',
    'Schattenweben',
    'TödlicheSchwäche',
    'ZüngleinanderWaage',
    'Donnerschlag',
    'EinTraumvontausendKranichen',
    'AngemessenesÄußeres',
    'HiebderSturmwinde',
    'FinsternisderNacht',
    'LebenderSchatz',
    'GöttlicherWind',
    'KühleStimmederVernunft',
    'LiedderErdmutter',
    'EiseskältederVerzweiflung',
    'LähmenderBlick',
    'LenkendesSturms',
    'Schattenschnitt',
    'UnterDruck',
    'Haft',
    'StärkedesBeherrschers',
    'OffeneWunden',
    'Gehorsam',
    'Schattenrudel',
    'AtemderWyldnis',
    'Männergestalt',
    'WyldeRegeneration',
    'FluchdesAeolus',
    'KalisZunge',
    'Knien',
    'Gnadenstoß',
    'Herzklaue',
    'SchmerzindenEingeweiden',
    'SchwingendesPegasus',
    'Qualenbereiten',
    'Wespenklauen',
    'Gorgonenblick',
    'Wyldnisverformung',
    'Falkenauge',
    'GriffdesFalken',
    'ZüngelndeFlamme',
    'EinheitdesRudels',
    'Empathie',
    'Handklinge',
    'Falkenklauen',
    'Flammenklinge',
    'GaiasZorn',
    'DemTodausweichen',
    'GeistigeBarriere',
    'Meisterschaft',
    'LunasRächer',
    'PfotendesneugeborenenWelpen',
    'ErneuerungdesZyklus',
    'EiserneEntschlossenheit',
    'Gleichgewicht',
    'Kanalisieren',
    'EinstimmungaufdieOberfläche',
    'InnereKraft',
    'InneresLicht',
    'Versuchungwiderstehen',
    'Wuxing',
    'GnadedenBesiegten',
    'Klarheit',
    'WiederkehrendeGunstdesWindes',
    'ÜbernatürlichesBewusstsein',
    'HarmonischeEinheitdersmaragdenenMutter',
    'Schlägeumlenken',
    'WeisheitdesSehers',
    'OrientierungamHimmel',
    'Stille',
    'VisionenvomDuat',
    'AusdauerdesBoten',
    'AufSebeksRücken',
    'Anpassung',
    'DergroßeSprung',
    'MaldesTodeswolfs',
    'SchwarzesMal',
    'EindämmenderHerzflut',
    'UnvorstellbareSchnelligkeit',
    'Mondtor',
    'Umbraerreichen',
    'Echsengeist',
    'Magiegespür',
    'Verhüllen',
    'WindungenderSchlange',
    'Fetischruf',
    'GeistdesFisches',
    'GeistdesVogels',
    'SchattenimMorgengrauen',
    'Nebelketten',
    'Totembannen',
    'Unsichtbarkeit',
    'Wahrsagen',
    'ZerreißenderKunst',
    'Elementarrufen',
    'HandderErdherren',
    'BlickunterdieHaut',
    'Makeltarnen',
    'Fetischpuppe',
    'Briserufen',
    'Eisecho',
    'SchlagderHerztrommel',
    'Tarnung',
    'MitdenWindgeisternsprechen',
    'SchneidenderWind',
    'WieeinLachsimWasser',
    'BlutdesNordens',
    'BlutigeLabsal',
    'Himmelslauf',
    'Kannibalengeistrufen',
    'KältedesfrühenFrostes',
    'HerzausEis',
    'Sturmgeisterbeschwören'
}
Ränge = ['Cliath', 'Pflegling', 'Adren', 'Athro', 'Ältester', 'Legende']
Bruten = ['Menschling','Metis','Lupus']
Stämme = ['Fianna','Glaswandler','KinderGaias','Knochenbeißer','NachfahrenDesFenris','RoteKlauen','Schattenlords','SchwarzeFurien','Silberfänge','Sternenträumer','StilleWanderer','Uktena','Wendigo','Tänzer der schwarzen Spirale']
BrutGabenNamen = {
    'Menschling': {
        'Cliath': ['Primatendaumen', 'Stadtläufer', 'HerrüberdasFeuer', 'Überzeugungskraft', 'GeruchdesMenschen'],
        'Pflegling': ['Technologiestören', 'MaldesWolfs', 'Weltsprache', 'Niederstarren'],
        'Adren': ['BeruhigendeswildenTieres', 'Kugelneinschüchtern', 'Unruhe', 'Gegenstandumformen'],
        'Athro': ['Körperveränderung', 'DenWolfbegraben', 'Kokon', 'SchutzzeichengegenGeister'],
        'Ältester': ['Einordnung', 'Übermenschlich', 'DenSchleierteilen'],
        'Legende': [], },
    'Metis': {
        'Cliath': ['Abstreifen', 'Elementerschaffen', 'Rattenkopf', 'Urwut', 'Wyrmgespür'],
        'Pflegling': ['FluchdesHasses', 'Graben', 'HerrschaftüberdieGestalt', 'Silbergespür', 'Chamäleon'],
        'Adren': ['GeistigeUnterredung', 'Katzenaugen', 'Schutzhülle'],
        'Athro': ['BissderKlapperschlange', 'GabedesStachelschweins', 'Gliedmaßenverdorrenlassen', 'ZornigerSchlag'],
        'Ältester': ['Totemgabe', 'Vielgestaltigkeit', 'Wahnsinn'],
        'Legende': []},
    'Lupus': {
        'Cliath': ['ArsenaldesRaubtiers', 'AxisMundi', 'Beuteaufspüren', 'Beutedenken', 'GeschärfteSinne', 'Hasensprung'],
        'Pflegling': ['Adlerauge', 'Geistbenennen', 'Geruchssicht'],
        'Adren': ['Affenschwanz', 'GaiasKraft', 'Katzenpfoten', 'KnebelfürdieWeberin', 'Unnatürlichesfühlen'],
        'Athro': ['Beißen', 'FauchendesSchreckenswolfs', 'GaiasSchrei', 'Tierleben'],
        'Ältester': ['Elementargabe', 'LieddesGroßenTiers'],
        'Legende': []},
    'Menschling des Wyrms': {
        'Cliath': ['Aura des Giftes'],
        'Pflegling': ['Spannungsspitze'],
        'Adren': ['Rostruf'],
        'Athro': ['Festmahl des Menschenfleischs'],
        'Ältester': [],
        'Legende': []},
    'Metis des Wyrms': {
        'Cliath': ['Bluten'],
        'Pflegling': [],
        'Adren': ['Der Bastard von Niemandem', 'Schmerz in den Eingeweiden'],
        'Athro': [],
        'Ältester': [],
        'Legende': []},
    'Lupus des Wyrms': {
        'Cliath': ['Wege  des  Urbanen  Wolfs'],
        'Pflegling': [''],
        'Adren': ['Tausend Zähne'],
        'Athro': [],
        'Ältester': ['Entfesselte  Instinkte'],
        'Legende': []}
}
VorzeichenGabenNamen = {
    'Ragabash': {
        'Cliath': ['AnsteckendesLachen', 'GeruchdesfließendenWassers', 'Lügengesicht', 'Siegelöffnen', 'VerschwimmenvordemTrübenAuge'],
        'Pflegling': ['Beutegespür', 'DiebstahldesVergessenen', 'SeligeUnwissenheit', 'Spinnenlied', 'Affenschwanz'],
        'Adren': ['GlaubhafteLügen', 'Gremlins', 'Mondbrückeöffnen', 'Pfadfinder'],
        'Athro': ['LunasSegen', 'VerbannunginsUmbra', 'Welpenkörper'],
        'Ältester': ['KrallenderdiebischenElster', 'TausendGestalten'],
        'Legende': ['Feuerbringer']   },
    'Theurge': {
        'Cliath': ['BerührungderMutter', 'Geisterfalle', 'Geistersprache', 'Umbraleine', 'Wyrmgespür'],
        'Pflegling': ['BefehligenderGeister', 'Geistbenennen', 'Kampfmandala', 'DasZweiteGesicht'],
        'Adren': ['Exorzismus', 'Netzwandler', 'PulsdesUnsichtbaren', 'Umbratarnung'],
        'Athro': ['BeschlagenerSpiegel', 'ErfassendesJenseitigen', 'Essenzraub', 'SchutzzeichengegenGeister'],
        'Ältester': ['FormbarerGeist', 'TierischesWesen', 'UltimativeslogischesArgument'],
        'Legende': ['WieimAnfang'],    },
    'Philodox': {
        'Cliath': ['FängedesRichtspruchs', 'GaiasWahrheit', 'GeruchderwahrenGestalt', 'Schmerzwiderstehen', 'Überzeugungskraft'],
        'Pflegling': ['BefehligenderVersammlung', 'KönigderTiere', 'RufzurPflicht', 'Zielbewusstsein'],
        'Adren': ['GeistigeUnterredung', 'GeruchdesEidbrechers', 'Gleichgewichtsgespür', 'SchwacherArm', 'WeisheitderAltenWege'],
        'Athro': ['AnnehmenderwahrenGestalt', 'AufdenRücken', 'GeruchdesJenseitigen'],
        'Ältester': ['Geas', 'Granitwand'],
        'Legende': ['Bandebrechen'],    },
    'Galliard': {
        'Cliath': ['ExakteErinnerung', 'GeistigeVerständigung', 'GeschärfteSinne', 'RufderWyldnis', 'Tiersprache'],
        'Pflegling': ['Ablenkungen', 'NächtlichesGeheul', 'RufdesWyrms', 'Traumsprache'],
        'Adren': ['AugederKobra', 'Heldenlied', 'LieddesZorns', 'Sirenengesang'],
        'Athro': ['Brückengänger', 'GabederTräume', 'SchattenamFeuer'],
        'Ältester': ['Gedankenspiele', 'GewebedesGeistes'],
        'Legende': ['Bandebrechen'],    },
    'Ahroun': {
        'Cliath': ['FällendeBerührung', 'Inspiration', 'Rasiermesserklauen', 'Rudeltaktiken', 'Spornklauen'],
        'Pflegling': ['Kampfgeist', 'Silbergespür', 'WahreFurcht', 'Zornschild'],
        'Adren': ['HerzderWut', 'Kampfheilung', 'Silberklauen', 'Windklauen'],
        'Athro': ['AnfachenderbrennendenWut', 'EisernerKiefer', 'Körperveränderung', 'LichtdesVollmondes'],
        'Ältester': ['KussdesHelios', 'Willensstärke'],
        'Legende': ['UnaufhaltsamerKrieger'],    },
    'Ragabash des Wyrms': {
        'Cliath': ['Verleihen des Raubtierschattens'],
        'Pflegling': [],
        'Adren': ['Berührung des Aals'],
        'Athro': ['Kassandras Segen', 'Silberne Vergeltung',],
        'Ältester': ['Geduld des Wyrms', ],
        'Legende': []},
    'Theurge des Wyrms': {
        'Cliath': [],
        'Pflegling': ['Tausend Stimmen', 'Vergifteter Todesgürtel'],
        'Adren': ['Festmahl der Essenz', ],
        'Athro': [],
        'Ältester': [],
        'Legende': ['Präludium zur Apokalypse', ]},
    'Philodox des Wyrms': {
        'Cliath': ['Säurekrallen'],
        'Pflegling': ['Angst riechen', ],
        'Adren': [],
        'Athro': [],
        'Ältester': ['Omenklauen', ],
        'Legende': []},
    'Galliard des Wyrms': {
        'Cliath': [],
        'Pflegling': ['Verbündete aus der Tiefe', 'Heulen des Jägers', 'Schatten des Impergiums'],
        'Adren': [],
        'Athro': ['Geheul des Todes', ],
        'Ältester': ['Wahnsinn'],
        'Legende': []},
    'Ahroun des Wyrms': {
        'Cliath': ['Säurekrallen'],
        'Pflegling': ['Hörner des Pfählers ', 'Teerschatten',],
        'Adren': ['Schmerz in den Eingeweiden', ],
        'Athro': [],
        'Ältester': ['Unbegrenzte Stärke', ],
        'Legende': []},
}
StammGabenNamen = {
    'Fianna': {
        'Cliath': ['Feenlicht', 'Giftwiderstehen', 'Hasensprung', 'Überzeugungskraft', 'Giftwiderstehen', 'ZweiZungen'],
        'Pflegling': ['Flammentanz', 'GeheulderTodesfee', 'GeheuldesUnsichtbaren', 'HerrschaftüberdieGestalt', 'Schlangenzunge'],
        'Adren': ['Feenverwandte', 'Gegenstandumformen', 'Glückskind', 'Leylinien', 'Sirenengesang'],
        'Athro': ['BalorsBlick', 'Trugbild'],
        'Ältester': ['GabedesSpriggans', 'NebelüberdemMoor', 'RufderWildenJagd'],
        'Legende': []},
    'Glaswandler': {
        'Cliath': ['Diagnose', 'EinfacheMaschinekontrollieren', 'PlugandPlay', 'Trickschuss', 'Überzeugungskraft'],
        'Pflegling': ['Cybersinne', 'HändevollerDonner', 'Spannungsspitze', 'Stahlfell', 'Technologiestören'],
        'Adren': ['Eindringen', 'Elektroschock', 'Elementargunst', 'KomplexeMaschinekontrollieren'],
        'Athro': ['Doppelgänger', 'Einstimmung', 'Funkwellenreiter', 'Technobabbel'],
        'Ältester': ['Netzspinnebeschwören', 'OrdnungimChaos'],
        'Legende': []},
    'Kinder Gaias': {
        'Cliath': ['Barmherzigkeit', 'BerührungderMutter', 'GeruchdesBruders', 'Schmerzwiderstehen', 'Waffeblockieren'],
        'Pflegling': ['ArsenaldesEinhorns,Namen.BerührungderGroßmutter', 'LunasRüstung', 'ParaBellum', 'Ruhe'],
        'Adren': ['BeruhigendeswildenTieres', 'Geisterfreund', 'LiebendeBerührung', 'Überwältigen'],
        'Athro': ['FreiwiederWindseitdemerstenTag', 'Gelassenheit', 'SchlaginsLeere', 'Tierleben'],
        'Ältester': ['Korona', 'DerlebendeWald'],
        'Legende': []},
    'Knochenbeißer': {
        'Cliath': ['Giftwiderstehen', 'Kochen', 'KraftderVerzweiflung', 'SchätzeimMüll', 'SüßerHonigduft'],
        'Pflegling': ['AbscheulicherGestank', 'Hundetarnung', 'IndenRitzen', 'SeligeUnwissenheit'],
        'Adren': ['WildheitderindieEckegedrängtenRatte', 'GabederTermite', 'GabedesStinktiers', 'Gegenstandumformen', 'LachenderHyäne', 'Rostruf'],
        'Athro': ['Blinzeln', 'Einstimmung', 'Verseuchen'],
        'Ältester': ['Aufstand', 'Überlebenskünstler'],
        'Legende': []},
    'Nachfahren des Fenris': {
        'Cliath': ['BlitzschnelleReflexe', 'FratzedesFenris', 'HerrüberdasFeuer', 'Rasiermesserklauen', 'Schmerzwiderstehen'],
        'Pflegling': ['FängedesNordens', 'DieFluchtdesFeiglingshemmen', 'KnurrendesRaubtiers', 'Trollhaut'],
        'Adren': ['Giftblut', 'Schmerzumleiten', 'ThorsMacht'],
        'Athro': ['FelsinderBrandung', 'GaiasSchrei', 'HerzdesBerges', 'Körperveränderung'],
        'Ältester': ['FenrisBiss', 'HeimdallsAusdauer', 'WalhallasHorden'],
        'Legende': ['Fenrisrufen']},
    'Rote Klauen': {
        'Cliath': ['AugedesJägers', 'GeruchdesfließendenWassers', 'Tiersprache', 'VerborgenerMörder', 'WölfevordenToren'],
        'Pflegling': ['Beutegespür', 'NächtlichesGeheul', 'TierischeInstinkte', 'SchattendesImpergiums'],
        'Adren': ['Elementargunst', 'PfadloseEinöde', 'Revier', 'Zerlegen'],
        'Athro': ['GeheuldesTodes', 'Schlingen', 'Treibsand'],
        'Ältester': ['GaiasRache', 'LykaonsFluch', 'Schorfwandlerfluch'],
        'Legende': ['GaiasSchild']},
    'Schattenlords': {
        'Cliath': ['AuraderZuversicht', 'LauscheranderWand', 'Schattenweben', 'TödlicheSchwäche', 'ZüngleinanderWaage'],
        'Pflegling': ['Donnerschlag', 'KühleStimmederVernunft', 'LiedderErdmutter', 'LunasRüstung', 'NächtlichesGeheul'],
        'Adren': ['EiseskältederVerzweiflung', 'LähmenderBlick', 'LenkendesSturms', 'Schattenschnitt', 'UnterDruck'],
        'Athro': ['Haft', 'StärkedesBeherrschers', 'OffeneWunden'],
        'Ältester': ['Gehorsam', 'Schattenrudel'],
        'Legende': []},
    'Schwarze Furien': {
        'Cliath': ['AtemderWyldnis', 'Männergestalt', 'GeschärfteSinne', 'WyldeRegeneration', 'Wyrmgespür'],
        'Pflegling': ['Beutegespür', 'FluchdesAeolus', 'HerrschaftüberdieGestalt', 'KalisZunge', 'Knien'],
        'Adren': ['Gnadenstoß', 'Herzklaue', 'SchmerzindenEingeweiden', 'SchwingendesPegasus'],
        'Athro': ['Qualenbereiten', 'Tierleben', 'Wespenklauen'],
        'Ältester': ['Gorgonenblick', 'TausendGestalten', 'Wyldnisverformung '],
        'Legende': []},
    'Silberfänge': {
        'Cliath': ['Falkenauge', 'GriffdesFalken', 'Inspiration', 'Wyrmgespür', 'ZüngelndeFlamme'],
        'Pflegling': ['EinheitdesRudels', 'Empathie', 'Handklinge', 'LunasRüstung', 'Silbergespür'],
        'Adren': ['Falkenklauen', 'Flammenklinge', 'GaiasZorn', 'Silberklauen'],
        'Athro': ['DemTodausweichen', 'GeistigeBarriere', 'Meisterschaft'],
        'Ältester': ['LunasRächer', 'PfotendesneugeborenenWelpen'],
        'Legende': ['ErneuerungdesZyklus']},
    'Sternenträumer': {
        'Cliath': ['EiserneEntschlossenheit', 'FällendeBerührung', 'Gleichgewicht', 'Kanalisieren', 'Wyrmgespür'],
        'Pflegling': ['EinstimmungaufdieOberfläche', 'InnereKraft', 'InneresLicht', 'Versuchungwiderstehen', 'Wuxing'],
        'Adren': ['Gleichgewichtsgespür', 'GnadedenBesiegten', 'Klarheit', 'WiederkehrendeGunstdesWindes'],
        'Athro': ['GeistigeBarriere', 'SchlaginsLeere', 'ÜbernatürlichesBewusstsein'],
        'Ältester': ['HarmonischeEinheitdersmaragdenenMutter', 'Schlägeumlenken'],
        'Legende': ['WeisheitdesSehers']},
    'Stillen Wanderer': {
        'Cliath': ['OrientierungamHimmel', 'Wyrmgespür', 'Stille', 'Gedankenschnelle', 'VisionenvomDuat'],
        'Pflegling': ['AxisMundi', 'SeligeUnwissenheit', 'AusdauerdesBoten', 'Weltsprache', 'AufSebeksRücken'],
        'Adren': ['Anpassung', 'DergroßeSprung', 'MaldesTodeswolfs', 'Unnatürlichesfühlen'],
        'Athro': ['Einstimmung', 'SchwarzesMal', 'EindämmenderHerzflut', 'UnvorstellbareSchnelligkeit'],
        'Ältester': ['Mondtor', 'Umbraerreichen'],
        'Legende': []},
    'Uktena': {
        'Cliath': ['Echsengeist', 'Geistersprache', 'Magiegespür', 'Verhüllen', 'Wyrmgespür'],
        'Pflegling': ['WindungenderSchlange', 'Fetischruf', 'GeistdesFisches', 'GeistdesVogels', 'SchattenimMorgengrauen'],
        'Adren': ['Nebelketten', 'Totembannen', 'Unsichtbarkeit', 'Wahrsagen', 'ZerreißenderKunst'],
        'Athro': ['Elementarrufen', 'Haft', 'HandderErdherren'],
        'Ältester': ['Fetischpuppe', 'GewebedesGeistes'],
        'Legende': []},
    'Wendigo': {
        'Cliath': ['Briserufen', 'Eisecho', 'SchlagderHerztrommel', 'Schmerzwiderstehen', 'Tarnung'],
        'Pflegling': ['FängedesNordens', 'MitdenWindgeisternsprechen', 'SchneidenderWind', 'WahreFurcht', 'WieeinLachsimWasser'],
        'Adren': ['BlutdesNordens', 'BlutigeLabsal', 'Himmelslauf', 'WeisheitderAltenWege'],
        'Athro': ['FelsinderBrandung', 'GaiasSchrei', 'Kannibalengeistrufen', 'KältedesfrühenFrostes'],
        'Ältester': ['HerzausEis', 'Sturmgeisterbeschwören'],
        'Legende': []},
    'Tänzer der schwarzen Spirale': {
        'Cliath': ['Gift widerstehen','Schutzplage','Schmerz widerstehen','Verhüllen','Wyrmgespür','Baalsrüstung','Spiralschattentanz','Makel unterdrücken','Baalsaura'],
        'Pflegling': ['Fledermausohren','Wyrmhaut','Grabesklauen','Verborgener Mörder','Unterwerfen'],
        'Adren': ['Flughäute','Schäumende Wut','Schöne Lüge','Klauen der Korrosion','Ichorklinge','Gabe des Befleckten Totems'],
        'Athro': ['Wyrmelementar  beschwören','Schleichendes  Gift','Offene Wunden','Hungriger Rost','Gestohlene Haut','Das  Weiße  Heulen','Geheul der Plage'],
        'Ältester': ['Baalsfeuer','Makel tarnen','Mantel von Anthelios'],
        'Legende': []}}
FomoriGabenName = {
    'Andersicht','An der Wand entlang','Augen des Wyrms','Ballenpolster','Berserker','Betäubung','Chamäleonfärbung','Dunkelsicht','Echo des Zorns','Ektoplasmaausstülpung','Erhöhte Geschwindigkeit','Exoskelett','Feurige Entladung','Flügel','Froschzunge','Gabe','Gaiagespür','Gasform','Gebrüll des Wyrms','Gefährlicher Auswurf','Gefährlicher Odem','Gepanzerte Haut','Geisterbande','Geruch der Triade','Gewandtheit','Gezahnte Körperöffnung','Gifthauch','Giftiger Biss','Giftiges Miasma','Giftige Tumore','Größenveränderung','Hirnfresser','Höllenhaut','Homogenität','Immunität gegen das Delirium','Infektiöse Berührung','Klauen und Fänge','Körper der Fäulnis','Körpererweiterung','Körpersporne','Krebsartiger Körperpanzer','Magenpumpe','Mega-Attribut','Molekulare Schwächung','Panzerhaut','Peitschender Schwanz','Phönixfeuer','Pilzeuter','Plasmagestalt','Rattenkopf','Schattenspiel','Schlangenhaut','Schleimschicht','Schlund des Wyrms','Seitwärtsschritt','Selbstheilungskraft','Spinndrüse','Stimme des Wyrms','Synapsenüberladung','Täuschung','Teerbaby','Tierherrschaft','Toxische Sekrete','Übernatürliche Stärke','Ungeheure Mutation','Unnatürliches spüren','Verdrehte Sinne','Wahnsinn verursachen','Wasser atmen','Weichmacher','Zornige Schmähung','Zusätzliche Gliedmaßen',
}

def LookUpTexteByName(needle):
    for gabe in gabenTexte['alleGabenTexte']:
        if gabe['name'].replace(' ','') == needle.replace(' ',''):
            return gabe
    return {'name':needle,'fluffText':'nicht gefunden','systemText':'nicht gefunden'}

def GetGaben(Brut,Vorzeichen,Stamm,Rang='Cliath'):
    result = []
    for i in range(len(Ränge)):
        RangIdx = Ränge[i]
        if Stamm=='Tänzer der schwarzen Spirale':
            for gabenName in BrutGabenNamen[Brut+' des Wyrms'][RangIdx]:
                result.append(LookUpTexteByName(gabenName))
            for gabenName in VorzeichenGabenNamen[Vorzeichen+' des Wyrms'][RangIdx]:
                result.append(LookUpTexteByName(gabenName))
            for gabenName in StammGabenNamen[Stamm][RangIdx]:
                result.append(LookUpTexteByName(gabenName))
        else:
            for gabenName in BrutGabenNamen[Brut][RangIdx]:
                result.append(LookUpTexteByName(gabenName))
            for gabenName in VorzeichenGabenNamen[Vorzeichen][RangIdx]:
                result.append(LookUpTexteByName(gabenName))
            for gabenName in StammGabenNamen[Stamm][RangIdx]:
                result.append(LookUpTexteByName(gabenName))
        if RangIdx == Rang:
            break
    return {gabe['name']:{'fluffText':gabe['fluffText'],'systemText':gabe['systemText']} for gabe in result}

def GetFomorGaben():
    result = [LookUpTexteByName(gabenName) for gabenName in FomoriGabenName]
    return {gabe['name']: {'fluffText': gabe['fluffText'], 'systemText': gabe['systemText']} for gabe in result}










