import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common.login_token import get_token
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.mysql_data import Mysql_connet


class Test_Get_Index(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_device()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_device()
        cls.mysql.close()

    def test_get_index_success(self):
        """根据工单ID获取窖井信息成功用例: /work/order/getCellarWellDetail"""
        payload = {
            "id": self.mysql.work_order_id
            # "id": 1422033768985702401
        }
        # headers = {'Content-Type': 'application/json','token': get_token()}
        response = Test_Get_Index.http.get('/work/order/getCellarWellDetail', params=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '根据工单ID获取窖井信息失败')


if __name__ == '__main__':
    unittest.main()
