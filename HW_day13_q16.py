# Given a number in binary, print its hex , octa and binary representation 

if __name__ == "__main__":
    num = int(input("Enter a number in binary: "),base = 2 )
    print("Hexadecimal: ", hex(num))
    print("Octal: ", oct(num))
    print("Binary: ", bin(num))