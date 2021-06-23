from common.mysql_data import Mysql_connet
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.data_provide import XLS
import json
import unittest
import os
import sys
import pandas as pd

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)


class Test_Export(unittest.TestCase):

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
            
    def test_export_success(self):
        '''导出窖井列表信息成功用例：/device/export'''
        payload = {
            "controlStatus": None,
            "no": None,
            "addrId": None,
            "bluetoothStatus": None,
            "terminalNo": None,
            "subType": None,
            "hardwareVer": None,
            "semaphore": None,
            "isOnline": None,
            "startDate": None,
            "batteryNum": None,
            "departmentId": None,
            "coverType": None,
            "status": None,
            "pageSize": 10,
            "pageNum": 1,
            "endDate": None
        }
        headers = {'Content-Type':'application/json;charset=UTF-8'}
        payload = json.dumps(payload)
        response = Test_Export.http.post(
            '/device/export', data=payload,headers=headers)
        res = response.content
        with open('device.xls','wb')as f:   #返回的xls内容写入新的文件中
            f.write(res)
        txt = pd.read_excel(r'device.xls')  #读取文件内容用作断言
        print(txt)
       
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertIn(str('终端编号'), str(txt), '导出窖井列表信息失败')


if __name__ == '__main__':
    unittest.main()
