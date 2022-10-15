# given numbers ( in string format ) in a file, read them and create a numpy array
# marks.txt
# 10
# 20
# 30
# 20
# 50
# 80
# 100
# 55
# 60
# 70

if __name__ == "__main__":
    with open("D://Study//AI_DS//1_Term//05_Python//python_Statusneo//Code//scripts//marks.txt","r") as f:
        data = f.read()
        # data = data.split()
        # data = [int(i) for i in data]

    import numpy as np
    arr = np.array(data)
    print(arr)
    print(type(arr))

# import os 
# # current working directory
# os.getcwd()