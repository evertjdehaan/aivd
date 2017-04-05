# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:06:59 2017

@author: EVEHAA
"""

from cryptography import Cryptography


message = 'ANLNISUEWHTINSJECDNOENRBUEAKNLNHEEBB' 
key = 14
crypt = Cryptography()
crypt.set_encoded_text(message)
dec = crypt.decode_rail_fence(key)
print(dec)
crypt.set_decoded_text(dec)
print(crypt.encode_rail_fence(key))
print()


message = 'TMAVFEKUOBOBRNRSEVVALCYAVNMAMASSWETIC'
key = "VEERTIEN"
crypt = Cryptography()
crypt.set_encoded_text(message)
dec = crypt.decode_bifid(key)
print(dec)
crypt.set_decoded_text(dec)
print(crypt.encode_bifid(key))
print()


message = 'konijn'
crypt = Cryptography()
crypt.set_decoded_text(message)
result = crypt.encode_morse()
print(result)
print(result.count('.'))
print(result.count('-'))
print()


message = 'NZR NNFVYT QJG IWQN IQFLLNJQ'
key = 'johan cruijff'
crypt.set_encoded_text(message)
dec = crypt.decode_vigenere(key)
print(dec)
crypt.set_decoded_text(dec)
print(crypt.encode_vigenere(key))
print()



message = 'Evert de Haan is een rare aap. Waarom kijkt hij toch naar Ziggo Sport?'
rotation = 12
crypt.set_decoded_text(message)
enc = crypt.encode_rotation(rotation)
print(enc)
crypt.set_encoded_text(enc)
print(crypt.decode_rotation(rotation))
print()



message = 'Lyanne Wilts is een heel erg lieve meid! Wanneer is ze klaar met fietsen?'
key = 'Mischa Vermeer'
crypt.set_decoded_text(message)
enc = crypt.encode_monoalphabetic(key)
print(enc)
crypt.set_encoded_text(enc)
print(crypt.decode_monoalphabetic(key))