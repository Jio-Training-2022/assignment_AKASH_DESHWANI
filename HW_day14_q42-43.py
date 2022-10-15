# Draw sin wave using matplotlib. 
# Draw cos wave using matplotlib. 

import matplotlib.pyplot as plt
import numpy as np
# import math


# # Fs = 8000
# # f = 5
# # sample = 8000
# # x = np.arange(sample)
# # y = np.sin(2 * np.pi * f * x / Fs)
# # plt.plot(x, y)
# # plt.xlabel('sample(n)')
# # plt.ylabel('voltage(V)')
# # plt.show()


# x = np.arange(0,4*np.pi,0.1)   # start,stop,step
# y = np.sin(x)
# z = np.cos(x)

# plt.plot(x,y)
# plt.xlabel('sample(n)')
# plt.ylabel('voltage(V)')
# plt.show()
# plt.plot(x,z)

X = np.arange(0,4*np.pi,0.1) 

Y1 = np.sin(X)
Y2 = np.cos(X)
  
# Initialise the subplot function using number of rows and columns
figure, axis = plt.subplots(2)
  
# For Sine Function
axis[0].plot(X, Y1)
axis[0].set_title("Sine Function")
  
# For Cosine Function
axis[1].plot(X, Y2)
axis[1].set_title("Cosine Function")

plt.show()