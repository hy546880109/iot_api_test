import json
import unittest
import os,sys


def add_syspath():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))))
    sys.path.append(path)
add_syspath()
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.md5 import Md5_add


class Test_Auto_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_auto_task_success(self):
        '''获取自动派单列表成功用例: /task/pageQuery'''
        payload = {
            "endDate": "1996-12-22",
            "startDate": "1978-06-23",
            "createBy": 1377074593995628546,
            "departmentId": 23,
            "taskReceive": "1377099431489548290",
            "pageSize": 1,
            "pageNum": 2
        }
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = Test_Auto_Task.http.post('/task/pageQuery', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取自动派单列表失败')


if __name__ == '__main__':
    unittest.main()
