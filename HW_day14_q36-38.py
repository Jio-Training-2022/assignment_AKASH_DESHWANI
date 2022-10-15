# Convert the above numpy matrix to a pandas data frame 

import numpy as np
import pandas as pd


my_array = np.array([[11,22,33],[44,55,66]])

print(my_array)
print(type(my_array))

df = pd.DataFrame(my_array, columns = ['Column_A','Column_B','Column_C'])

print(df)
print(type(df))

# Save the above data frame as a csv file
df.to_csv('my_csv.csv')

# Save the above data frame as a excel file
df.to_excel('my_excel.xlsx')


# Replicate the same data in the excel file across multiple sheets with different names 

# df.to_excel('excel1.xlsx', sheet_name='Sheet1')
# df.to_excel('excel1.xlsx', sheet_name='Sheet2')
# df.to_excel('excel1.xlsx', sheet_name='Sheet3')