import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)

from common.login_token import get_token
from common.mysql_data import Mysql_connet
import unittest
import json
from config.config_test import Conf
from common.http_requests import HttpRequests
# from test_case.web_test_case.cellar_well_controller.test_delete import Test_Detele_Device

class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.delete_device()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_device()
        cls.mysql.close()    

    def test_add_task_success(self):
        '''新增资产用例：/capital/insert'''
        payload = {
        'address': "南山区科技中二路2栋靠近深圳软件园2期",
        'areaId': 440305,
        'areaName': "南山区",
        'cityId': 4403,
        'cityName': "深圳市",
        'coverType': 0,
        'createAt': "2021-07-20",
        'departmentId': self.mysql.department_id,
        'dutyMan': "",
        'dutyManPhone': "",
        'id': self.mysql.capital_id,
        'images1': None,
        'images2': None,
        'images3': None,
        'images4': None,
        'latitude': 22.545294,
        'longitude': 113.937705,
        "terminalNo": self.mysql.terminal_no,
        'no': self.mysql.no,
        'provinceId': 44,
        'provinceName': "广东省",
        'spec': "1",
        'subType': 2,
        'type': 0
        }

        headers = {'Content-Type':'application/json'}
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post('/capital/insert', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '新增资产失败')


if __name__ == '__main__':
    unittest.main()
