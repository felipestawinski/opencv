import cv2 as cv
import numpy as np

# img = cv.imread('Photos/test.jpg')
# cv.imshow('test', img)

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

blank[:] = 0, 255, 255
cv.imshow('Yellow', blank)

cv.waitKey(0)