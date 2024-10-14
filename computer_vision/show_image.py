import sys

import cv2

img = cv2.imread("./assets/cat.jpg")
if img is None:
    sys.exit("File Error")

cv2.imshow("Image display", img)
cv2.waitKey()
cv2.destroyAllWindows()
