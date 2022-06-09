import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)

from config.config_test import Conf
from common.http_requests import HttpRequests
from common.mysql_data import Mysql_connet

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


    def test_add_task_success(self):
        '''维护人员通过窖井锁跳转到申请授权用例：/key/authorize/skipApply'''
        payload = {
          "endAt": "2022-05-01 12:00:00",
          "keyId": self.mysql.key_id,
          "startAt": "2022-05-01 11:00:00",
          "terminalNo": self.mysql.terminal_no
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(
            '/key/authorize/skipApply', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '维护人员通过窖井锁跳转到申请授权失败')


if __name__ == '__main__':
    unittest.main()
