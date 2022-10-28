import requests
import json
import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from common.http_requests import HttpRequests
from config.config_test import Conf
from common import logging_test

from common.retry import Retry
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_add_task_success(self):
        """获取包上传人用例：/upgrade/package/getUploadUser"""
        headers = {'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post('/upgrade/package/getUploadUser', headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取包上传人失败')
        logging_test.log_test()
        logging_test.logging.info('接口返回:' + response.text)


if __name__ == '__main__':
    unittest.main()
