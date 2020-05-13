#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 17:05:31 2020

@author: hawk
"""

from aip import AipBodyAnalysis
APP_ID = "18332846"
API_KEY = "qKEHoRG0SRL08aUoWnadSNN5"
SECRET_KEY = "s4Iu3wPEf2o7vtWulHiNn0Iuxps22tkf"

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('image/image2.jpg')

""" 调用手势识别 """
result_dict = client.gesture(image)

print(result_dict['result'])
for item in result_dict['result']:
    print(item['classname'])
