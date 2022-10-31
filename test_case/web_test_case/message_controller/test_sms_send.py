import unittest
import json
import os
import sys


def add_syspath():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))))
    sys.path.append(path)
add_syspath()
from config.config_test import Conf
from common.http_requests import HttpRequests
from common import logging_test
from common.retry import Retry
from common.doc_value import doc_parameter
uri = '/sms/send'
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_add_task_success(self):
        '''发送短信成功用例：{}{}'''
        payload = {
            "validateCode": "98",
            "phones": [
                "13285426551",
                "18615035648"
            ],
            "terminalNo": "tempor in",
            "alarmType": "sunt ea in exercitation",
            "type": 32724742
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(
            uri, data=payload)
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '-接口返回:' + response.text)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '发送短信失败')


if __name__ == '__main__':
    unittest.main()
