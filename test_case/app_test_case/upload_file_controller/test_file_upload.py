from sys import int_info
from common.mysql_data import Mysql_connet
import unittest
import json
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Get_Index(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet("user")
        cls.in_mysql = cls.mysql.select_sql("select is_delete from t_user")
        if cls.in_mysql is None:
            cls.mysql.insert_sql("INSERT INTO t_user(code,name,password,salt,level,phone,icon,email,is_delete,status,department_id,province_id,province_name,city_id,city_name,area_id,area_name,last_login_time,create_at,create_by,update_at,update_by,remark,jpush_id) VALUES\
('hy','黄先春','2bd8934d1902b74caa2ce4f77bb84812','c0ae9feb',1,'180358812635','https://antian-iot-oss.obs.cn-south-1.myhuaweicloud.com:443/87fef3cda6e14762a572e4022a017a97.jpg','huang_xc@sohu.com',0,0,1382562817882931201,43,'湖南',4311,'永州',431129,'江华瑶族自治县','2021-06-03 09:15:10','2021-03-31 09:45:43',NULL,'2021-05-14 17:16:16',NULL,NULL,NULL)")
        cls.icon = cls.mysql.select_sql("select icon from t_user")


    def test_get_index_success(self):
        """上次头像成功用例: /user/fileUpload"""
        payload = {
            "file": Test_Get_Index.icon
        }
        response = Test_Get_Index.http.post('/user/fileUpload', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '上传头像失败')


if __name__ == '__main__':
    unittest.main()
