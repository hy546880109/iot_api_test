import unittest
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Detele_Device(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_delete_device_success(self):
        '''成功用例：/device/delete'''
        payload = {"id": 13}
        response = Test_Detele_Device.http.get(
            '/device/delete', params=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '删除窖井失败')


if __name__ == '__main__':
    unittest.main()
