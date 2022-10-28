from email import header
import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.retry import Retry
from common import logging_test
@Retry
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
        '''获取所有钥匙信息用例：/key/getTerminalInfo'''
        params = {
          "id": self.mysql.authorize_id,
          "pageNum": 1,
          "pageSize": 1,
          "type": 3,
          "userId": self.mysql.user_id
        }
        params = json.dumps(params)
        response = Test_Add_Task.http.post('/key/getTerminalInfo',data=params)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取所有钥匙信息失败')
        logging_test.log_test()
        logging_test.logging.info('接口返回:' + response.text)


if __name__ == '__main__':
    unittest.main()
