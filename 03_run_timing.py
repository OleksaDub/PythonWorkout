#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Run timing
Created on Mon Aug  3 20:48:44 2020
@author: oleksadub
"""

def run_timing():
    results = []
    while True:
        time = input("Enter your 10K result in minutes: ")
        if not time: break
        results.append(float(time))
        
    total_time = sum(results)
    average = round((total_time/len(results)), 2)
    print(f'Average time to run a 10K is {average} minutes over {len(results)} runs')
    
def abridge_float(num, before, after):
    l = str(num).split('.')
    integer = l[0][before:]
    decimal = l[1][:after]
    
    res = float(integer + '.' + decimal)
    
    print(res)
    
def abridge_float2(num, before, after):
    print(round(num%10**before, after))


#########
#   TO DO
#   DECIMAL CLASS