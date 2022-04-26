import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_add_task_success(self):
        '''导出设备上报指令日志成功用例：/ins/log/export'''
        payload = {
          "departmentId": 0,
          "endDate": "string",
          "ins": "string",
          "installEndDate": "string",
          "installStartDate": "string",
          "name": "string",
          "pageNum": 0,
          "pageSize": 0,
          "startDate": "string",
          "startNun": 0,
          "terminalNo": "string",
          "total": 0
        }
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post('/ins/log/export',data=payload, headers=headers)
        self.assertEqual(200,response.status_code,'返回非200')
        # self.assertEqual(str(0), str(response.json()['code']),'导出设备上报指令日志失败')


if __name__ == '__main__':
    unittest.main()
