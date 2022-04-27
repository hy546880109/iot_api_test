import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)

from common.login_token import get_token
from common.http_requests import HttpRequests
from config.config_test import Conf
import requests
import json

class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_add_task_success(self):
        '''上传升级包成功用例：/upgrade/package/insert'''
        payload = {
          "id": "",
          "name": "iWellGatewayV1.0.0.bin",
          "remark": "iWellGatewayV1.0.0",
          "size": 76696,
          "type": "0",
          "url": "https://antian-iot-oss.obs.cn-south-1.myhuaweicloud.com:443/5a5cf672bb4540c1b7bcc362493877e6.bin",
          "ver": "iWellGatewayV1.0.0"
        }
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json','token': get_token()}
        response = Test_Add_Task.http.post(
            '/upgrade/package/insert', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '上传升级包失败')


if __name__ == '__main__':
    unittest.main()
