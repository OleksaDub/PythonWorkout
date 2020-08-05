#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pig Latin Sentence
Created on Wed Aug  5 22:57:34 2020
@author: oleksadub
"""

def pig_latin(word):
    res = word + 'way'
    if word[0] not in 'aeiou':
        res = word[1:] + word[0] + 'ay'
        
    return res

def pl_sentence(sentence):
    words = sentence.split(' ')
    res = []
    for word in words:
        res.append(pig_latin(word))
        
    return ' '.join(res)


print(pl_sentence('this is a test translation'))