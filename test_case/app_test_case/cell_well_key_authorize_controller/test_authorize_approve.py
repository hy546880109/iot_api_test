import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common.login_token import get_token
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
        '''钥匙授权审批用例：/key/authorize/approve'''
        payload = {
          "id": self.mysql.authorize_id,
          "mobile": "string",
          "remark": "string",
          "status": 0
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(
            '/key/authorize/approve', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '钥匙授权审批失败')


if __name__ == '__main__':
    unittest.main()
