from tkinter import N
import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
from common.login_token import get_token
from common.http_requests import HttpRequests
from config.config_test import Conf

class Test_Device_List(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_device()
        cls.mysql.insert_user()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_device()
        cls.mysql.delete_user()
        cls.mysql.close()        


    def test_device_list_success(self):
        '''导出锁信息成功用例：/key/export'''
        payload = {
          "mac": "F2:A0:25:6D:03:56",
          "name": "ss",
          "pageNum": 1,
          "pageSize": 1,
          "startNum": 1,
          "total": 1,
          "userName": "string"
        }
        response = Test_Device_List.http.get('/key/export', params=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '导出锁信息失败')


if __name__ == '__main__':
    unittest.main()
