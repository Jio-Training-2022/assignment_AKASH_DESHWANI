#For any given integer array A (read as input by the user), How will you find the second larget element/value in the array ?
#Write a python program to solve this problem.

def secmax_ele (a):
    max_value = 0
    max_sec = 0
    for i in range (0,len(a)):
        if (max_value < a[i]):
            max_sec = max_value
            max_value = a[i]
        elif a[i] > max_sec and max_sec < max_value:
            max_sec = a[i]
    return (max_sec)

if __name__ == "__main__":
    arr = []
    total_ele = int(input("Enter total no. of element :"))
    for i in range (total_ele):
        val = int(input("please enter each element :"))
        arr.append(val)
    print("Second largest element :" ,secmax_ele(arr))

