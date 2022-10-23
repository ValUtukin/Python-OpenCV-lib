import cv2 as cv
from transformation import rescale_frame


def main():
    img = rescale_frame(cv.imread('../Images/Women.jpg'))
    cv.imshow('Origin BGR Image', img)

    # BGR to Grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', gray)

    # BGR to HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.imshow('HSV image', hsv)

    # BGR to L*A*B
    lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
    cv.imshow('LAB image', lab)

    # BGR to RGB
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    cv.imshow('RGB image', rgb)
    cv.waitKey(0)


if __name__ == '__main__':
    main()
