import unittest, json
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.login_token import get_token

class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)

    def test_add_task_success(self):
        '''获取资产用例：/capital/getCapitalByTerminalNoOrSensorNo'''
        payload = {"terminalNo": "888888810"}
        payload = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post('/capital/getCapitalByTerminalNoOrSensorNo', data=payload,headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取资产失败')


if __name__ == '__main__':
    unittest.main()
