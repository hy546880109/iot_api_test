import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.mysql_data import Mysql_connet
from common.retry import Retry
from common import logging_test
from common.doc_value import doc_parameter
uri = '/user/updatePassword'
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
    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_get_index_success(self):
        """修改密码成功用例: {}{}"""
        data = {
              "oldPassword": "e10adc3949ba59abbe56e057f20f883e",
              "password": "e10adc3949ba59abbe56e057f20f883e"
            }
        data = json.dumps(data)
        response = Test_Get_Index.http.post(uri, data=data)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(
            response.json()['code']), '修改密码成功用例失败')
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '-接口返回:' + response.text)

if __name__ == '__main__':
    unittest.main()
