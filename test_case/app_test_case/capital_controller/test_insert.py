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
        '''新增资产用例：/capital/insert'''
        payload = {
            "address": "大新路南头街道88-36号",
            "areaId": 440303,
            "areaName": "南山区",
            "cityId": 4403,
            "cityName": "深圳市",
            "coverType": 71,
            "createAt": "1977-02-03 14:57:32",
            "departmentId": 1382562817882931201,
            "dutyMan": "est proident tempor",
            "dutyManPhone": "18142359380",
            "id": 13919460123446761,
            "images1": "http://dummyimage.com/400x400",
            "images2": "http://dummyimage.com/400x400",
            "images3": "http://dummyimage.com/400x400",
            "images4": "http://dummyimage.com/400x400",
            "latitude": "22.54901",
            "longitude": "113.93109",
            "no": "888888801",
            "provinceId": 44,
            "provinceName": "广东省",
            "remark": "qui voluptate",
            "safeMan": "aliquip",
            "safeManPhone": "18174576460",
            "spec": "1",
            "subType": 0,
            "terminalNo": "88888881011",
            "type": 8,
            "userId": 1377074593995628546
        }
        headers = {'Content-Type':'application/json', 'Accept-Encoding': 'gzip, deflate, br', 'Cache-Control': 'no-cache', 'User-Agent': 'apifox/1.0.0 (https://www.apifox.cn)'}
        payload = json.dumps(payload).encode('utf-8')
        response = Test_Add_Task.http.post('/capital/insert', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '新增资产失败')


if __name__ == '__main__':
    unittest.main()
