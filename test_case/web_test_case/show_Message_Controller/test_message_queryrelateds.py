import unittest,json,logging
import os,sys
path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

from common import logging_test
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.doc_value import doc_parameter
uri = '/show/message/queryRelateds'
class Test_message_queryrelateds(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_success(self):
        """查询消息推送模板信息成功用例：{}{}"""
        data = {
          "flag": 0,
          "name": None,
          "pageNum": 1,
          "pageSize": 10,
          "status": None,
          "terminalNo": None,
          "type": None
        }
        data = json.dumps(data)
        response = Test_message_queryrelateds.http.post(uri, data=data)
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '-接口返回:' + response.text)
        self.assertEqual(200, response.status_code, '状态码返回非200')
        self.assertEqual(0, response.json()['code'], 'code返回非0')


if __name__ == '__main__':
    unittest.main()