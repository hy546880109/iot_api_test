from common.http_requests import HttpRequests
from config.config_test import Conf
import json
import unittest


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_add_task_success(self):
        '''自动派单成功用例：/history/alarm/autoDistributeTask'''
        payload = {
            "taskReceive": "1377099431489548290",
            "workSrc": 0,
            "prvFinishTime": "2021-04-21 12:00:01",
            "level": 1,
            "workType": 0,
            "departmentId": 1387731832590778370,
            "alarmId": 1391946012344676123
        }

        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(
            '/history/alarm/autoDistributeTask', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '派单失败')


if __name__ == '__main__':
    unittest.main()
