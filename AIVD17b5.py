# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 22:13:06 2016

@author: evehaa
"""

from getwords import getwords

allwords = getwords(minlen=4, maxlen=8)


greens = []
green_vals = [2, 5, 8, 11, 14, 17, 20, 23, 26]
for i1 in green_vals:
    for i2 in green_vals:
        for i3 in green_vals:
            for i4 in green_vals:
                for i5 in green_vals:
                    for i6 in green_vals:
                        if (i1+i2+i3+i4+i5+i6) == 51:
                            greens.append("{}{}{}{}{}{}".format(
                                chr(i1+64), chr(i2+64), chr(i3+64),
                                chr(i4+64), chr(i5+64), chr(i6+64)))
                            
blues = []
blue_vals = [3, 6, 9, 12, 15, 18, 21, 24]
for i1 in blue_vals:
    for i2 in blue_vals:
        for i3 in blue_vals:
            if (i1+i2+i3) == 60:
                blues.append("{}{}{}".format(
                    chr(i1+64), chr(i2+64), chr(i3+64)))
            
print(len(greens)*len(blues))
i = 0
j = 0                
with open('AIVD17b5.txt', 'w') as f:
    for green in greens:
        j += 1
        for blue in blues:
            permutation = (blue[0:2]+green[0:5]+blue[2]+green[5]).lower()

            if (i % 1000) == 0:
                print('{:.2f}\t{}'.format(j/len(greens), permutation))
            i += 1

            for w in allwords:
                if w in permutation:
                    f.write(w + '\t\t' + permutation + '\r\n')
