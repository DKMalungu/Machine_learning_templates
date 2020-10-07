# Importing libraries
import numpy as np
import matplotlib.image as mpimg  # for reading images
import matplotlib.pyplot as plt
import cv2  # Computer vision library

# Read in and display the image
image = mpimg.imread('simple_car.jpg')

# Print out the imsge dimensions
print('Image dimension: ', image.shape)

"""
Image dimension:  (724, 1131, 3)
724 - length values
1131 - height 
3 - channels 
"""

# Change from color to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.show()

# Print specific grayscale pixel values
x = 190
y = 375
pixel_val = gray_image[x, y]
print('pixel values at the location x = {}, y = {} is: '.format(x,y),pixel_val)

# Multipling each pixel by value 2
gray_image2 = gray_image*2
plt.imshow(gray_image2, cmap='gray')
plt.show()