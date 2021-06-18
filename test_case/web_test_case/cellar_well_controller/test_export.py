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
            "controlStatus": None,
            "no": None,
            "addrId": None,
            "bluetoothStatus": None,
            "terminalNo": None,
            "subType": None,
            "hardwareVer": None,
            "semaphore": None,
            "isOnline": None,
            "startDate": None,
            "batteryNum": None,
            "departmentId": None,
            "coverType": None,
            "status": None,
            "pageSize": 1,
            "pageNum": 1,
            "endDate": None
        }
        headers = {'Content-Type':'application/vnd.ms-excel;charset=UTF-8'}
        payload = json.dumps(payload)
        response = Test_Export.http.post(
            '/device/export', data=payload,headers=headers)
        print(response.content)
        # print(response.text.encode('raw_unicode_escape'))
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(None, str(response.json()['code']), '导出窖井列表信息失败')


if __name__ == '__main__':
    unittest.main()
