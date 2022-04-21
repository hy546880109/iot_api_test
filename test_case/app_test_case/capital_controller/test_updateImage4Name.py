import time
import unittest,os,sys,json

from pymysql import NULL

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common.login_token import get_token
from common.mysql_data import Mysql_connet
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_device()
        cls.mysql.insert_user()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_device()
        cls.mysql.delete_user()
        cls.mysql.close()    

    def test_add_task_success(self):
        '''更新设备名称用例：/capital/updateImage4Name'''

        payload = {
          "id":self.mysql.device_id,
          "images1": "string",
          "images2": "string",
          "images3": "string",
          "images4": "string",
          "name": "string"
        }

        headers = {'Content-Type': 'application/json','Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7','Accept-Encoding': 'gzip, deflate','X-Requested-With': 'com.antancorp.iot.device.service.impl','Accept': 'application/json'}
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(
            '/capital/updateImage4Name', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '更新设备名称失败')


if __name__ == '__main__':
    unittest.main()
