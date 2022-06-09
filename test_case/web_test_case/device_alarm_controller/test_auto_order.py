import unittest,os,sys,json
import requests

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
# from common.http_requests import HttpRequests
from config.config_test import Conf
from common.login_token import get_token

class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        # cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_device()
        cls.mysql.insert_user()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_device()
        cls.mysql.delete_user()
        cls.mysql.close()

    def test_add_task_success(self):
        '''自动派单成功用例：/history/alarm/autoDistributeTask'''
        payload = [
            # self.mysql.alarm_id
            1514149491463188482
        ]

        payload = json.dumps(payload)
        # cookies = dict(cookieucode='admin',cookieupwd='e10adc3949ba59abbe56e057f20f883e')
        header = {'token':get_token(),"Origin":'http://106.52.198.240:8081',"Content-Type": "application/json"}
        # response = Test_Add_Task.http.post(
        #     '/history/alarm/autoDistributeTask', data=payload, headers=header)
        response = requests.post(
            self.url + '/history/alarm/autoDistributeTask', data=payload, headers=header)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '派单失败')


if __name__ == '__main__':
    unittest.main()
