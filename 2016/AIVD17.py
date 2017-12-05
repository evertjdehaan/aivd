# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 22:13:06 2016

@author: evehaa
"""

from getwords import getwords

allwords = getwords(minlen=3, maxlen=9)

#col1 = 13
#col2 = 30
#
#start1 = 1
#if col1 > 26:
#    start1 = col1 - 26
#
#start2 = 1
#if col2 > 26:
#    start2 = col2 - 26
#    
#end1 = min(col1, 26+1)
#end2 = min(col2, 26+1)
#
#for i1 in range(start1, end1):
#    for i2 in range(start2, end2):
#        print("{}{}{}{}V".format(
#                chr(i1+64),
#                chr(i2+64),
#                chr(col1-i1+64),
#                chr(col2-i2+64))
#        )



greens = []
for i1 in range(26):
    for i2 in range(26):
        for i3 in range(26):
            for i4 in range(26):
                for i5 in range(26):
                    for i6 in range(26):
                        if (i1+i2+i3+i4+i5+i6+6) == 51:
                            greens.append("{}{}{}{}{}{}".format(
                                chr(i1+65), chr(i2+65), chr(i3+65),
                                chr(i4+65), chr(i5+65), chr(i6+65)))
                            
blues = []
for i1 in range(26):
    for i2 in range(26):
        for i3 in range(26):
            if (i1+i2+i3+3) == 60:
                blues.append("{}{}{}".format(
                    chr(i1+65), chr(i2+65), chr(i3+65)))
                    
                    
with open('AIVD17.txt', 'w') as f:
    for green in greens:
        for blue in blues:
           permutation = (blue[0:2]+green[0:5]+blue[2]+green[5]).lower()
           
           for w in allwords:
               if w in permutation:
                   f.write(w + '\t\t' + permutation + '\r\n')