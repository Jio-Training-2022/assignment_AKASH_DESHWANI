# Given a number A (read as input ), find the sum of its digits.


def getsum(n):
    sum = 0
    while(n != 0):
        sum = sum + int(n%10)
        n = int(n/10)
    return (sum)


if __name__ == "__main__":
    num = int(input("Enter a number to get some of digits :"))
    print ("Sum of digits : ",getsum(num))

