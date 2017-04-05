# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 2:58:51 2016

@author: evehaa
"""

from cryptography import Cryptography
from getwords import getwords

allwords = getwords(minlen=4, maxlen=10)

#message = '--....-.....----'
message = '..----.-----....'
options = []

crypt = Cryptography()


def add_option(string):
    options.append(string)


for i1 in range(1, 5):
    if i1 > len(message):
        break
    l1 = crypt.decode_morse(message[:i1])
    if l1 is None: continue
    sub1 = message[i1:]
    
    for i2 in range(1, 5):
        if i2 > len(sub1):
            add_option(l1)
            break
        l2 = crypt.decode_morse(sub1[:i2])
        if l2 is None: continue
        sub2 = sub1[i2:]        
        
        for i3 in range(1, 5):
            if i3 > len(sub2):
                add_option(l1+l2)
                break
            l3 = crypt.decode_morse(sub2[:i3])
            if l3 is None: continue
            sub3 = sub2[i3:]
        
            for i4 in range(1, 5):
                if i4 > len(sub3):
                    add_option(l1+l2+l3)
                    break
                l4 = crypt.decode_morse(sub3[:i4])
                if l4 is None: continue
                sub4 = sub3[i4:]
                
                for i5 in range(1, 5):
                    if i5 > len(sub4):
                        add_option(l1+l2+l3+l4)
                        break
                    l5 = crypt.decode_morse(sub4[:i5])
                    if l5 is None: continue
                    sub5 = sub4[i5:]
                    
                    for i6 in range(1, 5):
                        if i6 > len(sub5):
                            add_option(l1+l2+l3+l4+l5)
                            break
                        l6 = crypt.decode_morse(sub5[:i6])
                        if l6 is None: continue
                        sub6 = sub5[i6:]
                        
                        for i7 in range(1, 5):
                            if i7 > len(sub6):
                                add_option(l1+l2+l3+l4+l5+l6)
                                break
                            l7 = crypt.decode_morse(sub6[:i7])
                            if l7 is None: continue
                            sub7 = sub6[i7:]
                            
                            for i8 in range(1, 5):
                                if i8 > len(sub7):
                                    add_option(l1+l2+l3+l4+l5+l6+l7)
                                    break
                                l8 = crypt.decode_morse(sub7[:i8])
                                if l8 is None: continue
                                sub8 = sub7[i8:]
                                
                                for i9 in range(1, 5):
                                    if i9 > len(sub8):
                                        add_option(l1+l2+l3+l4+l5+l6+l7+l8)
                                        break
                                    l9 = crypt.decode_morse(sub8[:i9])
                                    if l9 is None: continue
                                    sub9 = sub8[i9:]
                                    
                                    for i10 in range(1, 5):
                                        if i10 > len(sub9):
                                            add_option(l1+l2+l3+l4+l5+l6+l7+l8+l9)
                                            break
                                        l10 = crypt.decode_morse(sub9[:i10])
                                        if l10 is None: continue
                                        
                                        add_option(l1+l2+l3+l4+l5+l6+l7+l8+l9+l10)

options2 = []
for opt in options:
    for w in allwords:
        if w in opt:
            options2.append(opt)
            break

with open('AIVD11dot.txt', 'w') as f:
    f.write('\n'.join(sorted(set(options2))))