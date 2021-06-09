import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_add_task_success(self):
        '''设备上报日志列表成功用例：/up/log/pageQuery'''
        payload = {
            "pageNum": 10,
            "pageSize": 10,
            "terminalNo": "veniam laboris sint",
            "startDate": "1948-03-19T20:01:24.496Z",
            "ins": "esse",
            "endDate": "2007-07-09T21:28:33.001Z"
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post('/up/log/pageQuery',data=payload)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'设备上报日志列表失败')


if __name__ == '__main__':
    unittest.main()
