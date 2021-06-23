from common.mysql_data import Mysql_connet
from common.http_requests import HttpRequests
from config.config_test import Conf
import requests
import demjson
import json
import os
import sys
import unittest
path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.in_mysql = cls.mysql.select_sql("select id from t_device_alarm where id='1403253009441370114'")
        if cls.in_mysql is None:
            cls.mysql.insert_sql("insert  into `t_device_alarm`(`id`,`terminal_no`,`alarm_type`,`status`,`dispatch_status`,`alarm_date`,`dissolve_date`,`alarm_value`,`is_read`) values \
(1403253009441370114,'869951044459653',1,0,0,'1970-01-01 08:00:00',NULL,'10',0)")
        cls.alarm_id = cls.mysql.select_sql("select id from t_device_alarm where id='1403253009441370114'")

    def test_add_task_success(self):
        '''批量删除报警成功用例：/history/alarm/deleteBatchIds'''
        payload = [
               Test_Add_Task.alarm_id 
            ]
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post(
            '/history/alarm/deleteBatchIds', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '批量删除报警失败')


if __name__ == '__main__':
    unittest.main()
