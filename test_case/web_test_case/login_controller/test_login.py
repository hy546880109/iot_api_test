# import pytest

from common.md5 import Md5_add
from common.http_requests import HttpRequests
from config.config_test import Conf
from common.parse_excel import ParseExcel
from common.mysql_data import Mysql_connet
import os
import sys
import json
import ddt
import unittest


def get_test_data():
    '''
    从外部获取参数数据
    :return:
    '''
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))), 'test_data')
    excelPath = os.path.join(path, 'test_user_api_data.xlsx')
    sheetName = '登陆用户'
    return ParseExcel(excelPath, sheetName)


@ddt.ddt
class Test_login(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        mysql = Mysql_connet('user')
        in_data = mysql.select_sql("select is_delete from t_user where code='hy'")
        if in_data is None:
            mysql.insert_sql("INSERT INTO t_user(code,name,password,salt,level,phone,icon,email,is_delete,status,department_id,province_id,province_name,city_id,city_name,area_id,area_name,last_login_time,create_at,create_by,update_at,update_by,remark,jpush_id) VALUES\
('hy','黄先春','2bd8934d1902b74caa2ce4f77bb84812','c0ae9feb',1,'180358812635','https://antian-iot-oss.obs.cn-south-1.myhuaweicloud.com:443/87fef3cda6e14762a572e4022a017a97.jpg','huang_xc@sohu.com',0,0,1382562817882931201,43,'湖南',4311,'永州',431129,'江华瑶族自治县','2021-06-03 09:15:10','2021-03-31 09:45:43',NULL,'2021-05-14 17:16:16',NULL,NULL,NULL)")

        
    @ddt.data(*get_test_data().getDatasFromSheet())
    def test_login_success(self, data):
        '''登陆用例 /login'''
        users,passwd,code,exp = tuple(data)
        password = Md5_add(str(passwd))
        payload = {
            "code": users,
            "password": password,
            # "password": "e10adc3949ba59abbe56e057f20f883e",
            "validateCode": code       #暂时屏蔽验证码用来测试
        }
        payload = json.dumps(payload)
        response = Test_login.http.post('/login',data=payload)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertIn(exp, response.text)


if __name__ == "__main__":
    unittest.main()
