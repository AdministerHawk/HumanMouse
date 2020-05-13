#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:24:42 2020

@author: hawk
"""

import cv2

import time

 

cap=cv2.VideoCapture(0)

cap.set(3,900)

cap.set(4,900)

while(cap.isOpened()):

    ret_flag, Vshow = cap.read()

    cv2.imshow('Capture', Vshow)

    k=cv2.waitKey(1)
    
    if k==ord('s'):

        #通过s键保存图片，并退出。
        cv2.imwrite("image/image2.jpg",Vshow)
        print('222222')

        print(cap.get(3))

        print(cap.get(4))

    elif k==ord('q'):

        print('完成')
        cap.release()
        break

cv2.destroyAllWindows()
    #print('摄像头捕获成功')

    # pass

# time.sleep(1)

#cap.release()


#cv2.destoryAllWindows()
#"""
#:param
#    无
#:return
#    无
#功能：调用笔记本摄像头获取视频图片
#"""""
#import numpy as np
#import cv2
##调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
#cap=cv2.VideoCapture(0)
#while True:
#    #从摄像头读取图片
#    sucess,img=cap.read()
##    #转为灰度图片
##    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
##    #显示摄像头，背景是灰度。
##    cv2.imshow("img",gray)
#    cv2.imshow("img",img)
#    #保持画面的持续。
#    k=cv2.waitKey(1)
#    if k == 27:
#        #通过esc键退出摄像
#        cv2.destroyAllWindows()
#        break
#    elif k==ord("s"):
#        #通过s键保存图片，并退出。
#        cv2.imwrite("image2.jpg",img)
#        cv2.destroyAllWindows()
#        break
##关闭摄像头
#cap.release()