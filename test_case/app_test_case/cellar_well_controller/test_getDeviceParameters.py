import unittest,os,sys,json
from wsgiref import headers

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.login_token import get_token

class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_device()
    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_device()
        cls.mysql.close() 
    
    def test_add_task_success(self):
        '''获取设备参数用例：/terminal/getDeviceParameters'''
        params = {'terminalNo':self.mysql.terminal_no}
        response = Test_Add_Task.http.get('/terminal/getDeviceParameters', params=params)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取设备参数失败')


if __name__ == '__main__':
    unittest.main()
