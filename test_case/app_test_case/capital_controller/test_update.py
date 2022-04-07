import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common.login_token import get_token
from common.mysql_data import Mysql_connet
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
        'address': "南山区科技中二路2栋靠近深圳软件园2期",
        'areaId': 440305,
        'areaName': "南山区",
        'cityId': 4403,
        'cityName': "深圳市",
        'coverType': 0,
        'createAt': "2021-07-30",
        'departmentId': "1420253676542480386",
        'dutyMan': "hh",
        'dutyManPhone': "13246988667",
        "hardwareVer": "string",
        'id': "1420635818199941122",
        'images1': "https://antian-iot-oss.obs.cn-south-1.myhuaweicloud.com:443/94fc06af67a44905982c9e9b2acc881a.jpg",
        'images2': "https://antian-iot-oss.obs.cn-south-1.myhuaweicloud.com:443/1d9dfa552a1e4f3481d4504ddf2f7d52.jpg",
        'images3': "https://antian-iot-oss.obs.cn-south-1.myhuaweicloud.com:443/c90355d70cc84648a0d6af8f033a6390.jpg",
        'images4': "https://antian-iot-oss.obs.cn-south-1.myhuaweicloud.com:443/5910b93f881746868d3378e31411ad75.jpg",
        'latitude': 22.545395,
        'longitude': 113.937587,
        "mac": "string",
        "name": "string",
        "remark": "string",
        'no': "869951044459604",
        'provinceId': 44,
        'provinceName': "广东省",
        'spec': "2",
        "safeMan": "string",
        "safeManPhone": "string",
        "softwareVer": "string",
        'subType': 5,
        'terminalNo': "869951044459604",
        'type': 0,
        "userId": 0
        }

        headers = {'Content-Type': 'application/json','token': get_token(),'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7','Accept-Encoding': 'gzip, deflate','X-Requested-With': 'com.antancorp.iot.device.service.impl','Accept': 'application/json'}
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(
            '/capital/update', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '更新资产失败')


if __name__ == '__main__':
    unittest.main()
