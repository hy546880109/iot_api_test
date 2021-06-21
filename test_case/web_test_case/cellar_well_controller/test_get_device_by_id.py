from common.mysql_data import Mysql_connet
import unittest, os, sys

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests



class Test_get_device(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        in_mysql = cls.mysql.select_sql('select is_delete from t_cellar_well where id=13919460123446761')
        if in_mysql is None:
            cls.mysql.insert_sql("INSERT  INTO `t_cellar_well`(`id`,`no`,`terminal_no`,`province_id`,`province_name`,`city_id`,`city_name`,`area_id`,`area_name`,`address`,`spec`,`department_id`,`department_name`,`type`,`sub_type`,`cover_type`,`is_online`,`control_status`,`status`,`is_delete`,`create_at`,`create_by`,`update_at`,`longitude`,`latitude`) VALUES\
        (13919460123446761,'88888801','88888810',44,'广东省',4403,'深圳市',440303,'南山区','大新路南头街道88-36号','1',1382562817882931201,'b',0,0,71,1,1,0,0,'2021-06-09 10:21:29',NULL,NULL,'113.93109','22.54901')")
        elif in_mysql == 1:
            cls.mysql.update_sql("update t_cellar_well set is_delete=0 where id=13919460123446761")
        cls.device_id = cls.mysql.select_sql('select id from t_cellar_well where id=13919460123446761')
        cls.device_no = cls.mysql.select_sql("select no from t_cellar_well where id=13919460123446761")
        

    def test_get_device_success(self):
        """获取窖井详情成功用例：/device/getDeviceById"""
        payload = {'id': Test_get_device.device_id ,
        'no': Test_get_device.device_no
        }
        response = Test_get_device.http.get('/device/getDeviceById', params=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取窖井详情失败')


if __name__ == '__main__':
    unittest.main()
