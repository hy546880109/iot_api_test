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
        cls.mysql = Mysql_connet('user')
        cls.mysql.insert_sql('user')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_user()
        cls.mysql.close()

    def test_get_index_success(self):
        """重置密码成功用例: /user/resetPwd"""
        data = {
          "userId": self.mysql.user_id

        }

        response = Test_Get_Index.http.get('/user/resetPwd', params=data)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(
            response.json()['code']), '重置密码成功用例失败')


if __name__ == '__main__':
    unittest.main()
