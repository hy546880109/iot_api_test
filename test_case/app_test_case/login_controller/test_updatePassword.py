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
        cls.mysql = Mysql_connet('user')
        cls.mysql.insert_sql('user')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_user()
        cls.mysql.close()

    def test_get_index_success(self):
        """修改密码成功用例: /user/updatePassword"""
        data = {
              "oldPassword": "e10adc3949ba59abbe56e057f20f883e",
              "password": "e10adc3949ba59abbe56e057f20f883e"
            }
        data = json.dumps(data)
        response = Test_Get_Index.http.post('/user/updatePassword', data=data)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(
            response.json()['code']), '修改密码成功用例失败')


if __name__ == '__main__':
    unittest.main()
