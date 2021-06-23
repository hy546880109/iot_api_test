from common.mysql_data import Mysql_connet
import unittest
import json
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.in_mysql = cls.mysql.select_sql(
        'select is_delete from t_cellar_well where id=13919460123446761')
        if cls.in_mysql is None:  # 如果不存在则插入一条数据
            cls.mysql.insert_sql("INSERT  INTO `t_cellar_well`(`id`,`no`,`terminal_no`,`province_id`,`province_name`,`city_id`,`city_name`,`area_id`,`area_name`,`address`,`spec`,`department_id`,`department_name`,`type`,`sub_type`,`cover_type`,`is_online`,`control_status`,`status`,`is_delete`,`create_at`,`create_by`,`update_at`,`longitude`,`latitude`) VALUES\
        (13919460123446761,'88888801','88888810',44,'广东省',4403,'深圳市',440303,'南山区','大新路南头街道88-36号','1',1382562817882931201,'b',0,1,1,1,1,0,0,'2021-06-09 10:21:29',NULL,NULL,'113.93109','22.54901')")
        elif cls.in_mysql == 1:
            cls.mysql.update_sql("update t_cellar_well set is_delete=0 where id=13919460123446761")
        cls.device_id = cls.mysql.select_sql(
            'select id from t_cellar_well where id=13919460123446761')

    def test_add_task_success(self):
        '''更新资产用例：/capital/update'''
        payload = {
            'address': "朗山路西丽街道149号",
            'areaId': 440305,
            'areaName': "南山区",
            'cityId': 4403,
            'cityName': "深圳市",
            'coverType': 0,
            'createAt': "2021-06-12",
            'departmentId': "1404711946925690882",
            'dutyMan': "",
            'dutyManPhone': "",
            'id': "13919460123446761",
            'images1': "https://antian-iot-oss.obs.cn-south-1.myhuaweicloud.com:443/0cec685333534204a3a499ebdd76ebe3.jpg",
            'images2': None,
            'images3': None,
            'images4': None,
            'latitude': 22.545266,
            'longitude': 113.937628,
            'no': "88888801",
            'provinceId': 44,
            'provinceName': "广东省",
            'spec': "1",
            'subType': 1,
            'terminalNo': "88888810",
            'type': 0
        }
        headers = {'Content-Type': 'application/json'}
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(
            '/capital/update', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '更新资产失败')


if __name__ == '__main__':
    unittest.main()
