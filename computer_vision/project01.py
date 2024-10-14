import sys

import cv2
import numpy as np

img = cv2.imread("./assets/cat.jpg")
if img is None:
    sys.exit("File Error")

# TODO: Color to grayscale
# I = round(0.299*R + 0.587*G + 0.114*B)
cvt_img = np.zeros_like(img)
for i in range(3):
    cvt_img[:, :, i] = (
        0.299 * img[:, :, 2] +
        0.584 * img[:, :, 1] +
        0.1148 * img[:, :, 0]
        )

cv2.imshow("Image display", cvt_img)
cv2.waitKey()
cv2.destroyAllWindows()
