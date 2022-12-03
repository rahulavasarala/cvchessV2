import time
import cv2 
from flask import Flask, render_template, url_for, Response
import os
import json
import time
import math
import torch
from PIL import Image
import numpy as np

image_list = ["test1.jpg", "test2.jpg", "test3.jpg", "test4.jpg"]

corner_list = [[[113,34],[489, 38],[575, 528],[59, 535]], 
[[111,54],[493,58],[585, 563],[58,576]], [[111,54],[493,58],[585, 563],[58,576]], 
[[111,54],[493,58],[585, 563],[58,576]]]

ind = 0

api_chess_data = [[-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1], 
[-1,-1,-1,-1,-1,-1,-1,-1], 
[-1,-1,-1,-1,-1,-1,-1,-1], 
[-1,-1,-1,-1,-1,-1,-1,-1], 
[-1,-1,-1,-1,-1,-1,-1,-1], 
[-1,-1,-1,-1,-1,-1,-1,-1], 
[-1,-1,-1,-1,-1,-1,-1,-1]]


def warp_point(p, M):#Working code

    px = (M[0][0]*p[0] + M[0][1]*p[1] + M[0][2]) / ((M[2][0]*p[0] + M[2][1]*p[1] + M[2][2]))
    py = (M[1][0]*p[0] + M[1][1]*p[1] + M[1][2]) / ((M[2][0]*p[0] + M[2][1]*p[1] + M[2][2]))
    p_prime = (int(px), int(py)) # after transformation

    return p_prime

def warp_and_find_points(pts1, pts2, location_list, class_list):

    M = cv2.getPerspectiveTransform(pts1, pts2)

    loc_list_warped = []

    for location in location_list:

        p_prime = warp_point(location, M)
        loc_list_warped.append(p_prime)

    for (point, classs) in zip(loc_list_warped, class_list):

        x = point[0]
        y = point[1]

        rows = int(y/50)
        cols = int(x/50)

        if api_chess_data[rows][cols] == -1:
            api_chess_data[rows][cols] = classs
    


def format_raw_data(data_dict):

    location_list = []
    class_list = []

    for detection in data_dict:

        class_list.append(detection['class'])
        center_x = (detection['xmin'] + detection['xmax'])/2
        center_y = (detection['ymin'] + detection['ymax'])/2 + (detection['ymax'] - detection['ymin'])/2

        location_list.append((center_x, center_y)) 

    return location_list, class_list

def run_detections():

    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./best.pt')
    img1 = Image.open("{a}".format(a = image_list[ind]))
    results = model(img1)
    bbox_res = results.pandas().xyxy[0].to_json(orient="records")

    print(bbox_res)

    return json.loads(bbox_res)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chess_data')
def chess_data():

    return json.dumps(api_chess_data)


def gen():
    
    cap = cv2.VideoCapture('{a}'.format(a = ind))

    # Read until video is completed
    while(cap.isOpened()):
      # Capture frame-by-frame
        ret, img = cap.read()
        if ret == True:
            img = cv2.resize(img, (0,0), fx=0.5, fy=0.5) 
            frame = cv2.imencode('.jpg', img)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(1/60)
        else: 
            break
        

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def main():

    #Run all of the detection stuff on startup

    data_dic = run_detections()
    loc_list, class_list = format_raw_data(data_dic)

    pts1 = corner_list[ind]
    pts2 = [[0,0], [400,0], [400,400], [0,400]]

    pts1 = np.float32(pts1)
    pts2 = np.float32(pts2)

    warp_and_find_points(pts1, pts2, loc_list, class_list)
    print(api_chess_data)

    pass

if __name__ == '__main__':

    main()
    app.run(debug=True, port=58956)