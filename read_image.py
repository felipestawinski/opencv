import cv2 as cv
import os

img = cv.imread('Photos/test.jpg')

cv.imshow('Test', img)


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cv.imshow('Test2', rescaleFrame(img))

cv.waitKey(0)