from common.mysql_data import Mysql_connet
from common.http_requests import HttpRequests
from config.config_test import Conf
import unittest


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.alarm_id = cls.mysql.select_sql("select id from t_device_alarm")

    def test_add_task_success(self):
        '''获取报警的图像信息成功用例：/history/alarm/getAlarmPictures'''
        payload = {'id':Test_Add_Task.alarm_id}
        response = Test_Add_Task.http.get(
            '/history/alarm/getAlarmPictures', params=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取报警的图像信息失败')


if __name__ == '__main__':
    unittest.main()