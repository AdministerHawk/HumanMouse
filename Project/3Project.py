#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:13:11 2020

@author: hawk
"""


import pyautogui

# 获取当前屏幕分辨率
screenWidth, screenHeight = pyautogui.size()

# 获取当前鼠标位置
currentMouseX, currentMouseY = pyautogui.position()

# 2秒钟鼠标移动坐标为100,100位置  绝对移动
pyautogui.moveTo(200, 180,2)

# 鼠标左击一次
pyautogui.click()


import cv2


from aip import AipBodyAnalysis
APP_ID = "18332846"
API_KEY = "qKEHoRG0SRL08aUoWnadSNN5"
SECRET_KEY = "s4Iu3wPEf2o7vtWulHiNn0Iuxps22tkf"

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

import numpy as np
from PIL import Image
def myrecognize(img): 
    # image = get_file_content('image/image2.jpg')
    
    """ 调用手势识别 """
    image = Image.fromarray(np.uint8(img)).tobytes()
    
    result_dict = client.gesture(image)
    rl = []    
    for item in result_dict['result']:
        rl.append(item['classname'])
    return rl


#cap.set(3,900)
#
#cap.set(4,900)

imgCount = 0
#speed = 1
frameCount = 0
trigger = 10
reduceLegacy = 0
triggerLevel = 3

cap=cv2.VideoCapture(0)

while(cap.isOpened()):
    ret_flag, Vshow = cap.read()
    Vshow = cv2.flip(Vshow, 1)
    cv2.namedWindow("Capture", cv2.WINDOW_AUTOSIZE)
    cv2.moveWindow("Capture", 1000, 100)
    cv2.imshow('Capture', Vshow)

    k=cv2.waitKey(80)
    frameCount +=1
    print("frame count", frameCount)
    print("Trigger:", trigger)
    print("reduceLegacy:", reduceLegacy)
    if (frameCount == trigger):
        frameCount = 0
        imgCount +=1
        
        if (trigger ==  triggerLevel):
            reduceLegacy += 1
            
        # cv2.imwrite("image/image2.jpg",Vshow)
        print('take image')
    
        rl = myrecognize(Vshow)
        if ('One' in rl):
            pyautogui.scroll(2)
            trigger = triggerLevel
    #        speed = 0.01
            print("up")
            if (reduceLegacy == 5):
                trigger = 10
                reduceLegacy = 0
#        elif ('Thumb_down' in rl):
        elif ('Two' in rl):
            pyautogui.scroll(-2)
            trigger = triggerLevel
    #        speed = 0.01
            print("down")
            if (reduceLegacy == 5):
                trigger = 10
                reduceLegacy = 0            
        elif ('Five' in rl):
            cap.release()
            print("The total number take is:",imgCount)
            print("close")
            break
        elif (reduceLegacy == 5):
            trigger = 10
            reduceLegacy = 0
        else:
            trigger = 10
#            speed = 1

cv2.destroyAllWindows()
