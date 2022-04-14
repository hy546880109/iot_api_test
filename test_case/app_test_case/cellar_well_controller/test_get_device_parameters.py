import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
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
        '''修改设备参数用例：/termianal/modifyDeviceParameters'''
        payload = {
    "wakeHeartbeat": 81691975,
    "waterLevel1": 40483546,
    "port": 95882002,
    "siltHeartbeat": -98993677,
    "terminalNo": "elit sunt consequat eu",
    "ch4": 74276084,
    "domain": "e.lfsro@qq.com",
    "sensorHeartbeat": -75433130,
    "ip": "74.210.160.79",
    "logNum": -53256683,
    "gasHeartbeat": 17431113,
    "openangle": -19900875,
    "siltHigh": 12089765,
    "waterLevel2": -27214844,
    "leanangle": -29060256
}
        payload = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json', 'token': get_token()}
        response = Test_Add_Task.http.post(
            '/termianal/modifyDeviceParameters', data=payload,headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '修改设备参数失败')


if __name__ == '__main__':
    unittest.main()
