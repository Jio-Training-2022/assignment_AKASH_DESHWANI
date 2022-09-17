## print first N natural numbers taking N as an input from the user

def natural_numbers(a):
    for i in range(1,a+1):
        print (i)
    pass

if __name__ == "__main__":
    print ('print first N natural numbers taking N as an input from the user')
    a = int(input("Enter a natural number :"))
    natural_numbers(a)