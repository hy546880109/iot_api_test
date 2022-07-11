import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
import pandas as pd
from config.config_test import Conf
from common.http_requests import HttpRequests

from common.retry import Retry
@Retry
class Test_Add_Task(unittest.TestCase):

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

    def test_add_task_success(self):
        '''报警列表导出成功用例：/history/alarm/export'''
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
        payload = json.dumps(payload)
        headers = {'Content-Type':'application/json;charset=UTF-8'}
        response = Test_Add_Task.http.post(
            '/history/alarm/export', data=payload, headers=headers)
        res = response.content
        with open('alarm.xlsx','wb')as f:   #返回的xls内容写入新的文件中
            f.write(res)
        txt = pd.read_excel(r'alarm.xlsx')  #读取文件内容用作断言
        print(txt)

        self.assertEqual(200, response.status_code, '返回非200')
        self.assertIn(str('.xlsx'),response.headers['content-disposition'] , '导出xlsx文件失败')
        self.assertIn(str('终端编号'), str(txt), '报警列表导出失败')


if __name__ == '__main__':
    unittest.main()
