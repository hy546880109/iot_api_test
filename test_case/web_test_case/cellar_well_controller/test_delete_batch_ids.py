import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from common.http_requests import HttpRequests
from config.config_test import Conf
from common.mysql_data import Mysql_connet
from common.retry import Retry
@Retry
class Test_Delete_Batch(unittest.TestCase):

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

    def test_delete_batch_success(self):
        '''批量删除设备成功用例：/device/deleteBatchIds'''
        payload = [self.mysql.work_order_id]
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = Test_Delete_Batch.http.post(
            '/device/deleteBatchIds', data=payload, headers=headers)
        print('payload:', payload)
        print(response.text)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '批量删除设备失败')


if __name__ == '__main__':
    unittest.main()
