#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ubbi Dubbi
Created on Thu Aug  6 19:42:56 2020
@author: oleksadub
"""

def ubbi_dubbi(word):
    res = ''
    for w in word:
        if w in 'aeiou':
            res += f'ub{w}'
        else: res += w
        
    return res

print(ubbi_dubbi('octopus'))
