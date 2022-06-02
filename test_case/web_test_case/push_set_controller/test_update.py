import os,sys


def add_syspath():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))))
    sys.path.append(path)
add_syspath()

from common.mysql_data import Mysql_connet
import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_device()
        cls.mysql.insert_user()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_device()
        cls.mysql.delete_user()

    def test_add_task_success(self):
        '''更新任务成功用例：/push/set/update'''
        payload = {
        "id": self.mysql.push_set_id,
        'departmentId': self.mysql.department_id,
        'messageType': "1",
        'pushType': "1,1,0",
        'userId': self.mysql.user_id
        }
        payload = json.dumps(payload)

        response = Test_Add_Task.http.post('/push/set/update',data=payload)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'更新任务失败')


if __name__ == '__main__':
    unittest.main()
