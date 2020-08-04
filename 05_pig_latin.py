#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pig Latin
Created on Tue Aug  4 23:32:16 2020
@author: oleksadub
"""

def pig_latin(word):
    res = word + 'way'
    if word[0] not in 'aeiou':
        res = word[1:] + word[0] + 'ay'
        
    return res
        
print(pig_latin('python'))