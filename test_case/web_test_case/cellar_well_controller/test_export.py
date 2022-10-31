import unittest,os,sys,json,logging

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.data_provide import XLS
import pandas as pd
from common import logging_test
from common.doc_value import doc_parameter
from common.retry import Retry
uri = '/device/export'
@Retry
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
    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_export_success(self):
        '''导出窖井列表信息成功用例：{}{}'''
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
            uri, data=payload,headers=headers)
        logging_test.log_test()
        res = response.content
        with open('device.xlsx','wb')as f:   #返回的xls内容写入新的文件中
            f.write(res)
        txt = pd.read_excel(r'device.xlsx')  #读取文件内容用作断言
        print(txt)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertIn(str('.xlsx'),response.headers['content-disposition'] , '导出xlsx文件失败')
        self.assertIn(str('窖井编号'), str(txt), '导出文件的内容不正确')


if __name__ == '__main__':
    unittest.main()
