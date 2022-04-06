import requests
import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

from config.config_test import Conf
from common.http_requests import HttpRequests


payload  = {
    "type": -20942696,
    "createAt": "2010-12-09T08:35:49.116Z",
    "deviceType": 15291067,
    "size": "laborum ex do",
    "url": "http://kmytb.ye/lvgs",
    "ver": "eu dolor eiusmod",
    "name": "传约物参",
    "remark": "aliquip esse"
}


class Test_Add_Task(unittest.TestCase):

    @classmethod 
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_add_task_success(self):
        '''获取传感器软件版本号用例：/upgrade/package/getSensorSoftwareVer'''
        headers = {'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post('/upgrade/package/getSensorSoftwareVer',data=payload, headers=headers)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取传感器软件版本号失败')


if __name__ == '__main__':
    unittest.main()
