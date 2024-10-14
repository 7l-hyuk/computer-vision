import sys

import cv2

# Road image
img = cv2.imread("./assets/cat.jpg")
if img is None:
    sys.exit("File Error")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert image color
resized_img = cv2.resize(gray_img, dsize=(0, 0), fx=0.5, fy=0.5)

cv2.imshow("Color image", img)
cv2.imshow("Grayscale image", gray_img)
cv2.imshow("Resized Image", resized_img)
cv2.waitKey()
cv2.destroyAllWindows()
