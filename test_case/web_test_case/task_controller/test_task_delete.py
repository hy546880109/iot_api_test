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
from common import logging_test
from common.retry import Retry
@Retry
class Test_Delete_Task(unittest.TestCase):

    @classmethod 
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_delete_task_success(self):
        '''删除任务成功用例：/task/deleteBatchIds'''
        payload = [57292403983134, 83390078552882]
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = Test_Delete_Task.http.post('/task/deleteBatchIds',data=payload, headers=headers)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'删除任务失败')
        logging_test.log_test()
        logging_test.logging.info('接口返回:' + response.text)
if __name__ == '__main__':
    unittest.main()