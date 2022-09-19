# Loan EMI Calculator
def EMIcal(p,n,r):
    r = (r/12)/100 #converting rate formula in months
    return (p*r*(((1+r)**n)/(((1+r)**n)-1)))

if __name__ == "__main__":
    p = float(input("Enter Principal loan ammount :"))
    n = float(input("Emter loan tenure in months :"))
    r = float(input("monthly interest rate :"))
    print ("EMI :", EMIcal(p,n,r))

