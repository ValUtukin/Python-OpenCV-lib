import cv2 as cv
from transformation import rescale_frame
import numpy as np


def main():
    img = rescale_frame(cv.imread('../Images/Djokonda.jpg'))
    cv.imshow('Origin image', img)

    # creating black mask with width and height of original image
    blank = np.zeros(img.shape[:2], dtype='uint8')

    mask1 = cv.circle(blank.copy(), (img.shape[1] // 2 - 10, 230), 100, 255, -1)
    cv.imshow('Mask 1', mask1)

    mask2 = cv.rectangle(blank.copy(), (img.shape[1] // 2 - 10, 230), (img.shape[0] // 2 + 10, 500), 255, -1)
    cv.imshow('Mask 2', mask2)

    masked = cv.bitwise_and(img, img, mask=mask1 + mask2)
    cv.imshow('Masked with bitwise AND', masked)
    cv.waitKey(0)


if __name__ == '__main__':
    main()

