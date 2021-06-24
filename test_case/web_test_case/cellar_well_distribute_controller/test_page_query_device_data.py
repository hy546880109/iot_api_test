import json
import unittest
import os
import sys

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from common.http_requests import HttpRequests
from config.config_test import Conf


class Test_Device_Data(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_device_data_success(self):
        '''窖井分布-设备数据分布查询成功用例：/device/pageQueryDeviceData'''
        payload = {
            "addrid": None,
            "alarmStatus": None,
            "departmentId": None,
            "startDate": None,
            "endDate": None,
            "subType": None,
            'pageNum': 1,
            'pageSize': 10
        }
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}

        response = Test_Device_Data.http.post(
            '/device/pageQueryDeviceData', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '窖井分布-设备数据分布查询失败')


if __name__ == '__main__':
    unittest.main()
