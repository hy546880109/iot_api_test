import requests
import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)

from config.config_test import Conf
from common.http_requests import HttpRequests
from common import logging_test
from common.retry import Retry
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod 
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_add_task_success(self):
        '''获取版本号用例：/ver/getUpgradePackage'''
        data = {
          "departmentId": "string",
          "type": 0,
          "ver": "string"
        }
        data = json.dumps(data)
        response = Test_Add_Task.http.post('/ver/getUpgradePackage', data=data)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取版本号失败')
        logging_test.log_test()
        logging_test.logging.info('接口返回:' + response.text)

if __name__ == '__main__':
    unittest.main()
