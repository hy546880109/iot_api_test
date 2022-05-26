# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例


import unittest,os,sys

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from websocket import create_connection
import websocket
from common.http_requests import HttpRequests
from common.mysql_data import Mysql_connet
from config.config_test import Conf

class Test_websoket(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.ws = Conf.TEST_WS_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('user')
        
    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.close()
        

    def test_websoket(self):
        '''websocket 消息推送:  /socketServer/${userId} '''
        url = self.ws + str(self.mysql.user_id)
        # url = 'ws://106.52.198.240:8003/websocket/1377074593995628546'  
        websocket.enableTrace(True)  # 打开跟踪，查看日志
        ws = create_connection(url)  # 创建连接
        # print(ws.getstatus())  # 打印连接状态
        self.assertEqual(101, ws.getstatus(), 'websocket连接错误')  # 断言连接状态
        # ws.settimeout(10)   #设置超时时间
        # print(ws.gettimeout())  #获取超时时间
        ws.shutdown()  # 关闭连接


if __name__ == '__main__':
    unittest.main()
