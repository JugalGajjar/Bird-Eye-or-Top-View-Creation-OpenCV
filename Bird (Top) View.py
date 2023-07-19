import sys
import cv2
import numpy as np

points = np.zeros((4, 2), dtype=int)
pt_num = 0


def get_pixel_using_mouse(event, x, y, flags, params):
    global pt_num
    try:
        if event == cv2.EVENT_LBUTTONDOWN:
            points[pt_num] = x, y
            pt_num += 1
    except IndexError:
        pass


try:
    img = cv2.imread("D:\\PYTHON PROJECTS\\Computer Vision\\TestData\\cardsImage.jpg")
    while True:
        if pt_num == 4:
            height, width = 280, 200

            select_points = np.float32([points[0], points[1], points[2], points[3]])
            output_points = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

            matrix = cv2.getPerspectiveTransform(select_points, output_points)
            top_img = cv2.warpPerspective(img, matrix, (width, height))
            cv2.imwrite("TopView.jpeg", top_img)
            print("TopView.jpeg is stored in the current active directory.")

            cv2.destroyWindow("Image")
            sys.exit()

        for i in range(0, 4):
            cv2.circle(img, (points[i][0], points[i][1]), 2, (0, 0, 255), cv2.FILLED)

        cv2.imshow("Image", img)
        cv2.setMouseCallback("Image", get_pixel_using_mouse)

        key = cv2.waitKey(1)
        if key == "q":
            sys.exit()

except KeyboardInterrupt:
    print("Terminating program.")
