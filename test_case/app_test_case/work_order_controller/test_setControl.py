import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
from config.config_test import Conf
from common.http_requests import HttpRequests


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
        """布/撤控成功用例: /work/order/setControl"""
        payload = {
            "controlStatus": 0,
            "duration": 3,
            "terminalNo": self.mysql.terminal_no
        }
        payload = json.dumps(payload)
        # headers = {'Content-Type': 'application/json','token': get_token()}
        response = Test_Get_Index.http.post(
            '/work/order/setControl', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '布/撤控失败')


if __name__ == '__main__':
    unittest.main()
