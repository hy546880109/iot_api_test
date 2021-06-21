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
        """成功用例: /address/sonList"""
        payload = {
            "pid": 0
        }
        response = Test_Get_Index.http.get('/address/sonList', params=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取下属子地址列表失败')


if __name__ == '__main__':
    unittest.main()