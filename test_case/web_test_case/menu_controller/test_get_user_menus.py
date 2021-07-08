import unittest
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.mysql_data import Mysql_connet


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
    
    def test_add_task_success(self):
        '''获取用户的资源成功用例：/menu/getUserMenus'''
        payload = {
                "userId": self.mysql.user_id
            }
        response = Test_Add_Task.http.get('/menu/getUserMenus',params=payload)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'获取用户的资源失败')


if __name__ == '__main__':
    unittest.main()
