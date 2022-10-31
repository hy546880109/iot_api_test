import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.mysql_data import Mysql_connet
from common.retry import Retry
from common import logging_test
from common.doc_value import doc_parameter
uri = '/key/authorize/approve'
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_device()
        cls.mysql.insert_user()


    @classmethod
    def tearDownClass(cls) -> None:
        # cls.mysql.delete_device()
        # cls.mysql.delete_user()
        cls.mysql.close()

    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_add_task_success(self):
        '''钥匙授权审批用例：{}{}'''
        payload = {
          "id": self.mysql.authorize_id,
          "mobile": "string",
          "remark": "string",
          "status": 0
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(
            uri, data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '钥匙授权审批失败')
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '-接口返回:' + response.text)

if __name__ == '__main__':
    unittest.main()
