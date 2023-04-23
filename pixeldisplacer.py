import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import map_coordinates

image = cv.imread("test_pictures/white_background.JPEG", cv.IMREAD_GRAYSCALE)

height, width = image.shape

x_coordinates, y_coordinates = np.meshgrid(np.arange(width, dtype=float), np.arange(height, dtype=float))

# # stretch out eyes
# c = 469.5
# w = 57
# a = 1/2
# y_coordinates -= a * (y_coordinates - c) * np.exp(- ((y_coordinates - c)/w)**2)

# # squish mouth
# c = 600
# w = 45
# a = -1/2
# y_coordinates -= a * (y_coordinates - c) * np.exp(- ((y_coordinates - c)/w)**2)

# displace eyes
a = 40
c = 469.5
w = 90
y_coordinates += a * np.exp(-((y_coordinates - c)/w)**2)
y_coordinates += 10

plt.imshow(map_coordinates(image, [y_coordinates, x_coordinates]), cmap="gray")
plt.show()


