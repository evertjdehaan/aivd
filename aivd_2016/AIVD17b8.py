# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 22:13:06 2016

@author: evehaa
"""

from getwords import getwords

allwords = getwords(minlen=4, maxlen=9)


reds = []
red_vals = [1, 4, 7, 10, 13, 16, 19, 22, 25]
for i1 in red_vals:
    for i2 in red_vals:
        for i3 in red_vals:
            for i4 in red_vals:
                if (i1+i2+i3+i4) == 46:
                    reds.append("{}{}{}{}".format(
                        chr(i1+64), chr(i2+64), chr(i3+64), chr(i4+64)))
greens = []
green_vals = [2, 5, 8, 11, 14, 17, 20, 23, 26]
for i1 in green_vals:
    for i2 in green_vals:
        for i3 in green_vals:
            for i4 in green_vals:
                if (i1+i2+i3+i4) == 38:
                    greens.append("{}{}{}{}".format(
                        chr(i1+64), chr(i2+64), chr(i3+64), chr(i4+64)))
                            
            
print(len(reds)*len(greens))
i = 0
j = 0                
with open('AIVD17b8.txt', 'w') as f:
    for red in reds:
        j += 1
        for green in greens:
            permutation = (green[0:2]+red[0:2]+green[2]+red[2]
                           +green[3]+red[3]+'t').lower()

            if (i % 1000) == 0:
                print('{:.2f}\t{}'.format(j/len(reds), permutation))
            i += 1

            for w in allwords:
                if w in permutation:
                    f.write(w + '\t\t' + permutation + '\r\n')
