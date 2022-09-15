#!/usr/bin/env python3
"""
Author : cheny <cheny@localhost>
Date   : 2022-09-13
Purpose: Python Control flow Statements and Loops
"""

# Calculate the cube of any given number
start_value = int(input('Enter your starting value:'))
end_value = int(input('Enter your stopping value:'))

for i in range(start_value, end_value+1):
    a = i**3
    print('Cube of', i, 'is', a)
