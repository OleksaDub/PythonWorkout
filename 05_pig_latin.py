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
        
#print(pig_latin('python'))

# Handle caitalisation
def pl_capitalization(word):
    if not word[0].isupper():
        res = pig_latin(word)
    else:
        newWord = word[0].lower() + word[1:]
        res = pig_latin(newWord).capitalize()
        
    return(res)
        

print(pl_capitalization("Link"))