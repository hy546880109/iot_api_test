import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests

from common.retry import Retry
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_add_task_success(self):
        '''页面查询成功用例：/operate/log/pageQuery'''
        payload = {
            "createName": "斯元话定经书低",
            "logType": 93686580,
            "endDate": "2007-01-03",
            "pageSize": 2434082,
            "logFrom": 45580018,
            "operateType": "est reprehenderit ipsum eiusmod nisi",
            "departmentId": 82619406,
            "pageNum": 97211303,
            "addrId": 98456171,
            "startDate": "1992-12-19"
            }
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post('/operate/log/pageQuery',data=payload, headers=headers)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'页面查询失败')


if __name__ == '__main__':
    unittest.main()
