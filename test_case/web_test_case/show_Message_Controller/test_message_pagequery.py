import unittest,json,logging
import os,sys
path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

from common import logging_test
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.doc_value import doc_parameter
uri = '/show/message/pageQuery'
class Test_message_pagequery(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_success(self):
        """查询设备下的所有推送信息成功用例：{}{}"""
        data = {
          "endDate": "string",
          "name": "string",
          "pageNum": 0,
          "pageSize": 0,
          "startDate": "string",
          "terminalNo": "string"
        }
        data = json.dumps(data)
        response = Test_message_pagequery.http.post(uri,data=data)
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '-接口返回:' + response.text)
        self.assertEqual(200,response.status_code, '状态码返回非200')
        self.assertEqual(0,response.json()['code'], 'code返回非0')

if __name__ == '__main__':
    unittest.main()