# File for testing purposes
import cv2 as cv
import web_cam as camera

video_capture = cv.VideoCapture(0)
frame = camera.grab_frame_from_camera(video_capture)

cv.imshow('Frame', frame)

cv.waitKey(0)


