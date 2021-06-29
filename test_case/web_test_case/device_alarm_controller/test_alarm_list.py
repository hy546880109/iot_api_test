from common.mysql_data import Mysql_connet
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
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_device()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_device()
        cls.mysql.close()


    def test_add_task_success(self):
        '''获取历史报警列表成功用例：/history/alarm/historyAlarmTaskPageQuery'''
        payload = {
            "alarmStartDate": "1998-08-13",
            "departmentId": 25354113,
            "status": 48674073,
            "terminalNo": "sunt",
            "pageNum": 1,
            "dispatchStatus": 72003994,
            "addrId": 74719650,
            "alarmType": 48581154,
            "alarmEndDate": "1977-07-11",
            "pageSize": 1,
            "dissolveStartDate": "1981-06-21",
            "dissolveEndDate": "2002-09-21"
        }
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post(
            '/history/alarm/historyAlarmTaskPageQuery', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取历史报警失败')


if __name__ == '__main__':
    unittest.main()
