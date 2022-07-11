import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from common.http_requests import HttpRequests
from common.mysql_data import Mysql_connet
from config.config_test import Conf

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

    def test_add_task_success(self):
        '''查看回单结果成功用例：/work/order/getWorkOrderById'''
        payload = {
            "id": self.mysql.work_order_id,
        }

        response = Test_Add_Task.http.get(
            '/work/order/getWorkOrderById', params=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '查看回单结果失败')


if __name__ == '__main__':
    unittest.main()
