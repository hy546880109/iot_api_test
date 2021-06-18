from common.mysql_data import Mysql_connet
import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests


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
        cls.department_id = cls.mysql.select_sql('select id from t_department where id="1382562817882931201"')
    
    def test_add_task_success(self):
        '''查询部门下所有的子部门成功用例：/department/getMySelfAndSon'''
        payload  = {"id":Test_Add_Task.department_id}
        payload = json.dumps(payload)
        print('data:',payload)
        response = Test_Add_Task.http.post('/department/getMySelfAndSon',data=payload)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'查询部门下所有的子部门失败')


if __name__ == '__main__':
    unittest.main()
