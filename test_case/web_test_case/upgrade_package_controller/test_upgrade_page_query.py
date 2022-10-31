import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

from common.http_requests import HttpRequests
from config.config_test import Conf
from common import logging_test
from common.doc_value import doc_parameter
from common.retry import Retry
uri = '/upgrade/package/pageQuery'
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_add_task_success(self):
        """获取升级包列表用例：{}{}"""
        payload = {
            "createBy": None,
            "name": None,
            "type": None,
            "ver": None,
            "startDate": None,
            "endDate": None,
            "pageNum": 1,
            "pageSize": 100000000
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(
            uri, data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取升级包列表失败')
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '-接口返回:' + response.text)

if __name__ == '__main__':
    unittest.main()
