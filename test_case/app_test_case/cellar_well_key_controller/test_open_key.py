import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)

from config.config_test import Conf
from common.http_requests import HttpRequests
from common.mysql_data import Mysql_connet
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
        '''蓝牙开锁，成功调用该接口，锁状态设置为 开锁状态用例：/key/bluetooth/open/key'''
        payload = {
          "terminalNo": self.mysql.terminal_no
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(
            '/key/bluetooth/open/key', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '蓝牙开锁，成功调用该接口，锁状态设置为 开锁状态失败')
        logging_test.log_test()
        logging_test.logging.info('接口返回:' + response.text)


if __name__ == '__main__':
    unittest.main()
