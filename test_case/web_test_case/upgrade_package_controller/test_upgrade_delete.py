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
uri = '/upgrade/package/deleteBatchIds'
@Retry
class Test_Delete_Upgrade(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('base')

    @classmethod
    def tearDown(cls) -> None:
        cls.mysql.close()
    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_delete_upgrade_success(self):
        """批量删除升级包成功用例：{}{}"""
        up_id = self.mysql.select_sql("SELECT id from t_upgrade_package where `name` ='iWellGatewayV1.0.0.bin' and is_delete = 0 LIMIT 1")
        payload = [up_id]
        payload = json.dumps(payload)
        response = Test_Delete_Upgrade.http.post(uri, data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '批量删除升级包失败')
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '-接口返回:' + response.text)

if __name__ == '__main__':
    unittest.main()
