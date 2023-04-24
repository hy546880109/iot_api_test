import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
from common.http_requests import HttpRequests
from config.config_test import Conf
from common.retry import Retry
from common import logging_test
from common.doc_value import doc_parameter
uri = '/2/service/property/getByRelateId'
title = '获取该服务下的所有属性和命令'
@Retry
class Test_Device_List(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    @doc_parameter(title,Conf.TEST_URL.value,uri)
    def test_device_list_success(self):
        '''{}成功用例：{}{}'''
        payload = {'relateId':1}
        response = Test_Device_List.http.get(uri, params=payload)
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + title + '-接口返回:' + response.text)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '{}失败'.format(title))


if __name__ == '__main__':
    unittest.main()
