import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from common.login_token import get_token
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_add_task_success(self):
        '''查询部门下所有的子部门成功用例：/department/pageQuery'''
        payload  = {
            "name": "a",
            "pageNum": 1,
            "pageSize": 10,
            "addrId": 1,
            "pid": 1
        }
        payload = json.dumps(payload)
        print('data:',payload)
        headers = {'Content-Type': 'application/json', 'token': get_token()}
        response = Test_Add_Task.http.post('/department/pageQuery',data=payload, headers=headers)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'查询部门下所有的子部门失败')


if __name__ == '__main__':
    unittest.main()
