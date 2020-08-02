#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Summing Numbers
Created on Sun Aug  2 20:32:47 2020
@author: oleksadub
"""

def mysum(* numbers):
    result = 0
    for number in numbers:
        result += number
    
    return result
    

def mysum_list(numbers, start = 0):
    for n in numbers:
        start += n
        
    return start
    

def average(numbers):
    result = 0
    for n in numbers:
        result += n

    return round((result / len(numbers)), 3)

def long_short_word(words):
    longest = shortest = len(words[1])
    total = 0
    
    for w in words:
        if len(w) > longest:
            longest = len(w)
        if len(w) < shortest:
            shortest = len(w)
        total += len(w)
        
    average_length = round((total / len(words)), 3)
    
    return (longest, shortest, average_length)
        
print(long_short_word(['mother','baked','cookies', 'and','bread']))








