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
        cls.in_mysql = cls.mysql.select_sql("select id from t_device_alarm where id='1403253009441370114'")
        if cls.in_mysql is None:
            cls.mysql.insert_sql("insert  into `t_device_alarm`(`id`,`terminal_no`,`alarm_type`,`status`,`dispatch_status`,`alarm_date`,`dissolve_date`,`alarm_value`,`is_read`) values \
(1403253009441370114,'869951044459653',1,0,0,'1970-01-01 08:00:00',NULL,'10',0)")
        cls.alarm_id = cls.mysql.select_sql("select id from t_device_alarm where id='1403253009441370114'")

    def test_add_task_success(self):
        '''获取报警的图像信息成功用例：/history/alarm/getAlarmPictures'''
        payload = {'id':Test_Add_Task.alarm_id}
        response = Test_Add_Task.http.get(
            '/history/alarm/getAlarmPictures', params=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取报警的图像信息失败')


if __name__ == '__main__':
    unittest.main()