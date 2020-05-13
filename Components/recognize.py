#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:01:26 2020

@author: hawk
"""

# encoding:utf-8

import requests
import base64

'''
手势识别
'''

def recognize():
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/gesture"
    # 二进制方式打开图片文件
    f = open('/home/hawk/Desktop/ML/myproject/image/image2.jpg', 'rb')
    print("********************")
    print(type(f))
    img = base64.b64encode(f.read())
    print("********************")
    print(type(img))
    params = {"image":img}
    access_token = '24.3e8890b23afdc2e06edcda6913aa8efc.2592000.1582281902.282335-18332846'
    #access_token = '[调用鉴权接口获取的token]
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())
    
    result_dict = response.json()
    print(result_dict['result'])
    for item in result_dict['result']:
        print(item['classname'])


recognize()