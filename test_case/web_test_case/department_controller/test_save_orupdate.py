import unittest, os, sys, json

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

    def test_add_task_success(self):
        """新增或者更新部门信息成功用例：/department/saveOrUpdate"""
        payload = {
            "addrId": 110101,
            "name": "b",
            "remark": "in ut qui cillum veniam",
            "id": 1382562817882931201,
            "pid": 0
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post('/department/saveOrUpdate', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '新增或者更新部门信息失败')


if __name__ == '__main__':
    unittest.main()
