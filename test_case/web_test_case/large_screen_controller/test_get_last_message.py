import unittest
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_add_task_success(self):
        '''最新消息成功用例：/large/screen/getLastMessage'''
        response = Test_Add_Task.http.get('/large/screen/getLastMessage')
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'最新消息失败')


if __name__ == '__main__':
    unittest.main()
