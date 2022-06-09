import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)

from config.config_test import Conf
from common.http_requests import HttpRequests
from common.mysql_data import Mysql_connet

class Test_Get_Index(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_sql('device')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_device()
        cls.mysql.close()

    def test_get_index_success(self):
        """注册电信平台成功用例: /iot/platform/registerIotPlatform"""
        data = {
          "imsi": "460113036642221",
          "terminalNo": self.mysql.terminal_no
        }
        data = json.dumps(data)
        response = Test_Get_Index.http.post('/iot/platform/registerIotPlatform', data=data)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(
            response.json()['code']), '注册电信平台成功用例失败')


if __name__ == '__main__':
    unittest.main()
