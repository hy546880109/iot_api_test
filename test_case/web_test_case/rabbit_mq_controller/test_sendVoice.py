import requests
import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)

from config.config_test import Conf
from common.http_requests import HttpRequests

from common.retry import Retry
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod 
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_add_task_success(self):
        '''sendVoice用例：/mq/push/message/sendVoice'''
        data = {
          "address": "string",
          "alarmDate": "2022-04-26T03:52:25.882Z",
          "alarmType": "string",
          "messageType": 0,
          "phone": "string",
          "terminalNo": "string"
        }
        data = json.dumps(data)
        response = Test_Add_Task.http.post('/mq/push/message/sendVoice', data=data)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']), 'sendVoice失败')


if __name__ == '__main__':
    unittest.main()
