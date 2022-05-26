import unittest,os,sys,json

import pandas as pd

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.mysql_data import Mysql_connet

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
        cls.mysql.close()
    
    def test_add_task_success(self):
        """导出Lora网关列表信息成功用例：/lora/export"""
        ids = {
          "addrId": 0,
          "address": "string",
          "batteryNum": 0,
          "bluetoothStatus": "string",
          "controlStatus": 0,
          "coverType": 0,
          "departmentId": 0,
          "endDate": "string",
          "hardwareVer": "string",
          "innerCapStatus": 0,
          "installStatus": 0,
          "isOnline": 0,
          "lockStatus": 0,
          "mac": "string",
          "moduleType": "string",
          "name": "string",
          "no": "string",
          "outCapStuatus": 0,
          "pageNum": 0,
          "pageSize": 0,
          "semaphore": "string",
          "startDate": "string",
          "startNun": 0,
          "status": 0,
          "subType": 0,
          "terminalNo": "string",
          "total": 0,
          "type": 0
        }
        ids = json.dumps(ids)
        response = Test_Add_Task.http.post('/lora/export', data=ids)
        self.assertEqual(200,response.status_code,'返回非200')
        # self.assertIn(str('.xlsx'),response.headers['content-disposition'] , '导出xlsx文件失败')
        # res = response.content
        # with open('lora.xlsx','wb')as f:   #返回的xls内容写入新的文件中
        #     f.write(res)
        # txt = pd.read_excel(r'lora.xlsx')  #读取文件内容用作断言
        # # print(txt)
        # self.assertIn(str('钥匙名称'), str(txt), '导出文件的内容不正确')


if __name__ == '__main__':
    unittest.main()
