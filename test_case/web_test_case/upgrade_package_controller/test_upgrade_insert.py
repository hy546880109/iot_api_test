import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)

from common.http_requests import HttpRequests
from config.config_test import Conf
from common.retry import Retry
from common import logging_test
@Retry
class Test_Add_Upgrade(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    @classmethod
    def tearDown(cls) -> None:
        pass

    def test_add_upgrade_success(self):
        '''上传升级包成功用例：/upgrade/package/insert'''
        payload = {
          "id": "",
          "name": "iWellGatewayV1.0.0.bin",
          "remark": "iWellGatewayV1.0.0",
          "size": 76696,
          "type": "0",
          "url": "https://antian-iot-oss.obs.cn-south-1.myhuaweicloud.com:443/5a5cf672bb4540c1b7bcc362493877e6.bin",
          "ver": "iWellGatewayV1.0.0"
        }
        payload = json.dumps(payload)
        response = Test_Add_Upgrade.http.post(
            '/upgrade/package/insert', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '上传升级包失败')
        logging_test.log_test()
        logging_test.logging.info('接口返回:' + response.text)


if __name__ == '__main__':
    unittest.main()
