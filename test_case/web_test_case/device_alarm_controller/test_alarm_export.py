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
            "terminalNo": None,
            "alarmStartDate": None,
            "alarmType": None,
            "addrId": None,
            "departmentId": None,
            "dissolveEndDate": None,
            "alarmEndDate": None,
            "dissolveStartDate": None,
            "status":None,
            "pageSize": 1,
            "pageNum": 10,
            "dispatchStatus": None
        }
        payload = json.dumps(payload)
        headers = {'Content-Type':'application/json;charset=UTF-8'}
        response = Test_Add_Task.http.post(
            '/history/alarm/export', data=payload, headers=headers)
        res = response.content
        with open('alarm.xls','wb')as f:   #返回的xls内容写入新的文件中
            f.write(res)
        txt = pd.read_excel(r'alarm.xls')  #读取文件内容用作断言
        print(txt)

        self.assertEqual(200, response.status_code, '返回非200')
        self.assertIn(str('终端编号'), str(txt), '报警列表导出失败')


if __name__ == '__main__':
    unittest.main()
