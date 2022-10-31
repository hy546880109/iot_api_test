import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.retry import Retry
from common import logging_test
from common.doc_value import doc_parameter
uri = '/device/pageQueryAreaData'
@Retry
class Test_Page_Query_Area(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_user()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_user()
        cls.mysql.close()
    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_page_query_area_success(self):
        '''窖井分布-区域数据分布查询成功用例：{}{}'''
        payload = {
            'addrId': None,
            'coverType': "",
            'departmentId': self.mysql.department_id,
            'pageNum': 1,
            'pageSize': 10,
            'spec': "",
            'subType': ""
        }
        # headers = {'token' : get_token(),'Content-Type': 'application/json'}
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = Test_Page_Query_Area.http.post(
            uri, data=payload)
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '-接口返回:' + response.text)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(
            response.json()['code']), '窖井分布-区域数据分布查询失败')


if __name__ == '__main__':
    unittest.main()
