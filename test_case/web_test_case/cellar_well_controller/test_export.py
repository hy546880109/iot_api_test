from config.config_test import Conf
from common.http_requests import HttpRequests
import json
import unittest
import os
import sys

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)


class Test_Export(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_export_success(self):
        '''导出窖井列表信息成功用例：/device/export'''
        payload = {
            "controlStatus": 0,
            "no": "888888831",
            "addrId": 440305,
            "bluetoothStatus": "1",
            "terminalNo": "8888888031",
            "subType": 1,
            "hardwareVer": None,
            "semaphore": "12",
            "isOnline": 1,
            "startDate": "2000-06-15",
            "batteryNum": 71776813.17486387,
            "departmentId": 1382562817882931201,
            "coverType": 1,
            "status": 1,
            "pageSize": 1,
            "pageNum": 10,
            "endDate": "2021-06-10"
        }

        payload = json.dumps(payload)
        response = Test_Export.http.post(
            '/device/export', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '导出窖井列表信息失败')


if __name__ == '__main__':
    unittest.main()
