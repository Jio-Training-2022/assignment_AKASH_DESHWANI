# Task
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

# Example
# a =3
# b=5

# Print the following:

# 8
# -2
# 15
# Input Format

# The first line contains the first integer, .
# The second line contains the second integer, .

# link ->  https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true
# code 

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)