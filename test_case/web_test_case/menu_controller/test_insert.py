import json
import unittest
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_add_task_success(self):
        '''增加角色资源成功用例：/menu/insert'''
        payload = [
            {
                "owns": False,
                "roleId": 39590059,
                "menuId": 61918944
            },
            {
                "menuId": 87668902,
                "roleId": 42174822,
                "owns": True
            },
            {
                "roleId": 13223315,
                "menuId": 79588311,
                "owns": False
            }
        ]
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post('/menu/insert',data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '增加角色资源失败')


if __name__ == '__main__':
    unittest.main()
