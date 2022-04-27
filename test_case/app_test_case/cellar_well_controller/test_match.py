import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from common.login_token import get_token
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)

    def test_add_task_success(self):
        '''网关跟传感器蓝牙配对用例：/bluetooth/match'''
        payload = {
            "macGateway": "sint reprehenderit tempor eiusmod nisi",
            "macSensor": "ea consequat exercitation",
            "bindStatus": 0
        }
        payload = json.dumps(payload)
    
        response = Test_Add_Task.http.post(
            '/bluetooth/match', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '网关跟传感器蓝牙配对失败')


if __name__ == '__main__':
    unittest.main()
