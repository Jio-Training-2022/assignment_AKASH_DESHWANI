
# Task
# The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

# Example

# The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

# 0
# 1
# 4
# Input Format

# The first and only line contains the integer, .



# link -> https://www.hackerrank.com/challenges/python-loops/problem
#code 

if __name__ == '__main__':
    n = int(input())
    for i in range (0,n):
        print (i**2)

