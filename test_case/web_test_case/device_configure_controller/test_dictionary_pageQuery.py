import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests
from common import logging_test
from common.retry import Retry
from common.doc_value import doc_parameter
uri = '/device/config/pageQuery'
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_add_task_success(self):
        '''获取设备配置列表成功用例：{}{}'''
        payload = {
            "endDate": None,
            "departmentId": None,
            "pageNum": 1,
            "startDate": None,
            "addrId": "44",
            "terminalNo": None,
            "pageSize": 10,
            "configStatus": None
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(uri,data=payload)
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '-接口返回:' + response.text)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'获取设备配置列表失败')


if __name__ == '__main__':
    unittest.main()
