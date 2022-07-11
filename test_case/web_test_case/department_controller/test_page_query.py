import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
from common.http_requests import HttpRequests
from config.config_test import Conf

from common.retry import Retry
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_user()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_user()
        cls.mysql.close()
        
    def test_add_task_success(self):
        '''查询部门下所有的子部门成功用例：/department/pageQuery'''
        payload = {
            "id": self.mysql.department_id
        }
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        print('data:', payload)
        response = Test_Add_Task.http.post(
            '/department/pageQuery', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '查询部门下所有的子部门失败')


if __name__ == '__main__':
    unittest.main()
