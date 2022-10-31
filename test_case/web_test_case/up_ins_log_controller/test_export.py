import unittest,os,sys,json

import pandas as pd

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests
from common import logging_test
from common.retry import Retry
from common.doc_value import doc_parameter
uri = '/ins/log/export'
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_add_task_success(self):
        '''导出设备上报指令日志成功用例：{}{}'''
        payload = {
          "departmentId": 0,
          "endDate": "string",
          "ins": "string",
          "installEndDate": "string",
          "installStartDate": "string",
          "name": "string",
          "pageNum": 0,
          "pageSize": 0,
          "startDate": "string",
          "startNun": 0,
          "terminalNo": "string",
          "total": 0
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(uri,data=payload)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertIn(str('.xlsx'),response.headers['content-disposition'] , '导出xlsx文件失败')
        res = response.content
        with open('ins.xlsx','wb')as f:   #返回的xls内容写入新的文件中
            f.write(res)
        txt = pd.read_excel(r'ins.xlsx')  #读取文件内容用作断言
        print(txt)
        self.assertIn(str('指令类型'), str(txt), '导出文件的内容不正确')
        logging_test.log_test()


if __name__ == '__main__':
    unittest.main()
