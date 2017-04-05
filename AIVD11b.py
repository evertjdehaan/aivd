# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 19:19:49 2017

@author: evehaa
"""

from cryptography import Cryptography

crypt = Cryptography()
print(crypt.decode_polybius([[1,3], [0,4], [3,3], [3,2], [0,4], [0,4], [2,2], [4,0], [2,3], [3,4], [0,3], [1,3], [1,1], [3,2], [2,3], [2,1], [2,3], [2,4], [0,0], [0,3], [0,4], [2,1], [3,3], [0,4], [0,2], [2,3], [2,1], [0,4], [2,2]]))