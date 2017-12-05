# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 23:51:35 2017

@author: evehaa
"""

from cryptography import Cryptography


message = 'NZR NNFVYT QJG IWQN IQFLLNJQ' 

crypt = Cryptography()


# Text 2
message = 'NZR NNFVYT QJG IWQN IQFLLNJQ'
key = 'johan cruijff'
crypt.set_encoded_text(message)
print(2, crypt.decode_vigenere(key))


# Text 3
message = 'XS UOOH VSH DOG NWSB OZG XS VSH RCCF VSPH'
crypt.set_encoded_text(message)
print(3, crypt.decode_rotation(14))


# Text 5
message = 'VROPRIDGIVDLWSEHVANBIVRWRWVAASIGMXCVOVRTQDPWPEECSZAIIROADMECANRT'
key = ''
crypt.set_encoded_text(message)
print(5, crypt.decode_playfair(key))


# Text 6
message = 'RM ELVGYZO RH SVG HRNKVO: QV YVMG LU LK GRQW LU QV YVMG GV OZZG. ZOH QV GV OZZG YVMG, NLVG QV ALITVM WZG QV LK GRQW EVIGIVPG' 
key = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
crypt.set_encoded_text(message)
print(6, crypt.decode_monoalphabetic(key))



citations = [
    "Als wij de bal hebben, kunnen hun niet scoren.",
    "Voetballen is simpel. Het moeilijkste wat er echter is, is simpel voetballen.",
    "Kijk, de bal moet minimaal tussen die twee palen.",
    "Als je de eerste goal scoort, win je de wedstrijd.",
    "Als je sneller wilt spelen kun je wel harder lopen, maar in wezen bepaalt de bal de snelheid van het spel.",
    "Voetbal is een spel van fouten. Wie de minste fouten maakt, wint.",
    "Voordat ik een fout maak, maak ik die fout niet.",
    "Je gaat het pas zien als je het door hebt.",
    "Als je ergens niet bent, ben je óf te vroeg óf te laat.",
    "Elk nadeel heb zijn voordeel.",
    "Als je een speler ziet sprinten, is hij te laat vertrokken.",
    "Je moet schieten, anders kun je niet scoren.",
    "Italianen kennen niet van je winnen, maar je ken wel van ze verliezen.",
    "In voetbal is het simpel: je bent óf op tijd óf je bent te laat. Als je te laat bent, moet je zorgen dat je op tijd vertrekt.",
    "Je moet altijd zorgen dat je een doelpunt meer scoort als de tegenstander.",
    "Wat is snelheid? Vaak verwisselt de sportpers snelheid met inzicht. Kijk, als ik iets eerder begin te lopen dan een ander, dan lijk ik sneller.",
    "Zonder de bal kun je niet winnen.",
    "Je moet een gat voor je laten vallen en er dan zelf inlopen.",
    "Als je op balbezit speelt, hoef je niet te verdedigen, want er is maar één bal.",
    "Kijk, de bal is een essentieel onderdeel van het spel.",
    "Als Italianen één kans krijgen, maken ze er twee.",
    "Italië heb een paar hele goeie voetballers, maar die moet je dan wel de bal spelen, zodat ze kunnen voetballen.",
    "Ik heb nog nooit een zak geld een goal zien maken."
]
for cit in citations:
#    print(len(cit.replace(' ','').replace(',','').replace('.','')), cit)
    for word in cit.split(' '):
        if len(word) == 8 and word[5] == 'u':
            print(word, cit)
    