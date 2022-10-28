import cv2 as cv
import numpy as np
from basic_scripts import transformation as trans
from find_edges import canny_edge_detection, laplacian_edge_detection


img = trans.rescale_frame(cv.imread('Images/lines_enhanced.jpg'))
cropped_img = img[25:, :-20]

canny = canny_edge_detection(cropped_img, (5, 5))  # Make Canny
laplacian = laplacian_edge_detection(cropped_img)  # Make Laplacian

contours, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)  # Find contours (canny or laplacian)
drawing = np.zeros((canny.shape[0], canny.shape[1], 1), dtype=np.uint8)  # Make Matrix for drawing

# Draw a matrix
for i in range(len(contours)):
    cv.drawContours(drawing, contours, i, 255, 1, cv.LINE_8, hierarchy, 0)

# Find coordinates
i, j = 0, 0
for contour in contours:
    print(f'New contour #{i+1}')
    for point in contour:
        print('X =', point[0][0], 'Y =', point[0][1])
        j += 1
    print(f'Total point:{j}')
    j = 0
    i += 1
print('Total contours:', i)
