import cv2 as cv
import sys

img = cv.imread("./assets/cat.jpg")

if img is None:
    sys.exit("File Error")

cv.imshow("Original_RGB", img)
cv.imshow("Upper left half", img[0:img.shape[0]//2, 0:img.shape[1]//2, :])
cv.imshow(
    "Center half",
    img[
        img.shape[0]//4:3*img.shape[0]//4,
        img.shape[1]//4:3*img.shape[1]//4,
        :
        ]
    )

cv.imshow("R channel", img[:, :, 2])
cv.imshow("G channel", img[:, :, 1])
cv.imshow("B channel", img[:, :, 0])

cv.waitKey()
cv.destroyAllWindows()
