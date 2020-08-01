#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Number Guessing Game
Created on Sat Aug  1 22:08:27 2020
@author: oleksadub
"""

import random as r

def guessing_game():
    number = r.randint(0, 100)
    isGuessed = False
    
    while not isGuessed:
        userInput = int(input("Please, enter a number between 0 and 100.\n"))
        if userInput == number:
            isGuessed = True
            print("Just right!")
        elif userInput > number:
            print("Too high. Try again")
        else:
            print("Too low. Try again")
            
guessing_game()



