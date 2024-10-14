import sys
import cv2

cap = cv2.VideoCapture("./assets/cat.mp4")
if not cap.isOpened():
    sys.exit("File Error")

captures = []
while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("video", frame)
        key = cv2.waitKey(1)  # delay 1 ms
        if key == ord("c"):
            captures.append(frame)
            print(captures)
        elif key == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()

# Captered Frame
if captures:
    for i, capture in enumerate(captures):
        cv2.imwrite(f"./outputs/frame-{i}.jpg", capture)
