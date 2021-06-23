import unittest
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.mysql_data import Mysql_connet


class Test_Detele_Device(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
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

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.close()

    def test_delete_device_success(self):
        '''删除窖井成功用例：/device/delete'''
        payload = {"id": Test_Detele_Device.device_id}
        response = Test_Detele_Device.http.get(
            '/device/delete', params=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '删除窖井失败')
        self.in_mysql = self.mysql.select_sql(
            'select is_delete from t_cellar_well where id=13919460123446761')   #再次查询删除标识位
        self.assertEqual(1,self.in_mysql,'数据库未删除，删除窖井用例执行失败')

if __name__ == '__main__':
    unittest.main()
