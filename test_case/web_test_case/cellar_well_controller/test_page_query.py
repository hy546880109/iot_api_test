import json
import unittest
import os
import sys

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from common.http_requests import HttpRequests
from config.config_test import Conf

class Test_Device_List(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_device_list_success(self):
        '''获取窖井列表信息成功用例：/device/pageQuery'''
        payload = {
            "no": None,
            "isOnline": None,
            "departmentId": None,
            "status": None,
            "coverType": None,
            "terminalNo": None,
            "controlStatus": None,
            "startDate": None,
            "endDate": None,
            "addrId": None,
            "hardwareVer": None,
            "subType": None,
            "pageSize": 10,
            "bluetoothStatus": None,
            "pageNum": 1,
            "batteryNum": None,
            "semaphore": None
        }

        payload = json.dumps(payload)
        response = Test_Device_List.http.post('/device/pageQuery', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取窖井列表信息失败')


if __name__ == '__main__':
    unittest.main()
