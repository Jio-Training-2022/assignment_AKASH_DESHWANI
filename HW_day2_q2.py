## Write a program to find simple interest on a principal amount A at interest rate of R for time period T. 
## Take A, R and T as input from the user.

## just checking changes in git

def SI(a,r,t):
    return float(a*r*t/100)

if __name__ == '__main__':
    print ("Write a program to find simple interest on a principal amount A at interest rate of R for time period T. Take A, R and T as input from the user.")
    a = float(input('Enter the amount :'))
    r = float(input('Enter the rate :'))
    t = float(input('Enter the Time period :'))
    print("Simple Intreset is :",SI(a,r,t))