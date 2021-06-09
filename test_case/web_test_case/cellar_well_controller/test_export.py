import json
import unittest
import os
import sys

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from common.http_requests import HttpRequests
from config.config_test import Conf

class Test_Export(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_export_success(self):
        '''导出窖井列表信息成功用例：/device/export'''
        payload = {
            "controlStatus": -58928019,
            "no": "eu",
            "addrId": 39160561,
            "bluetoothStatus": "veniam et mollit",
            "terminalNo": "dolor",
            "subType": -74293568,
            "hardwareVer": "culpa fugiat sint aute adipisicing",
            "semaphore": "sunt anim veniam culpa occaecat",
            "isOnline": 89805775,
            "startDate": "2000-06-15",
            "batteryNum": 71776813.17486387,
            "departmentId": -77315371,
            "coverType": -90503126,
            "status": -79172324,
            "pageSize": -46458547,
            "pageNum": -43404172,
            "endDate": "1990-05-24"
        }

        payload = json.dumps(payload)
        response = Test_Export.http.post(
            '/device/export', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '导出窖井列表信息失败')


if __name__ == '__main__':
    unittest.main()
