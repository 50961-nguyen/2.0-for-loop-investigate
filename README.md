## Setup
1. Git clone this repository.
2. In this repository, create a new file called for_loop_investigate.py

## Instructions
Run the code first, see what the output is. Does it make sense? If you don't understand WHY something outputs the way it does, ask me. This step is really important.

Modify each loop according to the given #TODO.

## Code
"""
author:
date:
For Loops Investigation
"""

separator = "-" * 10

# Prints this sentence 5 times
# TODO: Print this sentence 7 times
for i in range(5):
    print("I love corn.")

print(separator)

# Prints numbers from 0 to 9
# TODO: Print numbers from 1 to 20
for i in range(0, 10):
    print(i)

print(separator)

# Prints all the even numbers from 0 to 30
# TODO: Print all the odd numbers from 1 to 100
for i in range(0, 30, 2):
    print(i)

print(separator)

# Prints numbers from 10 down to 1
# TODO: Print numbers from 20 down to 1
for i in range(10, 0, -1):
    print(i)

print(separator)

# Prints the squares of numbers from 1 to 5
# TODO: Print the cubes of numbers from 1 to 10
for i in range(1, 6):
    print(i ** 2)

print(separator)

# Prints every 5th number from 0 to 50
# TODO: Print every 10th number from 0 to 100
for i in range(0, 51, 5):
    print(i)
