# print a picture using matplotlib.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread('Code\scripts\Image.jpeg')
imgplot = plt.imshow(img)
plt.show()