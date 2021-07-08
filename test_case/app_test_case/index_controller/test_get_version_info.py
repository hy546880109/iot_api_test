import unittest
import json
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.login_token import get_token

class Test_Get_Index(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)

    def test_get_index_success(self):
        """获取版本号成功用例: /getVersionInfo"""
        headers = {'Content-Type': 'application/json', 'token': get_token()}
        response = Test_Get_Index.http.post('/getVersionInfo', headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取版本号失败')


if __name__ == '__main__':
    unittest.main()
