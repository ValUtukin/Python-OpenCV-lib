import cv2 as cv
from transformation import rescale_frame

img = rescale_frame(cv.imread('../Images/Women.jpg'))
cv.imshow('Origin image', img)

# Averaging
average = cv.blur(img, (3, 3))
cv.imshow('Average blur', average)

# Gaussian blur
gaussian = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian blur', gaussian)

# Median blur
median = cv.medianBlur(img, 3)
cv.imshow('Median blur', median)

# Bilateral blur
bilateral = cv.bilateralFilter(img, 10, 45, 35)
cv.imshow('Bilateral blur', bilateral)
cv.waitKey(0)
