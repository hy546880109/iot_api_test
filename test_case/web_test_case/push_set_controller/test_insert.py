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
        '''创建任务成功用例：/push/set/insert'''
        payload = {
        "departmentId":1382562817882931201,
        "messageType":"1",
        "pushType":"0,0,1",
        "userId":1377074593995628546
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post('/push/set/insert',data=payload)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'创建任务失败')


if __name__ == '__main__':
    unittest.main()
