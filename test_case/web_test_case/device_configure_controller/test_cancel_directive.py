from common.mysql_data import Mysql_connet
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
        cls.mysql = Mysql_connet("device")
        cls.device_id = cls.mysql.select_sql("select id from t_cellar_well")

    def test_add_task_success(self):
        '''取消设备配置参数成功用例：/device/config/cancelDirective'''
        payload = [
            Test_Add_Task.device_id
        ]
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(
            '/device/config/cancelDirective', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '取消设备配置参数失败')


if __name__ == '__main__':
    unittest.main()
