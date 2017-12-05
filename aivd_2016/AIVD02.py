# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 22:13:06 2016

@author: evehaa
"""

import itertools

elements = ['AR', 'K', 'TI', 'NI', 'TA', 'AM']
#elements = ['B', 'N', 'AL', 'S', 'IN', 'TE', 'I', 'ER']

with open('AIVD02.txt', 'w') as f:
    for subset in itertools.permutations(elements, 6):
        f.write(str(subset).replace(' ','').replace('(', '').replace(')', '').replace('\'', '').replace(',', '') + '\r\n')