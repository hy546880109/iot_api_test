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
        '''导出锁授权信息成功用例：/key/authorize/export'''
        payload = {
          "lockName": "string",
          "name": "string",
          "pageNum": 0,
          "pageSize": 0,
          "startNum": 0,
          "status": 0,
          "total": 0,
          "userName": "string"
        }
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post(
            '/key/authorize/export', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        # self.assertEqual(str(0), str(response.json()['code']), '导出锁授权信息失败')


if __name__ == '__main__':
    unittest.main()
