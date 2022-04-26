import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
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
        cls.mysql.close()
    
    def test_add_task_success(self):
        '''新增安装指令帮助文档成功用例：/device/install/addInstallIllustrate'''
        data = [
          {
            "deviceType": 0,
            "funcCheckItem": 0,
            "id": 0,
            "illustrate": "string",
            "serialNumber": 0,
            "type": 0,
            "url": "string"
          }
        ]
        data = json.dumps(data)
        response = Test_Add_Task.http.post('/device/install/addInstallIllustrate',data=data)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'新增安装指令帮助文档失败')


if __name__ == '__main__':
    unittest.main()
