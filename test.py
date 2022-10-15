
import numpy as np
import pandas as pd


my_array = np.array([[11,22,33],[44,55,66]])

print(my_array)
print(type(my_array))

df = pd.DataFrame(my_array, columns = ['Column_A','Column_B','Column_C'])

print(df)
print(type(df))

# Save the above data frame as a excel file
df.to_excel('my_excel.xlsx')