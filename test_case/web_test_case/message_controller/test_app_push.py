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
        '''APP推送成功用例：/app/push'''
        payload = {
            "notificationAlert": "Excepteur id est incididunt voluptate",
            "registrationId": "22",
            "notificationTitle": "毛走观自"
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(
            '/app/push', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), 'APP推送失败')


if __name__ == '__main__':
    unittest.main()
