import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests

from common.retry import Retry
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_add_task_success(self):
        '''新增或修改字典值成功用例：/dictionary/saveOrUpdate'''
        payload  = {
            "remarks": "commodo exercitation ad ullamco et",
            "typeId": 68897006,
            "showInx": 72670575,
            "id": 37768834,
            "dicValue": "Ut incididunt sed Excepteur",
            "dicCode": "46"
        }

        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post('/dictionary/saveOrUpdate',data=payload, headers=headers)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'新增或修改字典值失败')


if __name__ == '__main__':
    unittest.main()
