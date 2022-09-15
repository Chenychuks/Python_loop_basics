
#!/usr/bin/env python3
"""
Author : cheny <cheny@localhost>
Date   : 2022-09-13
Purpose: Python Control flow Statements and Loops
"""

# prime number between any given range of number using while loop

start_value = int(input('Enter your starting value:'))
end_value = int(input('Enter your stopping value:'))

a = start_value
while (a <= end_value):
    i = 1
    count = 0
    while (i <= a):
        if(a % i == 0):
            count = count+1
        i = i+1
    if(count == 2):
        print(a)
    a = a+1

# prime number between any given range of number using for loop

for num in range(start_value, end_value+1):
    if num > 1:

        for item in range(2, num):
            if num % item == 0:
                break
        else:
            print(num)
