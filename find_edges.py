import cv2 as cv
import numpy as np
import datetime

def rescale_frame(frame, scale=0.3):
    # Work for images, video and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = rescale_frame(cv.imread('Images/lines_enhanced.jpg'))
cv.imshow('Origin image', img)

gray_wo_blur = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale without blurring', gray_wo_blur)

gauss_blur = cv.GaussianBlur(gray_wo_blur, (3, 3), sigmaX=1, sigmaY=1)
cv.imshow('Gaussian blur', gauss_blur)

sobelx = cv.Sobel(gauss_blur, cv.CV_8U, 1, 0)
# cv.imshow('Sobel X', sobelx)
sobely = cv.Sobel(gauss_blur, cv.CV_8U, 0, 1)
# cv.imshow('Sobel Y', sobely)
combined_sobel = cv.bitwise_or(sobelx, sobely)
# cv.imshow('Combined Sobel', combined_sobel)

threshold_sobel, thresh_sobel = cv.threshold(combined_sobel, 4, 255, cv.THRESH_BINARY)
# cv.imshow('Sobel threshold', thresh_sobel)

median = cv.medianBlur(img, 5)
# cv.imshow('Median blur', median)

# Grayscale after median blurring
gray_with_blur = cv.cvtColor(median, cv.COLOR_BGR2GRAY)
# cv.imshow('Grayscale after blurring', gray_with_blur)

lap = cv.Laplacian(gray_with_blur, cv.CV_8U)
lap = np.uint8(np.absolute(lap))
# cv.imshow('Laplacian', lap)

threshold_inverse, thresh_inverse = cv.threshold(lap, 4, 255, cv.THRESH_BINARY)
# cv.imshow('Simple threshold', thresh_inverse)

now = datetime.datetime.now()

canny = cv.Canny(gauss_blur, 30, 60, apertureSize=3, L2gradient=True)
cv.imshow('Canny', canny)

then = datetime.datetime.now()
delta = then - now

print(delta.microseconds)

cv.waitKey(0)
