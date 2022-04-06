import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.data_provide import XLS
import pandas as pd



class Test_Export(unittest.TestCase):

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
            
    def test_export_success(self):
        '''导出窖井列表信息成功用例：/device/export'''
        payload = {
            "controlStatus": None,
            "no": None,
            "addrId": None,
            "bluetoothStatus": None,
            "terminalNo": None,
            "subType": None,
            "hardwareVer": None,
            "semaphore": None,
            "isOnline": None,
            "startDate": None,
            "batteryNum": None,
            "departmentId": None,
            "coverType": None,
            "status": None,
            "pageSize": 10,
            "pageNum": 1,
            "endDate": None
        }
        headers = {'Content-Type':'application/json;charset=UTF-8'}
        payload = json.dumps(payload)
        response = Test_Export.http.post(
            '/device/export', data=payload,headers=headers)
        res = response.content
        with open('device.xls','wb')as f:   #返回的xls内容写入新的文件中
            f.write(res)
        txt = pd.read_excel(r'device.xls')  #读取文件内容用作断言
        print(txt)
       
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertIn(str('终端编号'), str(txt), '导出列表信息失败')


if __name__ == '__main__':
    unittest.main()
