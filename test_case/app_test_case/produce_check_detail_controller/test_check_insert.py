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
        """新增生产记录成功用例: /produce/check/insert"""
        payload = {
          "batchNo": "string",
          "imsi": "string",
          "item": 0,
          "mac": "string",
          "softwareVer": "string",
          "status": 0,
          "subType": 0,
          "terminalNo": "string",
          "type": 0,
          "value": "string"
        }
        payload = json.dumps(payload)
        response = Test_Get_Index.http.post('/produce/check/insert', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '新增生产记录失败')


if __name__ == '__main__':
    unittest.main()
