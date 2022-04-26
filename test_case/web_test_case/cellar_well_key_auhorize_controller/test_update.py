import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
from common.http_requests import HttpRequests
from config.config_test import Conf

class Test_Add_Task(unittest.TestCase):

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

    def test_add_task_success(self):
        '''更新锁授权成功用例：/key/authorize/update'''
        payload = {
          "endAt": "2022-04-26 13:00:00",
          "id": 0,
          "keyId": 0,
          "name": "string",
          "startAt": "2022-04-26 12:00:00",
          "terminalNo": "string",
          "type": 0,
          "updateAt": "string",
          "updateBy": 0,
          "userId": 0
        }
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post(
            '/key/authorize/update', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '更新锁授权失败')


if __name__ == '__main__':
    unittest.main()
