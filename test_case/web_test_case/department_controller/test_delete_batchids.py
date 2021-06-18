from common.http_requests import HttpRequests
from config.config_test import Conf
import unittest
import os
import sys
import json
from common.mysql_data import Mysql_connet

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)


# payload = json.dumps(payload)
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('user')
        cls.in_mysql = cls.mysql.select_sql(
            'select is_delete from t_department where id="1382562817882931201"')
        if cls.in_mysql is None:   #数据库不存在则插入
            cls.mysql.insert_sql("insert  into `t_department`(`id`,`name`,`pid`,`province_id`,`province_name`,`city_id`,`city_name`,`area_id`,`area_name`,`remark`,`is_delete`,`create_at`,`create_by`,`update_at`,`update_by`) values \
(1382562817882931201,'b',0,11,'北京',1101,'北京市辖',110101,'东城区','in ut qui cillum veniam',0,'2021-04-15 13:13:57',null,'2021-06-08 18:02:27',null)")

        cls.in_mysql_2 = cls.mysql.select_sql(
            'select is_delete from t_department where id="1382571330160009218"')
        if cls.in_mysql_2 is None:  #数据库不存在则插入
            cls.mysql.insert_sql("insert  into `t_department`(`id`,`name`,`pid`,`province_id`,`province_name`,`city_id`,`city_name`,`area_id`,`area_name`,`remark`,`is_delete`,`create_at`,`create_by`,`update_at`,`update_by`) values \
(1382571330160009218,'哈哈',1382562817882931201,11,'北京',1101,'北京市辖',110101,'东城区','士大夫三大下发给消费者本工程个',1,'2021-04-15 13:47:46',null,'2021-04-15 13:48:19',null)")
        cls.department_id = cls.mysql.select_sql("select id from t_department where id='1382562817882931201'")  #数据库取值作为入参
        cls.department_id1 = cls.mysql.select_sql("select id from t_department where id='1382571330160009218'")


    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_add_task_success(self):
        '''批量删除部门成功用例：/department/deleteBatchIds'''
        payload = [Test_Add_Task.department_id, Test_Add_Task.department_id1]
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(
            '/department/deleteBatchIds', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '批量删除部门失败')
        is_delete = self.mysql.select_sql("select is_delete from t_department where id='1382562817882931201'")
        is_delete_2 = self.mysql.select_sql("select is_delete from t_department where id='1382571330160009218'")
        self.assertEqual(1,is_delete,'数据库未删除，用例执行失败')
        self.assertEqual(1,is_delete_2,'数据库未删除，用例执行失败')


if __name__ == '__main__':
    unittest.main()
