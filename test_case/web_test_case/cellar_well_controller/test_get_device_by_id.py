import unittest,os,sys,json,logging

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
from config.config_test import Conf
from common.http_requests import HttpRequests
from common import logging_test
from common.doc_value import doc_parameter
from common.retry import Retry
uri = '/device/getDeviceById'
@Retry
class Test_get_device(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_device()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_device()
        cls.mysql.close()        
    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_get_device_success(self):
        """获取窖井详情成功用例：{}{}"""
        payload = {'id': self.mysql.device_id ,
        'no': self.mysql.no
        }
        response = Test_get_device.http.get(uri, params=payload)
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '-接口返回:' + response.text)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取窖井详情失败')


if __name__ == '__main__':
    unittest.main()
