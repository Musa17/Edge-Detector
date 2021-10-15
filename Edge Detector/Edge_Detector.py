import cv2
import numpy as np

# Load image
image = cv2.imread('Pikachu.jpg')

# Creating and printing filters
Hor_filter = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
Vert_filter = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])

print(Hor_filter)
print(Vert_filter)
