# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例

from websocket import create_connection

class WsWebsocket(object):
    def __init__(self, url):
        self.url = url
        self.ws = create_connection(self.url)

    # ws协议的消息发送
    def send(self, params):
        '''
        :param params: websocket接口的参数

        :return: 访问接口的返回值
        '''
        self.ws.send(params)
        res = self.ws.recv()
        return res

    def __del__(self):
        '''
        :return:
        '''
        self.ws.close()
