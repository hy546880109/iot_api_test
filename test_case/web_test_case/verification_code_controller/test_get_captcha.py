import requests
import json
import os,sys
import unittest
path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests


payload  = {

}

from common.retry import Retry
@Retry
class Test_Get_Code(unittest.TestCase):

    @classmethod 
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_get_captcha_success(self):
        '''获取验证码用例：/captcha'''
        response = Test_Get_Code.http.get('/captcha',data=payload)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'获取验证码失败')


if __name__ == '__main__':
    unittest.main()
