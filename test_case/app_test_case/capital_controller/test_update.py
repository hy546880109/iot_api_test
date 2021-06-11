import unittest
import json
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)

    def test_add_task_success(self):
        '''更新资产用例：/capital/update'''
        payload = {
            "no": "888888831",
            "departmentId": "1382562817882931201",
            "latitude": "22.54911",
            "images4": "../../assets/imgs/cover03.jpg",
            "remark": "",
            "cityId": 4403,
            "images1": "../../assets/imgs/cover00.jpg",
            "spec": "1",
            "createAt": "Tue May 18 10:39:25 CST 2021",
            "images3": "../../assets/imgs/cover02.jpg",
            "images2": "../../assets/imgs/cover01.jpg",
            "coverType": 0,
            "dutyMan": "张三",
            "cityName": "深圳市",
            "areaName": "南山区",
            "id": "13919460123446761",
            "safeManPhone": "",
            "longitude": "113.93109",
            "terminalNo": "8888888031",
            "address": "大新路南头街道88-36号",
            "dutyManPhone": "12345678901",
            "provinceId": 44,
            "safeMan": "",
            "areaId": 440305,
            "subType": 1,
            "provinceName": "广东省"
        }
        headers = {'Content-Type': 'application/json'}
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(
            '/capital/update', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '更新资产失败')


if __name__ == '__main__':
    unittest.main()
