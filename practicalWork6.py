# -*- coding: utf-8 -*-
"""LabWork6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fqeiFgV-qAXWdWGfZOTOKNT6uKW6HC2B
"""

import numba
from numba import cuda
import cv2
import matplotlib
import numpy as np
import time
import matplotlib.pyplot as plt

from matplotlib import image as img_
from matplotlib import pyplot as plt
import numpy as np

image = np.array(img_.imread("test.jpg", )).astype("uint16")
imageWidth = image.shape[1]
imageHeight= image.shape[0]

def gray(src,dst):
    for i in range(src.shape[0]):
      g = np.uint8((src[i][0] + src[i][1] + src[i][2])/3)
      dst[i][0] = dst[i][1] = dst[i][2] = g


image = image.reshape(imageWidth*imageHeight,3)
out = np.zeros((imageHeight*imageWidth, 3),np.uint8)  # This make the sum doesn't work. zeros by default use float  

gray(image,out)

image = out.reshape((imageHeight,imageWidth, 3))




########## BINERIZATION

# specify a threshold 0-255
threshold = 150

# make all pixels < image black
binarized = (1 * (image > threshold)).astype('uint8')

plt.imshow (binarized*255, cmap='gray', vmin=0, vmax=255)

from matplotlib import image as img_
from matplotlib import pyplot as plt
import numpy as np

image = np.array(img_.imread("test.jpg", )).astype("uint16")

# specify a brightness changes
brightness = 100
image = image + brightness

new_out = np.clip(image, 0,255).astype('uint8')


plt.imshow (new_out, cmap='gray', vmin=0, vmax=255)

from matplotlib import image as img_
from matplotlib import pyplot as plt
import numpy as np

# image = np.array(img_.imread("test.jpg", )).astype("uint16")

from PIL import Image
 
image1 = np.array(Image.open("test.jpg"))
newsize = (image1.shape[1], image1.shape[0])

image2 = np.array(Image.open("test2.jpg").resize(newsize, Image.ANTIALIAS))




# image2 = image2.resize(newsize)

w_1 = 0.5
w_2 = 0.5
image = w_1*image1 + w_2*image2

new_out = np.clip(image, 0,255).astype('uint8')


plt.imshow (new_out, cmap='gray', vmin=0, vmax=255)
