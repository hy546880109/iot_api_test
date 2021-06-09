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
        '''增加用户角色成功用例：/userRole/insert'''
        payload = [
    {
        "userId": 31246378,
        "roleId": 20846500
    },
    {
        "roleId": 44292708,
        "userId": 7221499
    }
    ]
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post('/userRole/insert',data=payload)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'增加用户角色失败')


if __name__ == '__main__':
    unittest.main()
