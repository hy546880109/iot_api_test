import unittest
import json
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_add_task_success(self):
        '''发送短信成功用例：/sms/send'''
        payload = {
            "validateCode": "98",
            "phones": [
                "13285426551",
                "18615035648"
            ],
            "terminalNo": "tempor in",
            "alarmType": "sunt ea in exercitation",
            "type": 32724742
        }
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post(
            '/sms/send', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '发送短信失败')


if __name__ == '__main__':
    unittest.main()
