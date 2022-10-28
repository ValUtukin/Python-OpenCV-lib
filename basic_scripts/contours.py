import cv2 as cv
import numpy as np
from transformation import rescale_frame

img = rescale_frame(cv.imread('../Images/Women.jpg'))
cv.imshow('Origin image', img)

blank = np.zeros(img.shape, dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow('Blur image', blur)
#
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny edges', canny)

ret, thresh = cv.threshold(gray, 105, 255, cv.THRESH_BINARY)
cv.imshow('Threshed image', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

cv.drawContours(blank, contours, -1, (0, 0, 200), 1)
cv.imshow('Contours drawn', blank)
cv.waitKey(0)
