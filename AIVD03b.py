# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 22:13:06 2016

@author: evehaa
"""

from getwords import getwords

allwords = getwords(minlen=5, maxlen=5)

with open('AIVD03b.txt', 'w') as f:
    for w in allwords:
        if (w[0] == w[3]) and (w[1] == w[2]):
            f.write(w + '\r\n')
