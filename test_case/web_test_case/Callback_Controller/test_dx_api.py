#!/usr/bin/python
# _*_ codeing: utf-8 _*_
import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.mysql_data import Mysql_connet


class Test_Detele_Device(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_device()
        cls.device_id = cls.mysql.select_sql(
            'select id from t_cellar_well where id={}'.format(cls.mysql.device_id))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_device()
        cls.mysql.close()

    def test_delete_device_success(self):
        """���Żص��ɹ�������/cwting/callback"""
        payload = {"id": Test_Detele_Device.device_id}
        response = Test_Detele_Device.http.get(
            '/cwting/callback', params=payload)
        self.assertEqual(200, response.status_code, '���ط�200')
        self.assertEqual(str(0), str(response.json()['code']), 'ɾ���Ѿ�ʧ��')
        self.in_mysql = self.mysql.select_sql(
            'select is_delete from t_cellar_well where id={}'.format(Test_Detele_Device.device_id))  # �ٴβ�ѯɾ����ʶλ
        self.assertEqual(1, self.in_mysql, '���ݿ�δɾ����ɾ���Ѿ�����ִ��ʧ��')


if __name__ == '__main__':
    unittest.main()
