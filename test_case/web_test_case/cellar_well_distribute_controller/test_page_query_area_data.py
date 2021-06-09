import json
import unittest
import os
import sys

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from common.http_requests import HttpRequests
from config.config_test import Conf


class Test_Page_Query_Area(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_page_query_area_success(self):
        '''区域数据分布查询成功用例：/device/pageQueryAreaData'''
        payload = {
            "addrid": 44,
            "alarmStatus": None,
            "departmentId": None,
            "startDate": None,
            "endDate": None,
            "subType": None,
            'pageNum': 1,
            'pageSize': 10
        }
        payload = json.dumps(payload)
        response = Test_Page_Query_Area.http.post(
            '/device/pageQueryAreaData', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '区域数据分布查询失败')


if __name__ == '__main__':
    unittest.main()
