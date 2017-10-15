# VM endpoint: http://hackgt.eastus.cloudapp.azure.com:5432/
import dlib
import cv2

import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


tracking = False
prevImg = None

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    if not file:
        print "Did not receive an image"
        return -1
    img = file.read()

    # get points of interest
    points = [(420, 300), (840, 600)]

    if not points:
        print "No points of interest!"
        tracking = False
        prevImg = img
        return -1

    if not tracking:
        # initialize tracker using the points
        tracker = dlib.correlation_tracker()
        tracker.start_track(img, dlib.rectangle(*points[0]))
    else:
        tracker.update(img)

    rect = tracker.get_position()

    pt1 = (int(rect.left()), int(rect.top()))
    pt2 = (int(rect.right()), int(rect.bottom()))

    return int(rect.left()) + "," + int(rect.top()) + "," + int(rect.right()) + "," + int(rect.bottom())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5432)
