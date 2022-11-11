import cv2 as cv
from advanced_scripts.find_edges import canny_edge_detection
from advanced_scripts.find_contours import find_coord


def kuka_coord(points):
    kuka_points = []
    for point in points:
        x = 244.6 + (251 - int(point[1]))*0.5
        y = 160.07 + (354 - int(point[0]))*0.5
        kuka_points.append([round(x, 2), round(y, 2)])
    return kuka_points


img = cv.imread('../Images/kuka_camera.jpg')

cropped_img = img[222:473, 486:840]
cv.imshow('Crop', cropped_img)

canny = canny_edge_detection(cropped_img)

contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_TC89_KCOS)

points = find_coord(contours[0])
print(*kuka_coord(points), sep="\n")
cv.waitKey(0)
