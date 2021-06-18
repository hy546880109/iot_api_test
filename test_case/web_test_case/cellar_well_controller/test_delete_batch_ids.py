from common.http_requests import HttpRequests
from config.config_test import Conf
from common.mysql_data import Mysql_connet
import unittest
import os
import sys
import json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)


class Test_Delete_Batch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.in_mysql = cls.mysql.select_sql(
            'select is_delete from t_work_order where id="1403288961291399169"')
        if cls.in_mysql is None:  # 如果不存在则插入一条数据
            cls.mysql.insert_sql("insert  into `t_work_order`(`id`,`work_no`,`work_src`,`work_type`,`terminal_no`,`alarm_id`,`user_id`,`reason`,`level`,`prv_finish_time`,`actual_finish_time`,`status`,`create_at`,`create_by`,`address`,`longitude`,`latitude`,`is_delete`,`is_read`) values \
(1403288961291399169,'GD202106118064',0,0,'869951044459653',1403278067702444033,1377074593995628546,NULL,0,'2021-06-12 00:00:00','2021-06-11 17:54:58',2,'2021-06-11 17:52:15',NULL,'南山区高新中二道粤海街道25号','113.937336','22.545404',0,1))")
        cls.work_id = cls.mysql.select_sql(
            'select id from t_work_order where id="1403288961291399169"')

    def test_delete_batch_success(self):
        '''批量删除工单成功用例：/device/deleteBatchIds'''
        payload = [Test_Delete_Batch.work_id]
        payload = json.dumps(payload)
        response = Test_Delete_Batch.http.post(
            '/device/deleteBatchIds', data=payload)
        print('payload:', payload)
        print(response.text)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '批量删除工单失败')


if __name__ == '__main__':
    unittest.main()
