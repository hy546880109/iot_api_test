import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
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
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_device()

    @classmethod
    def tearDown(cls) -> None:
        cls.mysql.delete_device()
        cls.mysql.close()

    def test_get_index_success(self):
        """通过子设备的设备ID获取Lora网关详情成功用例: /lora/getLoraGatewayDetailInfoById"""
        payload = {
          "id": self.mysql.cellar_well_terminal_id
        }

        response = Test_Get_Index.http.get('/lora/getLoraGatewayDetailInfoById', params=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '通过子设备的设备ID获取Lora网关详情失败')
        logging_test.log_test()
        logging_test.logging.info('接口返回:' + response.text)

if __name__ == '__main__':
    unittest.main()
