import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.mysql_data import Mysql_connet 

from common.retry import Retry
@Retry
class Test_Detele_Device(unittest.TestCase):

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

    def test_delete_device_success(self):
        '''删除窖井成功用例：/device/delete'''
        payload = {"id": self.mysql.device_id}
        response = Test_Detele_Device.http.get(
            '/device/delete', params=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '删除窖井失败')
        self.in_mysql = self.mysql.select_sql(
            'select is_delete from t_cellar_well where id={}'.format(self.mysql.device_id))   #再次查询删除标识位
        self.assertEqual(1,self.in_mysql,'数据库未删除，删除窖井用例执行失败')

if __name__ == '__main__':
    unittest.main()
