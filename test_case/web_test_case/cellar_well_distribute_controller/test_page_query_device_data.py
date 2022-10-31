import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
from common.http_requests import HttpRequests
from config.config_test import Conf
from common import logging_test
from common.retry import Retry
from common.doc_value import doc_parameter
uri = '/device/pageQueryDeviceData'
@Retry
class Test_Device_Data(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_user()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_user()
        cls.mysql.close()   
    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_device_data_success(self):
        '''窖井分布-设备数据分布查询成功用例：/device/pageQueryDeviceData'''
        payload = {
            "addrid": None,
            "alarmStatus": None,
            "departmentId": self.mysql.department_id,
            "startDate": None,
            "endDate": None,
            "subType": None,
            'pageNum': 1,
            'pageSize': 10
        }
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}

        response = Test_Device_Data.http.post(
            uri, data=payload, headers=headers)
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '-接口返回:' + response.text)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '窖井分布-设备数据分布查询失败')


if __name__ == '__main__':
    unittest.main()
