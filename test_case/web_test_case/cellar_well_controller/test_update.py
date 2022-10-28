import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
from common.http_requests import HttpRequests
from config.config_test import Conf
from common.retry import Retry
from common.logging_test import log_test
import logging
@Retry
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
        '''更新资产成功用例：/device/update'''
        payload = {
          "address": "南山区科技中二路29号靠近深圳软件园2期",
          "areaId": 440305,
          "areaName": "南山区",
          "cityId": 4403,
          "cityName": "深圳市",
          "coverType": 0,
          "createAt": "2022-04-13",
          "departmentId": "234567891",
          "dutyMan": "",
          "dutyManPhone": "",
          "hardwareVer": "IGW-NB-K-BX-V1.0",
          "iccid": "89861119212002368684",
          "id": self.mysql.device_id,
          "images1": "https://antian-iot-oss.obs.cn-south-1.myhuaweicloud.com:443/962d361a1b3742c8bd295ad8748e4aa2.jpg",
          "images2": "NULL",
          "images3": "NULL",
          "images4": "NULL",
          "imsi": "460113036642806",
          "latitude": 22.545289,
          "longitude": 113.937628,
          "mac": "C3:B2:5D:7E:AE:7B",
          "name": "hh",
          "no": self.mysql.no,
          "provinceId": 44,
          "provinceName": "广东省",
          "remark": "",
          "softwareVer": "ZL-V1.0.5-220411",
          "spec": "1",
          "subType": 2,
          "terminalNo": 678912345,
          "type": 2,
          "unitId": "1"
        }

        payload = json.dumps(payload)
        response = Test_Device_List.http.post('/device/update', data=payload)
        log_test()
        logging.info('接口返回:' + response.text)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '更新资产失败')


if __name__ == '__main__':
    unittest.main()
