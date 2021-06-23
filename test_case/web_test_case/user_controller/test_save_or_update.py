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
        '''新增或修改用户信息成功用例：/user/saveOrUpdate'''
        payload = {
            "code": "46",
            "departmentId": 55754820,
            "level": 91141095,
            "password": "in labore occaecat",
            "email": "r.hnusukn@qq.com",
            "phone": "13373524457",
            "name": "每价是数放导",
            "id": 68289069,
            "remark": "laboris aliqua magna"
        }
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post('/user/saveOrUpdate',data=payload, headers=headers)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'新增或修改用户信息失败')


if __name__ == '__main__':
    unittest.main()
