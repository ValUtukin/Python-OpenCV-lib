import cv2 as cv


def live_video_stream(video_capture):
    while True:
        ret, img = video_capture.read()

        cv.imshow('Live Video!', img)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()


def grab_frame_from_camera(video_capture):
    if video_capture.isOpened():
        ret, img = video_capture.read()
        if ret:
            return img
        else:
            return "frame not captured"
    else:
        return "cannot open camera"


def main():
    video_capture = cv.VideoCapture(0)  # work with WebCam

    # Start live stream from Camera
    # live_video_stream(video_capture)

    # Grab the frame from Camera
    # frame = grab_frame_from_camera(video_capture)
    # cv.imshow('Frame from Camera!', frame)

    cv.waitKey(0)


if __name__ == '__main__':
    main()
