from common.http_requests import HttpRequests
from config.config_test import Conf
from common.mysql_data import Mysql_connet
import unittest
import os
import sys
import json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_user()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_user()
        cls.mysql.close()

    def test_add_task_success(self):
        """新增或者更新部门信息成功用例：/department/saveOrUpdate"""
        payload = {
            "addrId": 440305,
            "name": "b222222222222",
            "remark": "in ut qui cillum veniam",
            "id": self.mysql.department_id,
            "pid": 0
        }
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post(
            '/department/saveOrUpdate', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '新增或者更新部门信息失败')


if __name__ == '__main__':
    unittest.main()
