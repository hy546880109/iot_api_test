from common.http_requests import HttpRequests
from config.config_test import Conf
import requests
import demjson
import json
import os
import sys
import unittest
path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_add_task_success(self):
        '''任务管理用例： /task/updateStatus'''
        payload = {
            'id': 2,
            'status': 1
        }
        response = Test_Add_Task.http.get('/task/updateStatus', params=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '任务管理失败')


if __name__ == '__main__':
    unittest.main()
