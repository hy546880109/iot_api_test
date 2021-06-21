import unittest,os,sys,json
import pandas as pd

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
        
    
    def test_add_task_success(self):
        '''导出工单成功用例：/work/order/export'''
        payload = {
            "addrId": None,
            "pageSize": 1,
            "alarmType": None,
            "finishEndDate": None,
            "overtimeStatus": None,
            "status": None,
            "pageNum": 1,
            "departmentId": None,
            "workOrderEndDate": None,
            "workOrderStartDate": None,
            "workSrc": None,
            "finishStartDate": None
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post('/work/order/export',data=payload)
        res = response.content
        with open('work.xls','wb')as f:   #返回的xls内容写入新的文件中
            f.write(res)
        txt = pd.read_excel(r'work.xls')  #读取文件内容用作断言
        print('txt:',txt)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertIn(str('窖井编号'), str(txt),'导出工单失败')



if __name__ == '__main__':
    unittest.main()
