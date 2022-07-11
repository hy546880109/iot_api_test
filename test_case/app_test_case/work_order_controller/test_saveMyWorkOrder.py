import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests

from common.retry import Retry
@Retry
class Test_Get_Index(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)

    def test_get_index_success(self):
        """执行工单成功用例: /work/order/saveMyWorkOrder"""
        payload = {
            "pageNum": 1,
            "pageSize": 10
        }
        payload = json.dumps(payload)
        response = Test_Get_Index.http.post(
            '/work/order/saveMyWorkOrder', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '执行工单失败')


if __name__ == '__main__':
    unittest.main()
