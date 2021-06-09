import unittest, json
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)

    def test_add_task_success(self):
        '''获取我的信息用例：/termianal/getMyInfo'''
    
        response = Test_Add_Task.http.get(
            '/termianal/getMyInfo')
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取我的信息失败')


if __name__ == '__main__':
    unittest.main()
