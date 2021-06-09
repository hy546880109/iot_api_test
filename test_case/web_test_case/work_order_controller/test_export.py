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
        '''导出工单成功用例：/work/order/export'''
        payload = {
            "addrId": 16554203,
            "pageSize": 1,
            "alarmType": 5608527,
            "finishEndDate": "1974-07-06",
            "overtimeStatus": 80903637,
            "status": -27805559,
            "pageNum": 1,
            "departmentId": 24091246,
            "workOrderEndDate": "1997-11-12",
            "workOrderStartDate": "1975-01-12",
            "workSrc": 13833952,
            "finishStartDate": "2011-07-23"
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post('/work/order/export',data=payload)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'导出工单失败')


if __name__ == '__main__':
    unittest.main()
