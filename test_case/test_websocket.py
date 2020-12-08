# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例


import unittest
from websocket import create_connection
import json

url = 'ws://10.10.100.184:9997/socketServer/'  # websocket连接地址，地址为虚拟地址
# websocket.enableTrace(True)                      #打开跟踪，查看日志
ws = create_connection(url)  # 创建连接
data = {"userId": 198}  # 测试数据

# new_data = json.dumps(data, ensure_ascii=False)  # 将data转化为字符串
ws.send(data)  # 发送请求
print(ws.recv())  # 打印服务器响应数据
ws.close()  # 关闭连接
