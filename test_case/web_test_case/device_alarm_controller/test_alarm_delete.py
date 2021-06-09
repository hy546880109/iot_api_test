import requests
import demjson
import json
import os,sys
import unittest
path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests


payload  = [
    11641045,
    75501558]
payload = json.dumps(payload)

class Test_Add_Task(unittest.TestCase):

    @classmethod 
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_add_task_success(self):
        '''批量删除报警成功用例：/history/alarm/deleteBatchIds'''
        response = Test_Add_Task.http.post('/history/alarm/deleteBatchIds',data=payload)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'批量删除报警失败')
    

if __name__ == '__main__':
    unittest.main()
