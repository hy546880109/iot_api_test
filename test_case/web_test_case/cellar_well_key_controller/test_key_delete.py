import unittest,os,sys

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
from common.http_requests import HttpRequests
from config.config_test import Conf
from common.retry import Retry
from common import logging_test
from common.doc_value import doc_parameter
uri = '/key/delete'
@Retry
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

    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_device_list_success(self):
        '''删除锁成功用例：{}{}'''
        payload = {
          'id':self.mysql.device_id
        }
        response = Test_Device_List.http.get(uri, params=payload)
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '-接口返回:' + response.text)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '删除锁失败')


if __name__ == '__main__':
    unittest.main()
