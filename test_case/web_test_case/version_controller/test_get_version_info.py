import unittest,json
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_add_task_success(self):
        '''获取版本号成功用例：/ver/getVersionInfo'''
        response = Test_Add_Task.http.post('/ver/getVersionInfo')
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'获取版本号失败')


if __name__ == '__main__':
    unittest.main()
