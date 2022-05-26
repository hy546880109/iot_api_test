import pandas as pd
import os
import sys


def add_syspath():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))))
    sys.path.append(path)
add_syspath()
from common.http_requests import HttpRequests
from config.config_test import Conf
import unittest
import os
import sys
import json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_add_task_success(self):
        '''导出用户操作日志成功用例：/operate/log/export'''
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
        headers = {'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post('/operate/log/export', data=payload, headers=headers)
        res = response.content
        
        with open('work.xls','wb')as f:   #返回的xls内容写入新的文件中
            f.write(res)
        txt = pd.read_excel('work.xls')  #读取文件内容用作断言
        print('txt:',txt)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertIn(str('.xlsx'),response.headers['content-disposition'] , '导出xlsx文件失败')
        self.assertIn(str('操作员'), str(txt), '导出用户操作日志失败')


if __name__ == '__main__':
    unittest.main()
