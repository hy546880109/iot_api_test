import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from common.login_token import get_token
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
        """地址列表成功用例: /address/list"""
        payload = {
            "name": "长沙",
            "pid": None,
            "id": None,
            "pageNum": 1,
            "pageSize": 10
        }
        payload = json.dumps(payload)
        # headers = {'Content-Type': 'application/json', 'token': get_token()}
        response = Test_Get_Index.http.post('/address/list', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '地址列表失败')


if __name__ == '__main__':
    unittest.main()
