import cv2 as cv
import web_cam as wc
import hystogram as hysto

video_cap = cv.VideoCapture(0)

img = wc.grab_frame_from_camera(video_cap)
cv.imshow('Frame from Camera', img)

hysto.show_gray_histogram(img)
hysto.show_color_histogram(img)

cv.waitKey(0)


