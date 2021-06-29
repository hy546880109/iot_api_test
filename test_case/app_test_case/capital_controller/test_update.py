from common.login_token import get_token
from common.mysql_data import Mysql_connet
import unittest
import json
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_device()
        cls.mysql.insert_user()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_device()
        cls.mysql.delete_user()
        cls.mysql.close()    

    def test_add_task_success(self):
        '''更新资产用例：/capital/update'''
        payload = {
            'address': "朗山路西丽街道149号",
            'areaId': 440305,
            'areaName': "南山区",
            'cityId': 4403,
            'cityName': "深圳市",
            'coverType': 0,
            'createAt': "2021-06-12",
            'departmentId': self.mysql.department_id,
            'dutyMan': "",
            'dutyManPhone': "",
            'id': self.mysql.capital_id,
            'images1': "https://antian-iot-oss.obs.cn-south-1.myhuaweicloud.com:443/0cec685333534204a3a499ebdd76ebe3.jpg",
            'images2': None,
            'images3': None,
            'images4': None,
            'latitude': 22.545266,
            'longitude': 113.937628,
            'no': self.mysql.no,
            'provinceId': 44,
            'provinceName': "广东省",
            'spec': "1",
            'subType': 1,
            'terminalNo': self.mysql.terminal_no,
            'type': 0
        }
        headers = {'Content-Type': 'application/json','token': get_token()}
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(
            '/capital/update', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '更新资产失败')


if __name__ == '__main__':
    unittest.main()
