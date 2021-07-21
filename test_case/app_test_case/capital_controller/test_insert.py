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
        '''新增资产用例：/capital/insert'''
        payload = {
          "address": "南山区科技中二路2栋靠近深圳软件园2期",
          "areaId": 440305,
          "areaName": "南山区",
          "cityId": 4403,
          "cityName": "深圳市",
          "no": "869951040891735",
          "terminalNo": "869951040891735",
          "subType": 2,
          "coverType": 0,
          "spec": "1",
          "departmentId": "1413372197602385922",
          "type": 0,
          "dutyMan": "",
          "dutyManPhone": "",
          "createAt": "2021-07-20",
          "latitude": 22.54528,
          "longitude": 113.937714,
          "provinceName": "广东省",
          "provinceId": 44,
          "images1": "https://antian-iot-oss.obs.cn-south-1.myhuaweicloud.com:443/04263299e3db47f58d87df1b4e982e85.jpg",
          "images2": None,
          "images3": None,
          "images4": None,
          "id": "1416962487957372930"
        }

        # payload = {
        # 'address': "南山区科技中二路2栋靠近深圳软件园2期",
        # 'areaId': 440305,
        # 'areaName': "南山区",
        # 'cityId': 4403,
        # 'cityName': "深圳市",
        # 'coverType': 0,
        # 'createAt': "2021-07-20",
        # 'departmentId': self.mysql.department_id,
        # 'dutyMan': "",
        # 'dutyManPhone': "",
        # 'id': self.mysql.device_id,
        # 'images1': self.mysql.images_id,
        # 'images2': None,
        # 'images3': None,
        # 'images4': None,
        # 'latitude': 22.545294,
        # 'longitude': 113.937705,
        # "terminalNo": self.mysql.terminal_no,
        # 'no': self.mysql.no,
        # 'provinceId': 44,
        # 'provinceName': "广东省",
        # 'spec': "1",
        # 'subType': 2,
        # 'terminalNo': self.mysql.terminal_no,
        # 'type': 0
        # }

        headers = {'Content-Type':'application/json', 'token': get_token()}
        # payload = json.dumps(payload).encode('utf-8')
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post('/capital/insert', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '新增资产失败')


if __name__ == '__main__':
    unittest.main()
