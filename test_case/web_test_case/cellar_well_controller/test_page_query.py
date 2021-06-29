from common.mysql_data import Mysql_connet
from common.login_token import get_token
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
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_device()
        cls.mysql.insert_user()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_device()
        cls.mysql.delete_user()
        cls.mysql.close()        


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
        headers = {'Content-Type': 'application/json', 'token': get_token()}
        response = Test_Device_List.http.post('/device/pageQuery', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取窖井列表信息失败')


if __name__ == '__main__':
    unittest.main()
