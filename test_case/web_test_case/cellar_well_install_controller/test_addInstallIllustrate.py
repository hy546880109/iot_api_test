import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.mysql_data import Mysql_connet
from common import logging_test
from common.retry import Retry
from common.doc_value import doc_parameter
uri = '/device/install/addInstallIllustrate'
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
    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_add_task_success(self):
        '''新增安装指令帮助文档成功用例：{}{}'''
        data = [
          {
            "deviceType": 0,
            "funcCheckItem": 0,
            "id": 0,
            "illustrate": "string",
            "serialNumber": 0,
            "type": 0,
            "url": "string"
          }
        ]
        data = json.dumps(data)
        response = Test_Add_Task.http.post(uri,data=data)
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '-接口返回:' + response.text)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'新增安装指令帮助文档失败')


if __name__ == '__main__':
    unittest.main()
