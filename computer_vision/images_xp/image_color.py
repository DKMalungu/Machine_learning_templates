# Importing Libraries
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Loading the image
image = mpimg.imread('simple_car.jpg')

# RGB channel visualization
red = image[:, :, 0]
green = image[:, :, 1]
blue = image[:, :, 2]
color = image[:, :, :]

f, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(20, 10))
ax1.set_title('Red color channel')
ax1.imshow(red, cmap='Reds')
ax2.set_title('Blue color channel')
ax2.imshow(blue, cmap='Blues')
ax3.set_title('Green color channels')
ax3.imshow(green, cmap='Greens')
ax4.set_title(' All color')
ax4.imshow(color)
plt.show()