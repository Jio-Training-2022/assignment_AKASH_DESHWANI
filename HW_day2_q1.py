## Write a program to find sum all Natural numbers from 1 to N where you have to take N as input from user

def sum(n):
    if n <= 1:
        return n
    else:
        return n + sum(n-1)


if __name__ == '__main__':
    print ("Write a program to find sum all Natural numbers from 1 to N where you have to take N as input from user")
    
    num = int(input("Enter a number: "))
    if num < 0:
        print("Enter a positive number")
    else:
        print("The sum is", sum(num))