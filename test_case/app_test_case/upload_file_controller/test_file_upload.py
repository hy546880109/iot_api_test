from common.login_token import get_token
from sys import int_info
from common.mysql_data import Mysql_connet
import unittest
import json
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Get_Index(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_user()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_user()
        cls.mysql.close()
        

    def test_get_index_success(self):
        """上次头像成功用例: /user/doBase64"""
        payload = {
            "base64Str": 'https://antian-iot-oss.obs.cn-south-1.myhuaweicloud.com:443/bf75aa98846240248412a9c8433aed6b.jpg'
        }
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json', 'token': get_token()}
        response = Test_Get_Index.http.post('/user/doBase64', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '上传头像失败')


if __name__ == '__main__':
    unittest.main()
