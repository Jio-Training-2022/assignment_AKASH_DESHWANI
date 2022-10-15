#Construct a 2x5 numpy matrix by taking all the numbers as input from user 

import numpy as np
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
  
  
print("Enter the entries in a single line (separated by space): ")
  
# User input of entries in a 
# single line separated by space
# matrix = np.full((R, C), 0) how to use this ?
entries = list(map(int, input().split()))
  
# For printing the matrix
matrix = np.array(entries).reshape(R, C)
print(matrix)
