from common.mysql_data import Mysql_connet
from common.http_requests import HttpRequests
from config.config_test import Conf
import json
import unittest


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.alarm_id = cls.mysql.select_sql("select id from t_device_alarm")

    def test_add_task_success(self):
        '''自动派单成功用例：/history/alarm/autoDistributeTask'''
        payload = [
            Test_Add_Task.alarm_id
        ]

        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post(
            '/history/alarm/autoDistributeTask', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '派单失败')


if __name__ == '__main__':
    unittest.main()
