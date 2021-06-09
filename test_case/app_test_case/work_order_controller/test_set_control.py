import unittest
import json
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Get_Index(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)

    def test_get_index_success(self):
        """布/撤控成功用例: /work/order/setControl"""
        payload = {
            "controlStatus": 0,
            "duration": 3,
            "terminalNo": "888888810"
        }
        payload = json.dumps(payload)
        response = Test_Get_Index.http.post(
            '/work/order/setControl', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '布/撤控失败')


if __name__ == '__main__':
    unittest.main()
