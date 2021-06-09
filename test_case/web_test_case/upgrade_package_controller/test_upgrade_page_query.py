import json
import os, sys
import unittest

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_add_task_success(self):
        """获取升级包列表用例：/upgrade/package/pageQuery"""
        payload = {
        "createBy": 1377074593995628546,
        "endDate": "2021-04-15",
        "name": "V1.0",
        "pageNum": 1,
        "pageSize": 1,
        "startDate": "2021-03-15",
        "type": 0,
        "ver": "1.0"
        }
        response = Test_Add_Task.http.post('/upgrade/package/pageQuery', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取升级包列表失败')


if __name__ == '__main__':
    unittest.main()
