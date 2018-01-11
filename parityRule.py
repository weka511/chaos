# -*- coding: utf-8 -*-
# Copyright (C) 2016 Universite de Geneve, Switzerland
# E-mail contact: sebastien.leclaire@etu.unige.ch
#
# The Parity Rule
#

import numpy as np, matplotlib.pyplot as plt,scipy,copy,scipy.misc
from matplotlib import cm
    
# Definition of functions
def readImage(string): # This function only work for monochrome BMP. 
    image =  scipy.misc.imread(string,1);
    image[image == 255] = 1
    image = image.astype(int) 
    return image # Note that the image output is a numPy array of type "int".

# Main Program

# Program input, i.e. the name of the image "imageName" and the maximum number of iteration "maxIter"
imageName = 'image3.bmp'
maxIter   = 32

# Read the image and store it in the array "image"
image = readImage(imageName) # Note that "image" is a numPy array of type "int".
# Its element are obtained as image[i,j]
# Also, in the array "image" a white pixel correspond to an entry of 1 and a black pixel to an entry of 0.

# Get the shape of the image , i.e. the number of pixels horizontally and vertically. 
# Note that the function shape return a type "tuple" (vertical_size,horizontal_size)
imageSize = np.shape(image);

# Print to screen the initial image.
print('Initial image:')
#plt.clf()
plt.imshow(image, cmap=cm.gray)
plt.figure()
#plt.pause(0.1)

# Main loop
for it in range(1,maxIter+1):
    
    imageCopy = copy.copy(image);
    
    # You need to write here the core of the parity rule algorithm.
    # Altough not mandatory, you might need to use the array "imageCopy" and the tuple "imageSize".
    #
    # Code that you need to write...
    # Code that you need to write...
    
    # Print to screen the image after each iteration.

    m=len(image)
    n=len(image[0])
    for i in range(m):
        for j in range(n):
            image[i][j]=(imageCopy[(i-1)%m][j]+imageCopy[(i+1)%m][j]+imageCopy[i][(j-1)%n]+imageCopy[i][(j+1)%n])%2
    print('Image after',it,'iterations:')
    plt.clf()
    plt.imshow(image, cmap=cm.gray)
    plt.figure()
    #plt.pause(0.1)
        
# Print to screen the number of white pixels in the final image
print("The number of white pixels after",it,"iterations is: ", sum(sum(image)))
plt.show()