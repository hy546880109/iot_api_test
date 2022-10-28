import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from common.http_requests import HttpRequests
from config.config_test import Conf
from common import logging_test
from common.retry import Retry
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_add_task_success(self):
        '''获取历史工单列表成功用例：/work/order/pageQuery'''
        payload = {
            "finishEndDate": "1994-04-02",
            "addrId": -65544111,
            "departmentId": 14734859,
            "workSrc": 99715239,
            "workOrderEndDate": "1985-11-29",
            "alarmType": -225822,
            "workOrderStartDate": "2005-05-19",
            "pageSize": 36070881,
            "status": 44537036,
            "finishStartDate": "1970-04-02",
            "overtimeStatus": -52032459,
            "pageNum": -53841090
        }
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post(
            '/work/order/pageQuery', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取历史工单列表失败')
        logging_test.log_test()
        logging_test.logging.info('接口返回:' + response.text)

if __name__ == '__main__':
    unittest.main()
