import unittest,os,sys
import json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Delete_Batch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_delete_batch_success(self):
        '''批量删除工单成功用例：/device/deleteBatchIds'''
        payload  =  [10, 20]
        payload = json.dumps(payload)
        response = Test_Delete_Batch.http.post('/device/deleteBatchIds',data=payload)
        print('payload:',payload)
        print(response.text)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'批量删除工单失败')


if __name__ == '__main__':
    unittest.main()
