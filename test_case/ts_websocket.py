# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例


import unittest
from websocket import create_connection
import websocket


class Test_websoket(unittest.TestCase):
    def test_websk(self):
        '''websocket 消息推送:  /socketServer/${userId} '''
        url = 'ws://10.10.100.184:9997/socketServer/528'  # websocket连接地址
        websocket.enableTrace(True)  # 打开跟踪，查看日志
        ws = create_connection(url)  # 创建连接
        print(ws.getstatus())  # 打印连接状态
        self.assertEqual(101, ws.getstatus(), 'websocket连接错误')  # 断言连接状态
        ws.settimeout(10)   #设置超时时间
        print(ws.gettimeout())  #获取超时时间
        # ws.shutdown()  # 关闭连接


if __name__ == '__main__':
    unittest.main()
