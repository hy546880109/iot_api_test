import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.mysql_data import Mysql_connet
from common.retry import Retry
from common import logging_test
@Retry
class Test_Add_Task(unittest.TestCase):

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
        """Lora网关配置修改，修改的是t_cellar_well_terminal表中的ID成功用例：/lora/updateLoraConifg"""
        ids = {
          "id": self.mysql.cellar_well_terminal_id,
          "ip": "106.52.198.240",
          "networkConnMax": 99,
          "port": 9999,
          "wakeHeartbeat": 86400
        }
        ids = json.dumps(ids)
        response = Test_Add_Task.http.post('/lora/updateLoraConifg', data=ids)
        logging_test.log_test()
        logging_test.logging.info('接口返回:' + response.text)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'Lora网关配置修改，修改的是t_cellar_well_terminal表中的ID失败')


if __name__ == '__main__':
    unittest.main()
