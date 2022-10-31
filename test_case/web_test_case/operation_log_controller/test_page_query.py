import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests
from common import logging_test
from common.retry import Retry
from common.doc_value import doc_parameter
uri = '/operate/log/pageQuery'

@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_add_task_success(self):
        '''页面查询成功用例： {}{}'''
        # Test_Add_Task.__doc__ = '''页面查询成功用例： {}/operate/log/pageQuery'''.format(Test_Add_Task.url)
        payload = {
            "createName": "斯元话定经书低",
            "logType": 93686580,
            "endDate": "2007-01-03",
            "pageSize": 2434082,
            "logFrom": 45580018,
            "operateType": "est reprehenderit ipsum eiusmod nisi",
            "departmentId": 82619406,
            "pageNum": 97211303,
            "addrId": 98456171,
            "startDate": "1992-12-19"
            }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(uri,data=payload)
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '>>>' +'接口返回:' + response.text)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'页面查询失败')


if __name__ == '__main__':
    unittest.main()
