# -*- coding: utf-8 -*-
'''
Created on Mon Jan  9 10:20:54 2017

@author: evehaa
'''

needles = ['Jan Smit', 'Jan', 'Smit', 1979,
           'Ik zing dit lied voor jou alleen', 'Kerstmis met Jantje Smit', 'Het land van mijn dromen', 'Jantje Smit', 'Jan Smit 2000',
           'Zing en lach', 'Zonder jou', 'Op eigen benen', 'jansmit.com', 'Op weg naar geluk', 'Stilte in de storm', 'Leef',
           'Vrienden', 'Jij & ik', 'Kerst voor iedereen', 20, 
           'Ik zing dit lied voor jou alleen', 'Pappie, waar blijf je nou?', 'Ave Maria', 'Het land van mijn dromen', 'O sole mio',
           'Eens zit het leven je weer mee', 'Puik idee ballade', 'Zing en lach en leef je uit', 'Op eigen benen', 'Als de nacht verdwijnt (live)',
           'Vrienden voor het leven', 'Als de nacht verdwijnt (live)', 'Boom Boom Bailando', 'Laura', 'Hoe kan ik van je dromen',
           'Als de morgen is gekomen', 'Cupido', 'Op weg naar geluk', 'Dan volg je haar benen', 'Calypso', 'Stilte in de storm', 'Als je lacht',
           'Je naam in de sterren', 'Leef nu het kan', 'Terug in de tijd', 'Zie wel hoe ik thuis kom', 'Niemand zo trots als wij',
           'Hou je dan nog steeds van mij', 'Dromen', 'Echte vrienden', 'Zingen lachen dansen', 'Altijd daar', 'Sla je armen om me heen',
           'Hoop, liefde en vertrouwen', 'Leeg om je heen', 'To All the Girls I\'ve Loved Before', 'Nederland wordt kampioen!', 'Jij & ik',
           'Handen omhoog', 'Recht uit m\'n hart', 'Duizend en één nacht', 'Kleine superster', 'Kom dichterbij me'
]

