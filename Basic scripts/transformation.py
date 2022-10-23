import cv2 as cv
import numpy as np

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down
def translation(img, x, y):
    trans_matrix = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans_matrix, dimensions)


def rotate(img, angle, rotation_point=None):
    (height, width) = img.shape[:2]

    if rotation_point is None:
        rotation_point = (width // 2, height // 2)
    rotation_matrix = cv.getRotationMatrix2D(rotation_point, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotation_matrix, dimensions)


def rescale_frame(img, scale=0.5):
    # Work for images, video and live video
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)


def change_resolution(width, height, video_capture):
    # Work only for live video
    video_capture.set(3, width)
    video_capture.set(4, height)


def main():
    img = rescale_frame(cv.imread('../Images/Women.jpg'))
    cv.imshow('Origin image', img)

    # Moving an image along x and y axis
    translated = translation(img, -100, -150)
    cv.imshow('Translated image', translated)

    # Rotate an image
    rotated = rotate(img, -90)
    cv.imshow('Rotated image', rotated)

    # Flip an image
    flipped = cv.flip(img, -1)  # 0 - flip over x-axis, 1 - flip over y-axis, -1 - flip over both axis
    cv.imshow('Flipped image', flipped)
    cv.waitKey(0)


if __name__ == '__main__':
    main()
