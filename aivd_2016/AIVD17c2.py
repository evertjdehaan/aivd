# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 22:13:06 2016

@author: evehaa
"""

from getwords import getwords

allwords = getwords(minlen=4, maxlen=12)

reds = []
red_vals = [1, 4, 7, 10, 13, 16, 19, 22, 25]
for i1 in red_vals:
    for i2 in red_vals:
        for i3 in red_vals:
            for i4 in red_vals:
                for i5 in red_vals:
                    for i6 in red_vals:
                        if (i1+i2+i3+i4+i5+i6) == 30:
                            reds.append("{}{}{}{}{}{}".format(
                                chr(i1+64), chr(i2+64), chr(i3+64),
                                chr(i4+64), chr(i5+64), chr(i6+64)))

greens = []
green_vals = [2, 5, 8, 11, 14, 17, 20, 23, 26]
for i1 in green_vals:
    for i2 in green_vals:
        for i3 in green_vals:
            for i4 in green_vals:
                for i5 in green_vals:
                    if (i1+i2+i3+i4+i5) == 40:
                        greens.append("{}{}{}{}{}".format(
                            chr(i1+64), chr(i2+64), chr(i3+64),
                            chr(i4+64), chr(i5+64)))

print(len(greens)*len(reds))
i = 0
j = 0
with open('AIVD17c2.txt', 'w') as f:
    for red in reds:
        j += 1
        for green in greens:
            permutation = (red[0]+green[0]+red[1]+green[1:3]+'i'+
                            red[2]+green[3:5]+red[3:6]).lower()

            if (i % 5000) == 0:
                print('{:.2f}\t{}'.format(j/len(reds), permutation))
            i += 1

            for w in allwords:
                if w in permutation:
                    f.write(w + '\t\t' + permutation + '\r\n')
