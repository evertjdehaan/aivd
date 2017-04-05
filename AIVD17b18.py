# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 22:13:06 2016

@author: evehaa
"""

from getwords import getwords

allwords = getwords(minlen=3, maxlen=8)

greens = []
green_vals = [2, 5, 8, 11, 14, 17, 20, 23, 26]
for i1 in green_vals:
    for i2 in green_vals:
        for i3 in green_vals:
            for i4 in green_vals:
                if (i1+i2+i3+i4) == 47:
                    greens.append("{}{}{}{}".format(
                        chr(i1+64), chr(i2+64), chr(i3+64), chr(i4+64)))
                            
print(len(greens))
i = 0
j = 0                
with open('AIVD17b18.txt', 'w') as f:
    for green in greens:
        j += 1
        permutation = ('s'+green[0]+'u'+green[1:4]).lower()

        if (i % 500) == 0:
            print('{:.2f}\t{}'.format(j/len(greens), permutation))
        i += 1

        for w in allwords:
            if w in permutation:
                f.write(w + '\t\t' + permutation + '\r\n')
