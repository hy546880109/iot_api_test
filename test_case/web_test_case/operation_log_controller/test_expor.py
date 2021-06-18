from common.http_requests import HttpRequests
from config.config_test import Conf
import unittest
import os
import sys
import json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_add_task_success(self):
        '''导出用户操作日志成功用例：/operate/log/export'''
        payload = {
            "addrId": None,
            "createName": None,
            "departmentId": None,
            "logFrom": None,
            "logType": None,
            "operateType": None,
            "startDate": None,
            "endDate": None,
            "pageNum": 1,
            "pageSize": 10
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post('/operate/log/export', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '导出用户操作日志失败')


if __name__ == '__main__':
    unittest.main()
