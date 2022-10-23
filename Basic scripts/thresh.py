import cv2 as cv
from transformation import rescale_frame


def main():
    img = rescale_frame(cv.imread('../Images/lines_enhanced.jpg'), scale=0.3)
    cv.imshow('Origin image', img)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', gray)

    # Simple Thresholding
    threshold, thresh = cv.threshold(gray, 230, 255, cv.THRESH_BINARY)
    cv.imshow('Simple thresholded', thresh)

    threshold_inverse, thresh_inverse = cv.threshold(gray, 210, 255, cv.THRESH_BINARY_INV)
    # cv.imshow('Simple thresholded inverse', thresh_inverse)

    # Adaptive thresholding
    adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 7, 5)
    cv.imshow('Adaptive threshold', adaptive_thresh)

    blur = cv.GaussianBlur(adaptive_thresh, (5, 5), 11)
    # cv.imshow('Blur', blur)

    canny = cv.Canny(adaptive_thresh, 20, 255, apertureSize=7, L2gradient=False)
    cv.imshow('Canny', canny)

    cv.waitKey(0)


if __name__ == '__main__':
    main()
