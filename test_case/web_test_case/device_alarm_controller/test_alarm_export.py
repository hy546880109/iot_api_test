import json
import unittest

import pandas as pd
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        

    def test_add_task_success(self):
        '''报警列表导出成功用例：/history/alarm/export'''
        payload = {
            "terminalNo": "8888888031",
            "alarmStartDate": "2003-08-07",
            "alarmType": 1,
            "addrId": 440305,
            "departmentId": 1382562817882931201,
            "dissolveEndDate": "2015-04-06",
            "alarmEndDate": "1997-01-19",
            "dissolveStartDate": "2003-04-14",
            "status": 0,
            "pageSize": 1,
            "pageNum": 10,
            "dispatchStatus": 1
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(
            '/history/alarm/export', data=payload)
        res = response.content
        with open('alarm.xls','wb')as f:   #返回的xls内容写入新的文件中
            f.write(res)
        txt = pd.read_excel(r'alarm.xls')  #读取文件内容用作断言
        print(txt)

        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '报警列表导出失败')


if __name__ == '__main__':
    unittest.main()
