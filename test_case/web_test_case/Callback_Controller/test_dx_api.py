#!/usr/bin/python
# _*_ codeing: utf-8 _*_
import unittest,os,sys,json,logging

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.mysql_data import Mysql_connet
from common.logging_test import log_test
from common.retry import Retry
@Retry
class Test_Detele_Device(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_device()
        cls.device_id = cls.mysql.select_sql(
            'select id from t_cellar_well where id={}'.format(cls.mysql.device_id))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_device()
        cls.mysql.close()

    def test_delete_device_success(self):
        """电信回调数据/cwting/callback"""
        payload = {"upPacketSN":-1,"upDataSN":-1,"topic":"v1/up/ad","timestamp":1650554828842,"tenantId":"2000033629","serviceId":"","protocol":"lwm2m","productId":"15114816","payload":{"APPdata":"AQFWMS4wAAAAACMAAAAH/wAlODYyNTkyMDUxNjUxNDcyAAEAMjUAODAAAAAAAAABAQAAAAEAAASD"},"messageType":"dataReport","deviceType":"","deviceId":"40edca19b0124480864366de4621de99","assocAssetId":"","IMSI":"undefined","IMEI":"862592051651472"}
        payload = json.dumps(payload)
        response = Test_Detele_Device.http.post(
            '/cwting/callback', data=payload)
        log_test()
        logging.info('接口返回:' + response.text)
        self.assertEqual(200, response.status_code, '返回非200')
        # self.assertEqual(str(0), str(response.json()['code']), '电信回调数据失败')



if __name__ == '__main__':
    unittest.main()
