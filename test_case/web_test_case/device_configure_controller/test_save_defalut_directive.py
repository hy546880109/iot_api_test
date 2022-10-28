import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
from config.config_test import Conf
from common.http_requests import HttpRequests
from common import logging_test
from common.retry import Retry
@Retry
class Test_Add_Task(unittest.TestCase):
    '''恢复出厂接口已停用暂时不判断逻辑'''

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_device()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_device()
        cls.mysql.close()
    
    def test_add_task_success(self):
        '''恢复出厂设置成功用例：/device/config/saveDefalutDirective'''
        payload = [self.mysql.no]  
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post('/device/config/saveDefalutDirective',data=payload)
        logging_test.log_test()
        logging_test.logging.info('接口返回:' + response.text)
        self.assertEqual(200,response.status_code,'返回非200')
        # self.assertEqual(str(0), str(response.json()['code']),'恢复出厂设置失败')


if __name__ == '__main__':
    unittest.main()
