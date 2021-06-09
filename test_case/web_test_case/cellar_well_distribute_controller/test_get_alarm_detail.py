import json
import unittest,os,sys

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Get_Alarm_Detail(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_get_alarm_success(self):
        '''获取窖井报警详情成功用例：/device/getAlarmDetailByNo'''
        payload  = {"no":1391946012344676354}
        response = Test_Get_Alarm_Detail.http.get('/device/getAlarmDetailByNo',params=payload)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'获取窖井报警详情失败')


if __name__ == '__main__':
    unittest.main()
