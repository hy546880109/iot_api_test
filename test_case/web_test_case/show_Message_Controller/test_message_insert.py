import unittest
import json,logging
import os,sys

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

from common import logging_test
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.doc_value import doc_parameter
uri = '/show/message/insert'

class Test_message_insert(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_success(self):
        """新增消息推送模板成功用例: {}{}"""
        data = {
          "alarmAt": "2022-10-27 02:27:51.814Z",
          "content": "string",
          "createAt": "2022-10-27 02:27:51.814Z",
          "name": "string",
          "status": 0,
          "terminalNo": "string"
        }
        data = json.dumps(data)
        response = Test_message_insert.http.post(uri, data=data)
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '-接口返回:' + response.text)
        self.assertEqual(200,response.status_code,'响应码返回非200')
        self.assertEqual(str(0),str(response.json()['code']),'code返回非0')



if __name__ == "__main__":
    unittest.main()
