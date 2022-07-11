import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)

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
        cls.mysql = Mysql_connet('device')


    def test_get_index_success(self):
        """测试删除电信平台数据成功用例: /iot/platform/deleteByDeviceId"""
        params = {'terminalNo':self.mysql.terminal_no}
        response = Test_Get_Index.http.get('/iot/platform/deleteByDeviceId', params=params)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(
            response.json()['code']), '测试删除电信平台数据成功用例失败')


if __name__ == '__main__':
    unittest.main()
