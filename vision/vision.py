import numpy as np
import cv2

CAMERA_DEV = 1

low_blue = np.uint8([180, 20, 40])
high_blue = np.uint8([260, 255, 200])

cap = cv2.VideoCapture(CAMERA_DEV)

while (True):
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    rows, cols, chans = frame.shape
    # Threshold hsv space for blue duck values
    mask = cv2.inRange(hsv, low_blue, high_blue)

    kernel_erode = np.ones((5,5), np.uint8)
    kernel_dilate = np.ones((9,9), np.uint8)

    roi_map = cv2.erode(mask, kernel_erode, iterations=3)
    roi_map = cv2.dilate(roi_map, kernel_dilate, iterations=3)

    roi_map2, contours, hierarchy = cv2.findContours( roi_map,
            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    frame2 = cv2.drawContours(frame, contours, -1, (0, 0, 255), 3)

    cv2.imshow("Tracking", frame2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


