import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests
from common import  logging_test
from common.retry import Retry
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_add_task_success(self):
        '''基础数据成功用例：/large/screen/getBasicData'''
        response = Test_Add_Task.http.get('/large/screen/getBasicData')
        logging_test.log_test()
        logging_test.logging.info('接口返回:' + response.text)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'基础数据失败')


if __name__ == '__main__':
    unittest.main()
