import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests

from common.retry import Retry
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_add_task_success(self):
        '''通过名称获取上一级地址成功用例：/address/getProvinceCityDistrictByName'''
        payload = {
            "name": '湖南'
            }
        response = Test_Add_Task.http.get('/address/getProvinceCityDistrictByName',params=payload)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'通过名称获取上一级地址失败')


if __name__ == '__main__':
    unittest.main()
