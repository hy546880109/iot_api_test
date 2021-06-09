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
        '''上传升级包成功用例：/upgrade/package/insert'''
        payload = {
            "url": "http://www.baidu.com",
            "type": 0,
            "createAt": "2000-12-17 07:14:18",
            "remark": "第一次發佈版本",
            "ver": "1.0",
            "size": 531,
            "deviceType": 0,
            "name": "app"
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(
            '/upgrade/package/insert', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '上传升级包失败')


if __name__ == '__main__':
    unittest.main()
