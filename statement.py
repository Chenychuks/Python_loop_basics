#!/usr/bin/env python3
"""
Author : cheny <cheny@localhost>
Date   : 2022-09-13
Purpose: Python Control flow Statements and Loops
"""

# for loop with a nested if-else statement
my_name = 'Chukwuno Victoria'
count_check = 0
for item in range(3):
    count_check += 1
    name = input('Enter your name: ')
    if name and count_check < 3:
        if name.upper().lower() == my_name.upper().lower():
            print('Welcome')
            break
        else:
            print('Name can not be verified')
    else:
        print('Try again in 60 seconds')

# if-else statement in for loop
for item in range(3):
    name = input('Enter your name: ')
    if name.upper().lower() == my_name.upper().lower():
        print('Welcome')
        break
    else:
        print('Name can not be verified')
