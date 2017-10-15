import numpy as np
from math import sqrt, pi
import cv2
from gripper_mcu import GripperMCU

import serial

def dist(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    return sqrt( dx**2 + dy**2 )

def findCentroid(cnt):
    M = cv2.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    return cx, cy

def calcActualWidth(pixelWidth, sonarDist, frameWidth=640, fovTh=.8*pi):
    # TODO: Normalize the pixelWidth and multiply by a const to scale
    width = (sonarDist*tan(.5*fovTh)) + (.5*frameWidth)
    width *= 2*pixelWidth
    width /= frameWidth
    return width

# The camera device value
CAMERA_DEV = 1

# Low and High HSV profiles for object detection test
low_blue = np.uint8([180, 20, 40])
high_blue = np.uint8([260, 255, 200])



# Begin new video capture
cap = cv2.VideoCapture(CAMERA_DEV)

# Instantiate the gripper MCU
hand = GripperMCU('/dev/ttyACM0')

# Read first frame for information purposes
ret, frame = cap.read()
# Retrieve const frame dimensinos
ROWS, COLS, CHANS = frame.shape

# Constant coordinates for frame center
frame_center_x = COLS / 2;
frame_center_y = ROWS / 2;

while (True):
    # Read in a new frame
    ret, frame = cap.read()

    # Convert color profile to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold hsv space for blue object values
    mask = cv2.inRange(hsv, low_blue, high_blue)

    # Morphological kernels to be used
    kernel_erode = np.ones((5,5), np.uint8)
    kernel_dilate = np.ones((9,9), np.uint8)

    # Perform some morphological filtering on mask pixels
    roi_map = cv2.erode(mask, kernel_erode, iterations=3)
    roi_map = cv2.dilate(roi_map, kernel_dilate, iterations=3)

    # Calculate contours for the mask
    roi_map2, contours, hierarchy = cv2.findContours( roi_map,
            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the centroid of the object
    cnt = contours[0]
    cx, cy = findCentroid(cnt)

    # check whether object is approximately centered in frame
    if dist(cx, cy, frame_center_x, frame_center_y) > DIST_THRES:
        # Check whether frame is on the object's bounding rectangle body
        # Generate a bounding box for object to retrieve gripping information
        x, y, w, h = cv2.boundingRect(cnt)
        if (frame_center_x >= x) and (frame_center_x <= x+w) \
                and (frame_center_y >= y) and (frame_center_y <= y+h):
                    # Read distance read by ultrasonic sensor
                    dSonar = hand.sonarRead()
                    # Check the distance to the sonar
                    if dSonar <= hand.SONAR_DIST_THRESHOLD:
                        hand.grip(w); # Grip the object by a certain distance

    

    frame2 = cv2.drawContours(frame, contours, -1, (0, 0, 255), 3)

    cv2.imshow("Tracking", frame2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

ser.close()
