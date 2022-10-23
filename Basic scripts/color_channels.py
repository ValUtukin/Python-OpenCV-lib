import cv2 as cv
import numpy as np
from transformation import rescale_frame


def blue_multiplication(blue_channel_image, multi):
    height, width = blue_channel_image.shape[:2]
    for i in range(0, height):
        for j in range(0, width):
            blue_channel_image[i][j][0] = int(blue_channel_image[i][j][0] * multi)
    return blue_channel_image


def green_multiplication(green_channel_image, multi):
    height, width = green_channel_image.shape[:2]
    for i in range(0, height):
        for j in range(0, width):
            green_channel_image[i][j][1] = int(green_channel_image[i][j][1] * multi)
    return green_channel_image


def red_multiplication(red_channel_image, multi):
    height, width = red_channel_image.shape[:2]
    for i in range(0, height):
        for j in range(0, width):
            red_channel_image[i][j][2] = int(red_channel_image[i][j][2] * multi)
    return red_channel_image


img = rescale_frame(cv.imread('../Images/Djokonda.jpg'))
cv.imshow('Origin image', img)

# Just black blank with width and height of original image
blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

new_blue = blue_multiplication(blue, 1.7)
new_green = green_multiplication(green, 1/8)
new_red = red_multiplication(red, 1.1)

grayBlue = cv.cvtColor(new_blue, cv.COLOR_BGR2GRAY)
grayGreen = cv.cvtColor(new_green, cv.COLOR_BGR2GRAY)
grayRed = cv.cvtColor(new_red, cv.COLOR_BGR2GRAY)

merged = cv.merge([grayBlue, grayGreen, grayRed])
cv.imshow('New color values', merged)

cv.waitKey(0)
