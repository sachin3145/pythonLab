""" write a python program to convert an RBG image to a grayscale image. """

import matplotlib.pyplot as plt
import matplotlib.image as mpimg 

img = mpimg.imread("./other/sample.jpg")

plt.imshow(img[:,:,1], cmap='gray', vmin = 0, vmax = 255)
plt.show()