import requests
import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common import logging_test
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.doc_value import doc_parameter
from common.retry import Retry
uri = '/mq/push/message/sendVoice'
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod 
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_add_task_success(self):
        '''sendVoice用例：{}{}'''
        data = {
          "address": "string",
          "alarmDate": "2022-04-26T03:52:25.882Z",
          "alarmType": "string",
          "messageType": 0,
          "phone": "string",
          "terminalNo": "string"
        }
        data = json.dumps(data)
        response = Test_Add_Task.http.post(uri, data=data)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']), 'sendVoice失败')
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '-接口返回:' + response.text)

if __name__ == '__main__':
    unittest.main()
