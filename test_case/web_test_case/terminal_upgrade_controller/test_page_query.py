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
        """获取设备升级列表成功用例：/device/upgrade/pageQuery"""
        payload = {
            "departmentId": 1382562817882931201,
            "pageSize": 1,
            "mac": None,
            "softwareVer": None,
            "deviceType": 0,
            "hardwareVer": None,
            "addrId": "19",
            "batteryNum": None,
            "isOnline": 1,
            "pageNum": 10,
            "upgradeStatus": None,
            "terminalNo": None
        }
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post('/device/upgrade/pageQuery', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取设备升级列表失败')


if __name__ == '__main__':
    unittest.main()
