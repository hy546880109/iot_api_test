import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common import logging_test
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.mysql_data import Mysql_connet
from common.retry import Retry
@Retry
class Test_Get_Index(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('user')

    def test_get_index_success(self):
        """获取版本号成功用例: /ver/getUpgradePackage"""
        data = {
          "departmentId": None,
          "type": 4,
          "ver": None
        }
        data = json.dumps(data)
        response = Test_Get_Index.http.post('/ver/getUpgradePackage', data=data)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(
            response.json()['code']), '获取版本号用例失败')
        logging_test.log_test()
        logging_test.logging.info('接口返回:' + response.text)

if __name__ == '__main__':
    unittest.main()
