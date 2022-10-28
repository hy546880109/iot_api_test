import unittest,os,sys,json

import pandas as pd

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
        """导出Lora网关列表信息成功用例：/lora/export"""
        ids = {
          "name": "string",
          "startNun": 1,
          "terminalId": 1,
          "total": 1
        }
        ids = json.dumps(ids)
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        response = Test_Add_Task.http.post('/lora/export', data=ids, headers=headers)
        logging_test.log_test()
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertIn(str('.xlsx'),response.headers['content-disposition'] , '导出xlsx文件失败')
        res = response.content
        with open('lora.xlsx','wb')as f:   #返回的xls内容写入新的文件中
            f.write(res)
        txt = pd.read_excel(r'lora.xlsx')  #读取文件内容用作断言
        # print(txt)
        self.assertIn(str('设备编号'), str(txt), '导出文件的内容不正确')


if __name__ == '__main__':
    unittest.main()
