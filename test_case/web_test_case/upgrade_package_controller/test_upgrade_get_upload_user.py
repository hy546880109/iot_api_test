import requests
import demjson
import json
import os
import sys
import unittest
path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from common.http_requests import HttpRequests
from config.config_test import Conf

# payload = {

# }


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_add_task_success(self):
        """获取包上传人用例：/upgrade/package/getUploadUser"""
        response = Test_Add_Task.http.post('/upgrade/package/getUploadUser')
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取包上传人失败')
        


if __name__ == '__main__':
    unittest.main()
