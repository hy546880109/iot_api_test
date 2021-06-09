import unittest,os,sys

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests


payload  = {"id":13}

# payload = json.dumps(payload)
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_add_task_success(self):
        '''删除部门成功用例：/department/delete'''
        response = Test_Add_Task.http.get('/department/delete',params=payload)
        # response = Test_Add_Task.http.get('/department/delete?id=13',params=payload)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'删除部门失败')


if __name__ == '__main__':
    unittest.main()
