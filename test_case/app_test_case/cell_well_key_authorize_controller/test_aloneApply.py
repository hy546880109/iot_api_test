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
        # cls.mysql.delete_device()
        # cls.mysql.delete_user()
        cls.mysql.close()


    def test_add_task_success(self):
        '''单独申请授权用例：/key/authorize/aloneApply'''
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
        headers = {
            'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post(
            '/key/authorize/aloneApply', data=payload,headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '单独申请授权失败')


if __name__ == '__main__':
    unittest.main()
