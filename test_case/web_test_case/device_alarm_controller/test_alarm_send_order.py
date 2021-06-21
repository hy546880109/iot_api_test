from common.mysql_data import Mysql_connet
import requests
import demjson
import json
import unittest
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.alarm_id = cls.mysql.select_sql("select id from t_device_alarm")
        
    def test_add_task_success(self):
        '''手动派单成功用例：/history/alarm/manualDistributeTask'''
        payload = {
            "alarmId": Test_Add_Task.alarm_id,
            "departmentId": 1382562817882931201,
            "level": 0,
            "prvFinishTime": "2021-05-21 12:25:56",
            "taskReceive": 1377074593995628546,
            "workSrc": 0,
            "workType": 0
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(
            '/history/alarm/manualDistributeTask', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '手动派单失败')


if __name__ == '__main__':
    unittest.main()