# Given numbers ( in string format ) in a file, read them and create a pandas data frame object 


# if __name__ == "__main__":
#     # with open("D://Study//AI_DS//1_Term//05_Python//python_Statusneo//Code//scripts//marks.txt","r") as f:
#     #     data = f.read()
#     #     # data = data.split()
#     #     # data = [int(i) for i in data]
    

# You can do as:
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

import pandas as pd
df = pd.read_csv('D://Study//AI_DS//1_Term//05_Python//python_Statusneo//Code//scripts//marks.txt', delimiter = "/n")
print(df)