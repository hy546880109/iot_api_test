import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

import unittest
import json
from config.config_test import Conf
from common.http_requests import HttpRequests

from common.retry import Retry
@Retry
class Test_Get_Index(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)

    def test_get_index_success(self):
        """版本一致性检测成功用例: /produce/check/isVerSame"""
        payload = {
          "hardware": "string",
          "software": "string",
          "subType": 0,
          "type": 0
        }
        payload = json.dumps(payload)
        response = Test_Get_Index.http.post('/produce/check/isVerSame', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '版本一致性检测失败')


if __name__ == '__main__':
    unittest.main()
