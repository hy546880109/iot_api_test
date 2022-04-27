from pickle import NONE
import unittest,os,sys,json

from pymysql import NULL

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
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
            'addrId': None,
            'batteryNum': None,
            'bluetoothStatus': None,
            'controlStatus': None,
            'departmentId': None,
            'endDate': None,
            'hardwareVer': None,
            'innerCapStatus': None,
            'installStatus': None,
            'isOnline': None,
            'lockStatus': None,
            'mac': None,
            'moduleType': None,
            'name': None,
            'no': None,
            'outCapStuatus': None,
            'pageNum': 1,
            'pageSize': 10,
            'semaphore': None,
            'startDate': None,
            'startNun': 1,
            'status': None,
            'subType': None,
            'terminalNo': None,
            'total': 7,
            'type': None
        }
        headers = {'Content-Type':'application/json;charset=UTF-8'}
        payload = json.dumps(payload)
        response = Test_Export.http.post(
            '/device/export', data=payload,headers=headers)
        res = response.content
        with open('device.xlsx','wb')as f:   #返回的xls内容写入新的文件中
            f.write(res)
        txt = pd.read_excel(r'device.xlsx')  #读取文件内容用作断言
        print(txt)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertIn(str('窖井编号'), str(txt), '导出列表信息失败')



if __name__ == '__main__':
    unittest.main()