questions = [
    'Woordreeksen, het traditionele begin. Wat is een passende afsluiting van deze reeks? START, ASTER, STIER, INERT, DINER, Welk getal past op de plaats van het vraagteken en wat is het woord? KEUZEVAK, MARKEREN, KANSSPEL, TROTTOIR, GEMURMEL, HANENKAM, NAVRAGEN',
    'Elementair: wie valt in dit gezelschap uit de toon',
    'Laatste vragen van 2016? Om wie gaat het hier? T, OTO, OO ND JU, NG , CBT, YOU T, T TT Zeven codes met een verband. Wat waren de oorspronkelijke teksten? TCJN, XDAAW MNZLYOMN, ACN AQISJWQ, JQ SOT WDPNE HJNNQ EDWC, QLMJR KOODSY, CIICP, PQTQKJG QJ PQTQKJG. Zes sleutels, zes sleutelwerken. Wat waren de oorspronkelijke teksten? ER IUUH VUI ER NJJP NHHQ PE SNMTVMBEIS ZHSQ HJ DULF RSUO VFR FQ RP DEKB UMMP UFPBFKFE VMMIL? WMMQPTTH WMMQVJJQ OCUIQIRRI',
    'Kun je het volgende getal in elk van deze reeksen geven? 2, 2, 3, 6067, 97, 7, 499, 7, 5, 2, 631, 5, 7, 89, 47, 3',
    'Een aantal landenreeksen. Waar past NEDERLAND in de volgende reeks? IERLAND, ZWEDEN, VERENIGD KONINKRIJK, FRANKRIJK, LUXEMBURG, ISRAEL, DENEMARKEN, NOORWEGEN, DUITSLAND Waar past NEDERLAND in de volgende reeks? MALTA, PORTUGAL, LUXEMBURG, BELGIE, SPANJE, ITALIE, POLEN, FRANKRIJK, DUITSLAND',
    'Voor een feestje waren DJT, FDMH en JMK uitgenodigd, net als J-PS, JFS en BLF, YO, JMS, en OH en BH. Wie was verhinderd?',
    'Rotaties kunnen verdraaid lastig zijn. Bij a begint het met ongeveer 13,85° en bij b wordt geroteerd met 180°. Wat staat hier? XBU CFHPO BMT FFO SVUVKIG TQVDWLH ZPTVR OXAMDYVD LNA OX KDDGO GEVTNFI IOMW MJJGGQHIBRDOP QFMUXLHSD JB UZ YNDXXN WCKD',
    'Aardrijkskunde dan: vier categorieën met ieder zeven elementen. Wat zijn de vier categorieën? CGTGIGPDGM, DAFAIHJCHNK, DGPKBPOAS ZSS, DIOOIOOIJJI, DQMMLYGLMCIFE, FASUW-IUAFSG, FGTJMGHSSN, FIVC, GBSXGFTSMSABGFT, HFYX, HGKJGHBUH, IKUJQ VAJPKJ, IMHHQ-RMAQQGFFAS, IMHSFBGFT, LDLZHFS, LUJGHD CHYH, QBQBOGOGHSSN, RHMFSH, RJVSIHSSN, STJHFA, SYNSHSSN, TFONKTP, TVTNTPQ, VBOQJNBGHSSN, VJPQJDHSSN, VLFEPOSBILFE, VUUMBGFT, WHCEL',
    'Gegeven is BONNETJE = WAARBORG, BURGERGEZIN = THEATERVORM en FRAMBOZENBOS = FRAMBOZENBOS. Wat zijn nu de volgende woorden? BERGFAZANT, BERGRIVIER, BESPEURING, BIOGRAFEN, GRANATEN, OVERTRAINEN, VANMORGEN, WAARVOOR',
    'En nu iets heel anders. Twee personen op een veerboot doden de tijd door twee rijen te vergelijken. Een telt verschillen, de ander overeenkomsten. Ze komen tot de volgende getallenreeksen. 0 1 1 0 0 0 0 1 1 1 3 0 1 ..... 2 2 2 1 3 1 4 2 3 3 2 3 6 ..... Wat is het volgende getal in ieder van de reeksen?',
    'Nu iets eenvoudigs om op adem te komen. Wat staat hier?',
    'Bij de volgende reeksen is het uitgangspunt een aantal woorden met een gemeenschappelijk thema. Voor alle woorden samen is geteld welke letters hoe vaak voorkomen. Van elke van het aantal resulterende letters is vervolgens het aantal overeenkomstige letters uit het gemeenschappelijk thema afgetrokken. Van de letters die niet als resultaat 0 hebben zijn de frequenties weergegeven. Als voorbeeld, stel dat het thema SPEELKAART is en de woorden zijn RUITEN, HARTEN, SCHOPPEN, KLAVEREN, dan geeft dit als resultaat: C1 E3(=5-2) H2 I1 N4 O1 P1 R2 T1 U1 V1 (De A ontbreekt omdat die twee keer in het thema en ook twee keer in de woorden voor komt.) Wat is het thema van de volgende rijen?  A1 D1 E2 F1 G1 H1 I2 J1 N6 Ö1 R2 T1 Y1 −1  A5 B5 C1 E11 F1 G1 I6 J3 K1 L2 M4 N2 O3 P2 R9 S3 T4 U7 V1  A2 D2 E3 G1 I3 J1 L3 N2 O4 R2 T1 U1 V1 W1',
    'Elk van de woorden LAMP, PAKSOI, MUIS en GRIJS past in de volgende figuur. Welke woorden kunnen ze vervangen?',
    'Voor deze puzzel geldt: als je het antwoord gevonden hebt, dan is de opgave niet moeilijk meer. Daarom hoeven we het antwoord niet te weten, dat kun je verticaal schrijven. Wel graag de onvercijferde woorden 1 tot en met 7 in de puzzel. IG ZNBNPN ZIG ONG IB WJJPQHUIFGDIFB KGQSNPCNDIFB NZR NNFVYT QJG IWQN IQFLLNJQ XS UOOH VSH DOG NWSB OZG XS VSH RCCF VSPH ANLNISUEWHTINSJECDNOENRBUEAKNLNHEEBB VROPRIDGIVDLWSEHVANBIVRWRWVAASIGMXCVOVRTQDPWPEECSZAIIROADMECANRT RM ELVGYZO RH SVG HRNKVO: QV YVMG LU LK GRQW LU QV YVMG GV OZZG. ZOH QV GV OZZG YVMG, NLVG QV ALITVM WZG QV LK GRQW EVIGIVPG TMAVFEKUOBOBRNRSEVVALCYAVNMAMASSWETIC',
    'Allemaal titels. Welke? 1350, -89, -140, -123, -86, -194, -90, -156, 221, -192, -58, -25, -122, 89, 31, -179, 172 W/NW NW/NO N/NW Z/Z NW/W ZW/ZO Z/Z NW/N ZW/W Z/NO Z/Z O/NO NW/ZW NO/ZW NO/Z NW/O Z/Z NO/O ZW/NW ZO/ZW Z/N O/NW Z/Z O/ZW W/NW NW/W O/W W/ZO Z/Z O/NO Z/NO N/Z Z/Z W/O W/NW NO/ZW ZW/NO Z/Z ZW/Z ZO/ZW Z/N Z/Z Z/O Z/ZW NO/ZW ZW/NO Z/Z ZW/NW ZW/ZO Z/Z ZO/Z O/W Z/NO NO/Z ZW/ZO Z/Z TEES IMDO EJDR JPET RIEE PASE LBTR ETDT CNEW TODE IKSE ISRD SWEE',
    'Tevergeefs probeerden de puzzelmakers een boodschap te ontvangen, er zat helaas te veel ruis op de lijn. De verzender heeft het vijf keer geprobeerd, maar steeds werd een groot deel van de letters verkeerd ontvangen. Wat is de verzonden tekst? MKEICEFBYSDEXGNSNLGALZLDUOVKGSNANNJIHCVCLAWNEIHANEOLMISSPHVBHKKNEIKSA NIJNNORBYNNNOTINIWKAIZLZUHTKIXNANJUZLISRLEWNEZHDNNONMIWORHIEHCALEIKEA MKJIVORMISNLOTKNNLKAQSQZCHTTISLABJILLIECEAUNESHDYJTNJYWXWEVTHBAWADFEA MEEDVORBLNNITGIYILGEOSOECOTEUSNENNNLLIERLAUNOSQANNONJUWSTEIEHBECYASEA MUFINEXBISBINGKNXMKALYLECXTKUNLPRNJUHCSCEERDRSHZNNTNMISSCHETRCEREISLN',
    'Typisch NBV? Nijver hebben de puzzelaars een drietal citaten weten te verbergen. Van wie zijn de onderstaande citaten?',
    'Enkele rijtjes. Welke plant kan volgen? EZELEN, SPONS, SLOPEN, KETEN, LOOTJE, BELDEN, ERKERS, ? Welk getal volgt? RUTJF, TVOF4S, TT, CB, E, CAD, TGE, TBA, C, LSA, DAP, GB, B, L, SOTT, P, ATWIAD, PR, ?',
    'Nog meer rijtjes. Wat zijn (1) en (2)? F, G, NB, (1), O, (2), G, Z, D, F, L, U Wat zijn (1) en (2)? UH, (1), SV, (2), W, L, DB, A, L, H, Z, ... Even helemaal een andere kant op denken. Wat zijn (1) en (2)? A, T, C, M, (1), A, N, C, O, W, M, M, U, I, (2), ...',
    'Ja, natuurlijk ook dit jaar een creativiteitsopgave. Maak een tekst waarin één letter precies 1x voorkomt, een andere letter precies 2x voorkomt, weer een andere letter precies 3x voorkomt, etc. Voorbeeld: KAAS IS SAAI Met vier verschillende letters: 1 x K, 2 x I, 3 x S en 4 x A. Iedere inzending met minimaal zes verschillende letters krijgt de volledige punten. Als de puzzelmakers een oplossing heel mooi vinden dan kunnen ze bonuspunten toekennen.',
    'Ach, van welke man maakt de naam het erg verduveld lastig? DRUG JARIG NIKS ACHT ARCHIEVEN MELKERS DOLHEDEN NEVEL ZO HORIGE SCHOLIER STRUIF DRAAK MORSE REM HYGIËNE INRUIL OHMS RUIT TENDENS UIL HERSEN NICHT RAMP DAVEREND KOUDE OVEN GOUD IRIS KLEINKINDEREN',
    'Natuurlijk dit jaar ook een associatievraag. Een reinigingshandeling van een vrouw (a), verbonden worden met een meubelstuk (b) resulterend in een verknipte man (c) en een gebouw bij een galgenveld in Londen (d) leiden tot een religieuze uitroep (e). Bij welke trieste gelegenheid bestaat deze opgave?',
    'Sequenties. Wat zijn de volgende drie items in onderstaande lijsten? V, G, C, R, D, J, F, Z, I, A, N, H, B, ?, ?, ? 3, 22, 1, 9, 17, 10, 21, 27, 23, 55, 66, 89, 5, ?, ?, ?',
    'Met deze teksten kun je hopelijk de volgende vragen beantwoorden door de puzzels in de onderstaande boodschappen op te lossen. Wat is de som? Waar staan de torens? Om hoeveel ringen gaat het?',
    'In elk van de onderstaande reeksen is iets mis gegaan. De oorspronkelijke reeksen zijn alfabetisch en gerelateerd. Opgave c is voor de handige puzzelaar want daar is twee keer iets mis gegaan: eerst zoals bij a en vervolgens zoals bij b. Wat zijn de oorspronkelijke reeksen? APPELTAART, CHOCOLADESAUS, CITROENSAP, HAGELSLAG, KERSENJAM, MARINEREN, TARWEBLOEM, ZALMFILET POOT, STER, GOEROE, HOORN, BORST, PAD, EEUW REDENERING, ZEER, JACHT, ZORG, VRUCHT, TEKENAAR, DEN, GOM',
    'Traditioneel de laatste vraag, nu bijna. Wat staat hier? ARE AMPERE NOORD GENESIS AMPLITUDEMODULATIE EERSTKOMENDE ERBIUM SECONDE TELLUUR NEON EUROPESE NORM ZUID ORGANISATIE ELEKTRONISCHE LEEROMGEVING OHM ZWAVEL MILIMETER KUS VETERANENINSTITUUT JODIUM'
]

for key, val in enumerate(questions):
    haystack = val.replace(' ', '').replace(',', '').replace('?', '').replace('.', '').lower()
    for needle in needles:
        needle = str(needle).replace(' ', '').replace(',', '').replace('?', '').replace('.', '').lower()
        if needle in haystack:
            print('{}\t\t{}\t{}'.format(needle, key, val))
           
print('------------------------------------')           
           
for key, val in enumerate(questions):
    haystack = val.replace(' ', '').replace(',', '').replace('?', '').replace('.', '').lower()
    all_in_hay = True
    for letter in 'jansmit':
        if letter not in haystack:
            all_in_hay = False
            
    if all_in_hay:
        print(key)