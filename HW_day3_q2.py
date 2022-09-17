## Print table of 5, 6, 7, 8, 9, 10.

#def table_print(n):
    # for count in range(1,11):
    #     print (n,"*",count,"=", int(n*count) )


if __name__ == "__main__":
    print('Print table of 5, 6, 7, 8, 9, 10.')
    # number = int(input("Enter an integer: "))
    #table_print(number)
    n = int(input("Enter an integer: "))
    for count in range(1,11):
        print (n,"*",count,"=", int(n*count) )
 