import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.mysql_data import Mysql_connet
from common.retry import Retry
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_device()
        
    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_device()
        cls.mysql.close()
    
    def test_add_task_success(self):
        """获Lora网关列表信息成功用例：/lora/pageQuery"""
        ids = {
          "addrId": 0,
          "address": "string",
          "batteryNum": 0,
          "departmentId": self.mysql.department_id,
          "endDate": "2022-4-1 12:00:00",
          "installStatus": 0,
          "isOnline": 0,
          "name": "string",
          "pageNum": 1,
          "pageSize": 1,
          "semaphore": "12",
          "startDate": "2022-4-1 12:00:00",
          "startNun": 1,
          "terminalNo": self.mysql.terminal_no,
          "total": 1,
          "unitId": 1
        }
        ids = json.dumps(ids)
        response = Test_Add_Task.http.post('/lora/pageQuery', data=ids)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'获Lora网关列表信息失败')


if __name__ == '__main__':
    unittest.main()
