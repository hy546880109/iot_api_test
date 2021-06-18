from common.mysql_data import Mysql_connet
import requests
import demjson
import json
import os
import sys
import unittest
# path = os.path.join(os.path.dirname(os.path.dirname(
#     os.path.dirname(os.path.abspath(__file__)))))
# sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        in_mysql = cls.mysql.select_sql(
            'select is_delete from t_cellar_well where id="1403284529094864898"')
        if in_mysql is None:
            cls.mysql.insert_sql("INSERT  INTO `t_cellar_well`(`id`,`no`,`terminal_no`,`province_id`,`province_name`,`city_id`,`city_name`,`area_id`,`area_name`,`address`,`spec`,`department_id`,`department_name`,`type`,`sub_type`,`cover_type`,`is_online`,`control_status`,`status`,`is_delete`,`create_at`,`create_by`,`update_at`,`longitude`,`latitude`) VALUES \
(1403284529094864898,'123456789','869951044459653',44,'广东省',4403,'深圳市',440305,'南山区','朗山路西丽街道149号','1',1382562817882931201,'b',0,1,0,1,0,0,0,'2021-06-11 17:34:38',1377074593995628546,'2021-06-11 17:35:08','113.9482','22.55474')")
        cls.device_id = cls.mysql.select_sql(
            'select id from t_cellar_well where id="1403284529094864898"')

    def test_add_task_success(self):
        '''获取窖井详情用例：/history/alarm/getCellarWellById'''
        payload = {
            'id': Test_Add_Task.device_id
        }
        response = Test_Add_Task.http.get(
            '/history/alarm/getCellarWellById', params=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取窖井详情失败')


if __name__ == '__main__':
    unittest.main()
