from ast import Num
from random import randint
from tkinter import Variable

# Name: Erica Tovar

# Write a program that takes an integer from the user and print out a countdown from the integer down to 0
# using a while loop
# Optional: use this format of print to output the integers in one line: print(x, end=' ')

### Write here ###
num = int(input("Please enter the number you'd like to countdown from: "))
while(num >= 0):
    print(num, end=' ')
    num -= 1
print()

#--------------------------------------------------------------------------------------------------------

# Write a program that takes an integer from the user and calculate its factorial, Ex: (3! = 3 * 2 * 1)
# Don't forget 0! = 1

### Write here ###
num_2 = int(input("Please enter a positive integer to calculate its factoral: "))
fact = 1

if num_2 < 0:
    print("Please only enter positive integers.")
elif num_2 < 2:
    print("{}! = {}".format(num_2, fact))
else:
    for i in range(num_2, 1, -1):
        fact = fact * i
    print("{}! = {}".format(num_2, fact))
print()

#--------------------------------------------------------------------------------------------------------

# Below is a list filled with 100 random integers. Write a program that goes through the list and ONLY prints
# out each integer that is divisible by 7.

randInts = []
for i in range(100):
    randInts.append(randint(0,999))

### Write here ###
for i in randInts:
    if (i % 7 == 0):
        print(i)
print()

#--------------------------------------------------------------------------------------------------------

# Write a program that takes an integer from the user and prints the following pattern:
# 1
# 1 2
# 1 2 3
# 1 2 3 4...

# Optional: Only continue the code if the user enters an integer greater than 1

### Write here ###
rows = int(input("Please enter a positive integer here: "))

if rows < 0:
    print("Please only enter positive integers.")
else:
    for i in range(rows):
        for j in range(i + 1):
            print(j + 1, end=" ")
        print()
        