import unittest
import json
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)

    def test_add_task_success(self):
        '''获取设备参数用例：/termianal/getDeviceParameters'''
        palyload = {'terminalNo' : 888888810}
        response = Test_Add_Task.http.get(
            '/termianal/getDeviceParameters', params=palyload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取设备参数失败')


if __name__ == '__main__':
    unittest.main()
