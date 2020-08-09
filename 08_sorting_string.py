#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sorting a String
Created on Sun Aug  9 2020
@author: oleksadub
"""

def strsort(str):
    chars = []
    for char in str:
        chars.append(char)
    chars.sort()

    return ''.join(chars)


print(strsort('cdba'))
