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
        '''获取设备配置列表成功用例：/device/config/pageQuery'''
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
        response = Test_Add_Task.http.post('/device/config/pageQuery',data=payload)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'获取设备配置列表失败')


if __name__ == '__main__':
    unittest.main()
