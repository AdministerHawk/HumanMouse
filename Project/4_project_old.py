#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 16:59:51 2020

@author: hawk
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 12:02:12 2020

@author: hawk
"""


import pyautogui as gui
import cv2 as cv
import numpy as np
from keras.models import load_model


def active_target_app():
    # 获取当前屏幕分辨率
    screenWidth, screenHeight = gui.size()
    
    # 获取当前鼠标位置
    currentMouseX, currentMouseY = gui.position()
    
    # 2秒钟鼠标移动坐标为100,100位置  绝对移动
    gui.moveTo(200, 180,2)
    
    # 鼠标左击一次
    gui.click()





def prediction(eye_imgs):
    ret = 1    
    if eye_imgs.size >0:
        pred = eye_model.predict(eye_imgs)
        pre_result = np.where(pred==pred.max())
        pre_classes = pre_result[1]
        ret = round(pre_classes.mean())
    else:
        ret = -1
    return ret
    
def face_detect_demo(img):
    grey = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    grey = grey + 25
    faces = face_detector.detectMultiScale(grey, 1.1, 2)
    eye_imgs = []
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        print("x is %s y is %s, w is %s h is %s"%(x, y, w, h))
        roi_grey = grey[y:y+int(h*2/3), x:x+w]
        roi_img = img[y:y+int(h*2/3), x:x+w]
        # cv.imshow("roi", roi_img)
        eyes = eyes_detector.detectMultiScale(roi_grey, 1.1, 8)
        # rl = []
        for (ex, ey, ew, eh) in eyes:
            print("******************eye detected")
            eye = roi_img[ey:ey+eh, ex:ex+ew]
            print(type(eye))
            # get_eye = get_img(eye)
            rs_img = cv.resize(eye, (56,56))
            rh_img = np.reshape(rs_img, (3,56,56))
            eye_imgs.append(rh_img)
            cv.rectangle(roi_img, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)
    eye_imgs = np.array(eye_imgs)
    # ret = prediction(eye_imgs)
    cv.imshow("result", img)
    # cv.moveWindow("result", 600, 350)
    return eye_imgs


def take_action(pred):
    if pred == 0:
        gui.scroll(2)
        print("Down")
    if pred == 2:
        gui.scroll(-2)
        print("Up")
    
eye_model = load_model("NN/CNN006460985.model")

face_detector = cv.CascadeClassifier("/home/hawk/Downloads/opencv_data/data/haarcascades/haarcascade_frontalface_alt_tree.xml")
eyes_detector = cv.CascadeClassifier("/home/hawk/Downloads/opencv_data/data/haarcascades/haarcascade_eye.xml")

def main():
    active_target_app()
    
    capture = cv.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        eye_images = face_detect_demo(frame)
        print(eye_images.ndim)
        # print(eye_images==[])
        pred = prediction(eye_images)
        print("The prediction is :", pred)
        take_action(pred)
        k = cv.waitKey(50)
        if k == 27:
            break
    # cv.waitKey(0)
    print("we are our of here")
    cv.destroyAllWindows()

    
if __name__ == "__main__":
    main()