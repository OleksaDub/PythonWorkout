#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sorting a String
Created on Sun Aug  9 2020
@author: oleksadub
"""

#My solution
def strsort(str):
    chars = []
    for char in str:
        chars.append(char)
    chars.sort()

    return ''.join(chars)

#The book's solution
def strsort_book(str):
    return ''.join(sorted(str))

