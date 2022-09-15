#!/usr/bin/env python3
"""
Author : cheny <cheny@localhost>
Date   : 2022-09-13
Purpose: Python Control flow Statements and Loops
"""

# Use a loop to display elements from a given list present at odd index positions
My_list = []
list_size = int(input('Enter the size of your list:'))

for item in range(list_size):
    num = input('Enter item in list:')
    My_list.append(num)

for i in range(len(My_list)):
    if (not(i % 2)) == 0:
        print('Odd index:')
        print(My_list[i])


# Use a loop to display elements from a given list present at even index positions

My_list = []
list_size = int(input('Enter the size of your list:'))

for item in range(list_size):
    num = input('Enter item in list:')
    My_list.append(num)

for i in range(len(My_list)):
    if (i % 2) == 0:
        print('Odd index:')
        print(My_list[i])
