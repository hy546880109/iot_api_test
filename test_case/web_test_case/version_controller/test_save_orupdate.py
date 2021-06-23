import unittest,json
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_add_task_success(self):
        '''新增或修版本说明成功用例：/ver/saveOrUpdate'''
        payload =  {
            "remark": "veniam",
            "id": None,
            "ver": "1.0"
        }
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post('/ver/saveOrUpdate',data=payload, headers=headers)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'新增或修版本说明失败')


if __name__ == '__main__':
    unittest.main()
