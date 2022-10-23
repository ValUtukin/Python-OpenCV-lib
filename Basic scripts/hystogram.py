import cv2 as cv
import matplotlib.pyplot as plt
from transformation import rescale_frame


def show_gray_histogram(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    gray_hist = cv.calcHist([gray], [0], mask=None, histSize=[256], ranges=[0, 256])

    plt.figure()
    plt.title('Grayscale histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')
    plt.plot(gray_hist)
    plt.xlim([0, 256])
    plt.show()


def show_color_histogram(image):
    plt.figure()
    plt.title('Color histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')

    colors = ('b', 'g', 'r')
    for i, col in enumerate(colors):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])

    plt.show()


def main():
    img = rescale_frame(cv.imread('../Images/Djokonda.jpg'))
    cv.imshow('Origin image', img)

    show_gray_histogram(img)
    show_color_histogram(img)

    cv.waitKey(0)


if __name__ == '__main__':
    main()
