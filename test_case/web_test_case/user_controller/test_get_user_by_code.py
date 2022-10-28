import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests
from common import logging_test
from common.retry import Retry
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_add_task_success(self):
        '''通过用户账号获取用户信息成功用例：/user/getUserByCode'''
        payload = {"code":2}
        response = Test_Add_Task.http.get('/user/getUserByCode',params=payload)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'通过用户账号获取用户信息失败')
        logging_test.log_test()
        logging_test.logging.info('接口返回:' + response.text)

if __name__ == '__main__':
    unittest.main()
