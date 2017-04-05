# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 18:55:07 2017

@author: evehaa
"""


from cryptography import Cryptography


message = 'GEVTNFI IOMW MJJGGQHIBRDOP QFMUXLHSD JB UZ YNDXXN WCKD' 
key = 'zyxwvutsrqponmlkjihgfedcba'
#'honderdtachtig graden'
#'honderdtachtig'
#'omgedraaid'
#'omgekeerd'
#'terug'
#'ondersteboven'
#'achterstevoren'

crypt = Cryptography()
crypt.set_encoded_text(message)
print(crypt.decode_vigenere(key))

for i in range(0,26):
    print(crypt.decode_rotation(i))