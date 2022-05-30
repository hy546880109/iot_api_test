import unittest,os,sys,json

import pandas as pd

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
        '''导出锁信息成功用例：/key/export'''
        payload = {
          "mac": "C3:B2:5D:7E:AE:7A",
          "name": "ss",
          "pageNum": 1,
          "pageSize": 1,
          "startNum": 1,
          "total": 1,
          "userName": "string"
        }
        payload = json.dumps(payload)
        response = Test_Device_List.http.post('/key/export', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertIn(str('.xlsx'),response.headers['content-disposition'] , '导出锁信息失败')
        res = response.content
        with open('key.xlsx','wb')as f:   #返回的xls内容写入新的文件中
            f.write(res)
        txt = pd.read_excel(r'key.xlsx')  #读取文件内容用作断言
        # print(txt)
        self.assertIn(str('钥匙名称'), str(txt), '导出文件的内容不正确')


if __name__ == '__main__':
    unittest.main()
