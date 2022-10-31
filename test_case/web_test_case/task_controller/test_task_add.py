import requests
import demjson
import json
import os,sys
import unittest
path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests
from common import logging_test
from common.retry import Retry
from common.doc_value import doc_parameter
uri = '/task/add'
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod 
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_add_task_success(self):
        '''创建任务成功用例： {}{}'''
        payload  = {
        "alarmType": "2",
        "departmentId": 1382562817882931201,
        "taskReceive": "1377099431489548290",
        "remark": "",
        "selectDoPolicyDate": 0,
        "finsihFirishPolicyDate": 2
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(uri,data=payload)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '创建任务失败')
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '-接口返回:' + response.text)
        

if __name__ == '__main__':
    unittest.main()
