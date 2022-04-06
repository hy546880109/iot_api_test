import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Get_Alarm_Detail(unittest.TestCase):

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

    def test_get_alarm_success(self):
        '''窖井分布-获取窖井报警详情成功用例：/device/getAlarmDetailByNo'''
        payload  = {"no":self.mysql.no, 'id': self.mysql.device_id}
        response = Test_Get_Alarm_Detail.http.get('/device/getAlarmDetailByNo',params=payload)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'窖井分布-获取窖井报警详情失败')


if __name__ == '__main__':
    unittest.main()
