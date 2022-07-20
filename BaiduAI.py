#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/10 11:13
# @Author  : hkiny
# @File    : BaiduAI.py
# @Software: win10 Tensorflow1.13.1 python3.10.0
# encoding:utf-8

import requests

def people_reg(self,img_path,group_id,user_id):


    '''
    人脸注册
    '''

    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add"

    params = "{\"image\":\"027d8308a2ec665acb1bdf63e513bcb9\",\"image_type\":\"FACE_TOKEN\",\"group_id\":\"group_repeat\",\"user_id\":\"user1\",\"user_info\":\"abc\",\"quality_control\":\"LOW\",\"liveness_control\":\"NORMAL\"}"
    access_token = '[调用鉴权接口获取的token]'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())