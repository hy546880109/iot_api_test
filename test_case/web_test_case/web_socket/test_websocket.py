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
from common.retry import Retry
from common import logging_test
from common.doc_value import doc_parameter

user_id = Mysql_connet('user').user_id
@Retry
class Test_websoket(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.ws = Conf.TEST_WS_URL.value
        cls.mysql = Mysql_connet('user')
        cls.mysql.insert_user()
        
    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_user()
        cls.mysql.close()
    @doc_parameter(Conf.TEST_WS_URL.value,user_id)
    def test_websoket(self):
        '''websocket 消息推送:  {}{}'''
        url = self.ws + str(self.mysql.user_id)
        # url = 'ws://106.52.198.240:8003/websocket/1377074593995628546'  
        websocket.enableTrace(True)  # 打开跟踪，查看日志
        ws = create_connection(url)  # 创建连接
        self.assertEqual(101, ws.getstatus(), 'websocket连接错误')  # 断言连接状态
        # ws.settimeout(10)   #设置超时时间
        ws.shutdown()  # 关闭连接
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_WS_URL.value  + str(user_id) +'-接口连接状态:' + str(ws.getstatus()))

if __name__ == '__main__':
    unittest.main()
