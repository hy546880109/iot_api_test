import unittest,os,sys,json
from wsgiref import headers

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
from config.config_test import Conf
from common.http_requests import HttpRequests
from common import logging_test
from common.retry import Retry
from common.doc_value import doc_parameter
uri = '/key/authorize/getTerminalInfoById'
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('user')
        cls.mysql.insert_user()
    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_add_task_success(self):
        '''查看钥匙关联的锁信息用例：{}{}'''
        params = {'id':self.mysql.key_id}
        response = Test_Add_Task.http.get(uri,params=params)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '查看钥匙关联的锁信息失败')
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '-接口返回:' + response.text)

if __name__ == '__main__':
    unittest.main()
