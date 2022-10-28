import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)

from common.mysql_data import Mysql_connet
from config.config_test import Conf
from common.http_requests import HttpRequests
from common import logging_test
from common.retry import Retry
@Retry
class Test_Get_Index(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('user')
        # cls.mysql.insert_user()

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
        # headers = {'Content-Type': 'application/json', 'token': get_token()}
        response = Test_Get_Index.http.post('/user/doBase64', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '上传头像失败')
        logging_test.log_test()
        logging_test.logging.info('接口返回:' + response.text)

if __name__ == '__main__':
    unittest.main()
