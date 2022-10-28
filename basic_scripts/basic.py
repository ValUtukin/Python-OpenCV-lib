import cv2 as cv
from transformation import rescale_frame

img = rescale_frame(cv.imread('../Images/Women.jpg'))
cv.imshow('Origin image', img)

# Converting BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale image', gray)

# Blur an image
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur image', blur)

# Edge Detection
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

# Dilating canny
dilated = cv.dilate(canny, (11, 11), iterations=5)
cv.imshow('Dilated canny', dilated)

# Eroding
eroded = cv.erode(dilated, (3, 3), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (400, 600), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Crop image
cropped = img[100:800, 200:900]
cv.imshow('Cropped', cropped)
cv.waitKey(0)
