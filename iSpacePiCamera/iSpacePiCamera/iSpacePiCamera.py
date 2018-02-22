# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 18:03:00 2017

@author: Joel Mauriths Kambey
"""
import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
from firebase import firebase
import base64
import time
import datetime
url = "https://my-awesome-project-2fdd3.firebaseio.com//" # URL to Firebase database
token = "P6WgJAORwZYOtqNNz7PFtOB40fbhfSmCN3x0wj7z" # unique token used for authentication
firebase = firebase.FirebaseApplication(url, token)
i=0
while True:
    camera= PiCamera()
    rawCapture = PiRGBArray(camera)

    time.sleep(0.1)

    #while True:
    camera.capture(rawCapture,format="bgr")
    img_rgb = rawCapture.array
    #draw the timestamp on the image
    timestamp=datetime.datetime.now()
    ts=timestamp.strftime("%A %d %B %Y %I:%M:%S %p")
    cv2.putText(img_rgb, ts, (10, img_rgb.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    #Load carpark image
    #img_rgb = cv2.imread('Testimage4.jpg')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    #Load parking slots templates
    template1 = cv2.imread('PT1_3.jpg',0)
    w1, h1 = template1.shape[::-1]
    template2 = cv2.imread('PT2_3.jpg',0)
    w2, h2 = template2.shape[::-1]
    template3 = cv2.imread('PT3_3.jpg',0)
    w3, h3 = template3.shape[::-1]
    template4 = cv2.imread('PT4_3.jpg',0)
    w4, h4 = template4.shape[::-1]

    #Matching carpark image and templates
    output_ls = []
    res = cv2.matchTemplate(img_gray,template1,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    statusP1 = 'Occupied'
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w1, pt[1] + h1), (0, 0, 255), 2)
        statusP1 = 'Empty'
    output_ls.append(statusP1)
        
    res = cv2.matchTemplate(img_gray,template2,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    statusP2 = 'Occupied'
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w2, pt[1] + h2), (0, 0, 255), 2)
        statusP2 = 'Empty'
    output_ls.append(statusP2)
        
    res = cv2.matchTemplate(img_gray,template3,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    statusP3 = 'Occupied'
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w3, pt[1] + h3), (0, 0, 255), 2)
        statusP3 = 'Empty'
    output_ls.append(statusP3)

    res = cv2.matchTemplate(img_gray,template4,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    statusP4 = 'Occupied'
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w4, pt[1] + h4), (0, 0, 255), 2)
        statusP4 = 'Empty'
    output_ls.append(statusP4)
        
    print output_ls
    firebase.put('/', 'emptylots', output_ls)
    # Saving the File and Sending an Image to the Gui through Firebase
    cv2.imwrite("Feed.jpg", img_rgb)
    with open("Feed.jpg","rb") as imageFile:
        str =base64.b64encode(imageFile.read())
        print "Feed.jpg", str
        firebase.put('/', 'image', str)
#    cv2.imshow('Detected',img_rgb)
#    cv2.waitKey(0)
    cv2.destroyAllWindows()
    camera.close()
    time.sleep(5)
    i+=1
