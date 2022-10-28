
import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
from config.config_test import Conf
from common.http_requests import HttpRequests
from common import logging_test
from common.retry import Retry
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_user()
        cls.mysql.insert_device()
    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_user()
        cls.mysql.delete_device()
        cls.mysql.close()

    def test_add_task_success(self):
        '''新增安裝步驟用例：/device/install/insert'''
        data = {
          "model": "string",
          "status": 0,
          "step": 0,
          "terminalNo": self.mysql.terminal_no
        }
        data = json.dumps(data)
        response = Test_Add_Task.http.post('/device/install/insert',data=data)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '新增安裝步驟失败')
        logging_test.log_test()
        logging_test.logging.info('接口返回:' + response.text)


if __name__ == '__main__':
    unittest.main()
