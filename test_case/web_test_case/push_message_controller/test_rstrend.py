from cgi import parse_multipart
import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.mysql_data import Mysql_connet
from common import logging_test
from common.retry import Retry
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('user')
        cls.mysql.insert_user()
    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_user()
        cls.mysql.close()
    
    def test_add_task_success(self):
        '''推送走势图成功用例：/stat/push/rstrend'''
        response = Test_Add_Task.http.get('/stat/push/rstrend')
        logging_test.log_test()
        logging_test.logging.info('接口返回:' + response.text)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'推送走势图失败')


if __name__ == '__main__':
    unittest.main()
