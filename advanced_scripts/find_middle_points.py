import math
import cv2 as cv
import numpy as np


def get_points_till_first_edge(points):
    first_edge_center_pixel_coords = []
    for i in range(0, len(points)):
        r0 = 15
        J = -1
        for j in range(i + 1, len(points)):
            r = math.sqrt((points[j][0] - points[i][0]) ** 2 + (points[j][1] - points[i][1]) ** 2)
            if (r < 11) and (abs(i - j) >= 15) and (abs(i - j) <= len(points) - 15) and r < r0:
                J = j
                r0 = r
                xc = int((points[j][0] + points[i][0]) / 2)
                yc = int((points[j][1] + points[i][1]) / 2)
                first_edge_center_pixel_coords.append([xc, yc])
        if J < 0:
            break  # find an edge
        else:
            continue
    return first_edge_center_pixel_coords


def get_points_till_second_edge(points):
    second_edge_center_pixel_coords = []
    for i in range(len(points) - 1, 0, -1):
        r0 = 15
        J = -1
        for j in range(i, 0, -1):
            r = math.sqrt((points[j][0] - points[i][0]) ** 2 + (points[j][1] - points[i][1]) ** 2)
            if (r < 11) and (abs(i - j) >= 15) and (abs(i - j) <= len(points) - 15) and r < r0:
                J = j
                r0 = r
                xc = int((points[j][0] + points[i][0]) / 2)
                yc = int((points[j][1] + points[i][1]) / 2)
                second_edge_center_pixel_coords.append([xc, yc])
        if J < 0:
            break  # find an edge
        else:
            continue
    return second_edge_center_pixel_coords


def get_all_middle_points(till_first_edge, till_second_edge):
    return till_first_edge[::-1] + till_second_edge


def draw_middle_line(blank, points):
    for i in range(0, len(points)):
        cv.circle(blank, (points[i][0], points[i][1]), 1, (200, 0, 255), thickness=1)
    cv.imshow('Middle line', blank)


def main():
    img = cv.imread('../Images/Curve2.png')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, ksize=(5, 5), sigmaX=1)
    canny = cv.Canny(blur, 30, 60, apertureSize=3, L2gradient=True)
    contours, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    points = []
    for point in contours[0]:
        points.append([point[0][0], point[0][1]])

    first_points = get_points_till_first_edge(points)
    second_points = get_points_till_second_edge(points)

    print(f'Total amount of points in the middle line is {len(first_points[::-1] + second_points)}')
    print(f'Amount of points till first edge is {len(first_points)}')
    print(f'Amount of points till second edge is {len(second_points)}')
    print('All points below:')
    print(*get_all_middle_points(first_points, second_points))
    draw_middle_line(img, (first_points[::-1] + second_points))

    cv.waitKey(0)


if __name__ == "__main__":
    main()
