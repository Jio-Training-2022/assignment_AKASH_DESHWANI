# Given an array nums (read as input by the user), separate the odd and even numbers from the array and print them on separate lines.

def printEandO(a):
    Elist = []
    Olist = []
    for i in range (0,len(a)):
        if a[i]%2 == 0:
            Elist.append(a[i])
        else:
            Olist.append(a[i])
    
    print ("Even number :", Elist)
    print ("Odd numbers", Olist)

if __name__ == "__main__":
    arr = []
    total_ele = int(input("Enter total no. of element :"))
    for i in range (total_ele):
        val = int(input("please enter each element :"))
        arr.append(val)
    printEandO(arr)
