# Names are given in a file, check whether a particular name is present. 


if __name__ == "__main__":
    with open("D://Study//AI_DS//1_Term//05_Python//python_Statusneo//Code//scripts//name.txt", "r") as name:
        lines = name.readlines()
        sname = input("Enter the name to be searched: ")
        for line in lines:
            if sname in line:
                print("Name is present")
                break
        else:
            print("Name not present")
