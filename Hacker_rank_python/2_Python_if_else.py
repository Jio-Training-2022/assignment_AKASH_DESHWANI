# problem 

# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format

# A single line containing a positive integer, .

# Constraints

# Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.

# link -> https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
# code 

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0:
        print ('Weird')
    elif n%2 ==0 and (n in range (2,6) or n >20) :
        print ('Not Weird')
    elif n%2 ==0 and n in range (6,21):
        print ('Weird')
