import cv2 as cv
import numpy as np


def main():
    blank = np.zeros((500, 500, 3), dtype='uint8')
    # cv.imshow('Blank', blank)

    # Draw a square
    blank[1:10, 150:160] = 0, 255, 0  # y = [1; 10] and x = [150; 160]
    cv.imshow('Green square', blank)

    # Draw rectangle
    cv.rectangle(blank, (0, 0), (blank.shape[0] // 2, 170), (255, 0, 150), thickness=cv.FILLED)
    cv.imshow('Rectangle', blank)

    # Draw circle
    cv.circle(blank, (250, 100), 50, (255, 0, 0), thickness=5)
    cv.imshow('Circle', blank)

    # Draw line
    cv.line(blank, (0, 10), (blank.shape[0] // 2, blank.shape[1] // 2), (255, 255, 255), thickness=2)
    cv.imshow('Line', blank)

    # Write text
    cv.putText(blank, "What's up!", (20, 100), cv.FONT_HERSHEY_COMPLEX, 0.5, (156, 223, 0), 1)
    cv.imshow('Some text', blank)
    cv.waitKey(0)


if __name__ == '__main__':
    main()
