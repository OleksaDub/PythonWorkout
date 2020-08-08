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
       
# Handle punctuation
def pl_punctuation(word):
    punct = ['.',',','!','?',':',';']
    if not word[-1] in punct:
        return pig_latin(word)
    return pig_latin(word[0:-1]) + word[-1] 

# Handle caitalisation
def pl_capitalization(word):
    if not word[0].isupper():
        res = pl_punctuation(word)
    else:
        newWord = word[0].lower() + word[1:]
        res = pl_punctuation(newWord).capitalize()
        
    return(res)

# Same/Different vowels edition
def pl_vowels(word):
    vowels = set()
    for w in word:
        if w in 'aeiou':
            vowels.add(w)
    if len(vowels) > 1:
        return f'{word}way'
    else:
        return f'{word[1:]}{word[0]}ay'