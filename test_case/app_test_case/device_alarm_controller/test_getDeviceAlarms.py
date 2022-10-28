import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests
from common import logging_test
from common.mysql_data import Mysql_connet
from common.retry import Retry
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')

    def test_add_task_success(self):
        '''获取设备某种报警类型下的报警信息用例：/device/getDeviceAlarms'''
        payload = {
          "alarmType": 0,
          "alarmTypes": [
            0
          ],
          "status": 0,
          "terminalNo": self.mysql.terminal_no
        }
        payload = json.dumps(payload)

        response = Test_Add_Task.http.post(
            '/device/getDeviceAlarms', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取设备某种报警类型下的报警信息失败')
        logging_test.log_test()
        logging_test.logging.info('接口返回:' + response.text)


if __name__ == '__main__':
    unittest.main()
