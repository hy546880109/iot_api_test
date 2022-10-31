import requests
import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from common import logging_test
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.doc_value import doc_parameter
uri = '/upgrade/package/getSensorSoftwareVer'

from common.retry import Retry
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod 
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_add_task_success(self):
        '''获取传感器软件版本号用例：{}{}'''
        payload = {
            "type": -20942696,
            "createAt": "2010-12-09T08:35:49.116Z",
            "deviceType": 15291067,
            "size": "laborum ex do",
            "url": "http://kmytb.ye/lvgs",
            "ver": "eu dolor eiusmod",
            "name": "传约物参",
            "remark": "aliquip esse"
        }

        response = Test_Add_Task.http.post(uri,data=payload)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取传感器软件版本号失败')
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '-接口返回:' + response.text)

if __name__ == '__main__':
    unittest.main()
