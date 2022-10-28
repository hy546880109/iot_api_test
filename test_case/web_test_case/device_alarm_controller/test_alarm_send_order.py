import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
from config.config_test import Conf
from common.http_requests import HttpRequests
from common import logging_test
from common.retry import Retry
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_device()
        cls.mysql.insert_user()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_device()
        cls.mysql.delete_user()
        cls.mysql.close()
        
    def test_add_task_success(self):
        '''手动派单成功用例：/history/alarm/manualDistributeTask'''
        payload = {
            "alarmId": self.mysql.alarm_id,
            "departmentId": self.mysql.department_id,
            "level": 0,
            "prvFinishTime": "2021-05-21 12:25:56",
            "taskReceive": 1377074593995628546,
            "workSrc": 0,
            "workType": 0
        }
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post(
            '/history/alarm/manualDistributeTask', data=payload, headers=headers)
        logging_test.log_test()
        logging_test.logging.info('接口返回:' + response.text)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '手动派单失败')


if __name__ == '__main__':
    unittest.main()
