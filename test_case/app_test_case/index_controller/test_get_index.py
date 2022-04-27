import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from common.login_token import get_token
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Get_Index(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)

    def test_get_index_success(self):
        """APP首页报警、工单未读数据成功用例: /getNoRead"""
        
        response = Test_Get_Index.http.get('/getNoRead')
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(
            response.json()['code']), 'APP首页报警、工单未读数据成功用例失败')


if __name__ == '__main__':
    unittest.main()
