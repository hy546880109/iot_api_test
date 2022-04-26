from cgi import parse_multipart
import unittest,os,sys,json

from pymysql import paramstyle

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_add_task_success(self):
        '''窖井资产管理成功用例：/large/screen/captionManager'''
        params = {'type':1}
        response = Test_Add_Task.http.get('/large/screen/captionManager', params=params)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'窖井资产管理失败')


if __name__ == '__main__':
    unittest.main()