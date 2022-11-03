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
uri = '/key/authorize/aloneApply'
title = '单独申请授权'
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
        cls.mysql.delete_device()
        cls.mysql.delete_user()
        cls.mysql.close()

    @doc_parameter(title,Conf.TEST_URL.value,uri)
    def test_add_task_success(self):
        '''{}成功用例：{}{}'''
        payload = {
          "endAt": "2022-05-01 12:00:00",
          "id": 0,
          "keyId": self.mysql.key_id,
          "name": "string",
          "startAt": "2022-05-01 12:00:00",
          "terminalNo": self.mysql.terminal_no,
          "type": 0,
          "updateAt": "2022-05-01 12:00:00",
          "updateBy": 0,
          "userId": self.mysql.user_id
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(
            uri, data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '{}失败'.format(title))
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '-接口返回:' + response.text)

if __name__ == '__main__':
    unittest.main()
