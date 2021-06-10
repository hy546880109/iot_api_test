import json
import unittest
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_add_task_success(self):
        '''报警列表导出成功用例：/history/alarm/export'''
        payload = {
            "terminalNo": "voluptate eiusmod id enim exercitation",
            "alarmStartDate": "2003-08-07",
            "alarmType": 96222169,
            "addrId": 78584975,
            "departmentId": 88120510,
            "dissolveEndDate": "2015-04-06",
            "alarmEndDate": "1997-01-19",
            "dissolveStartDate": "2003-04-14",
            "status": 38520350,
            "pageSize": 64503461,
            "pageNum": 84387936,
            "dispatchStatus": 68933037
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(
            '/history/alarm/export', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '报警列表导出失败')


if __name__ == '__main__':
    unittest.main()
