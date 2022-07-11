import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests

from common.retry import Retry
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)

    def test_add_task_success(self):
        '''获取我的报警用例：/work/order/getMyAlarms'''
        payload = {
            "alarmTypes": [
                1,
                2
            ],
            "pageSize": 1,
            "alarmInterval": 1,
            "pageNum": 10
        }

        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(
            '/work/order/getMyAlarms', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取我的报警失败')


if __name__ == '__main__':
    unittest.main()
