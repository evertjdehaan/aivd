# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 18:02:24 2016

@author: evehaa
"""

from getwords import getwords

allwords = sorted(getwords())

with open('AIVD12.txt', 'w') as f:
    for w in allwords:
        if 'y' in w:
            f.write(w + '\r\n')