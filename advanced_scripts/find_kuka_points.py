import cv2 as cv
from advanced_scripts.find_edges import canny_edge_detection
from advanced_scripts.find_contours import find_coord
from advanced_scripts import find_middle_points


def kuka_coord(points):
    kuka_points = []
    for point in points:
        x = 244.6 + (251 - int(point[1]))*0.5
        y = 160.07 + (354 - int(point[0]))*0.5
        kuka_points.append([round(x, 2), round(y, 2)])
    return kuka_points


def main():
    img = cv.imread('../Images/Curve1.jpg')
    canny = canny_edge_detection(img)
    contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_TC89_KCOS)

    points = []
    for point in contours[0]:
        points.append([point[0][0], point[0][1]])

    cv.waitKey(0)


if __name__ == "__main__":
    main()
