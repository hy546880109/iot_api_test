import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
from common.http_requests import HttpRequests
from config.config_test import Conf

class Test_Device_List(unittest.TestCase):

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


    def test_device_list_success(self):
        '''搜索设备成功用例：/device/pageQuery'''
        payload = {
          "pageNum": 1,
          "pageSize": 1,
          "searchField": "string",
          "type": 0
        }

        payload = json.dumps(payload)
        response = Test_Device_List.http.post('/device/pageQuery', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '搜索设备失败')


if __name__ == '__main__':
    unittest.main()
