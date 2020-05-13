#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 18:42:00 2020

@author: hawk
"""

# encoding:utf-8
import requests 

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=qKEHoRG0SRL08aUoWnadSNN5&client_secret=s4Iu3wPEf2o7vtWulHiNn0Iuxps22tkf'
response = requests.get(host)
if response:
    print(response.json())