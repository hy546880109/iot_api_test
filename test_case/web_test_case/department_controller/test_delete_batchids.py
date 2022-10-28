import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from common.http_requests import HttpRequests
from config.config_test import Conf
from common.mysql_data import Mysql_connet

from common import logging_test
from common.retry import Retry
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('user')
        cls.mysql.insert_user()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_user()
        cls.mysql.close()

    def test_add_task_success(self):
        '''批量删除部门成功用例：/department/deleteBatchIds'''
        payload = [self.mysql.department_id]
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post(
            '/department/deleteBatchIds', data=payload, headers=headers)
        logging_test.log_test()
        logging_test.logging.info('接口返回:' + response.text)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '批量删除部门失败')
        is_delete = self.mysql.select_sql("select is_delete from t_department where id={}".format(self.mysql.department_id))
        self.assertEqual(1,is_delete,'数据库未删除，用例执行失败')



if __name__ == '__main__':
    unittest.main()
