# Given number ( in string format ) in a file, read them and create a pandas series 

import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('D://Study//AI_DS//1_Term//05_Python//python_Statusneo//Code//scripts//marks.txt', delimiter = "/n")
    df1 = pd.Series(df)
    ## error 