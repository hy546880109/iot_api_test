from common.http_requests import HttpRequests
from config.config_test import Conf
import os
import sys
import unittest
path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_add_task_success(self):
        '''上传文件用例：/file/upload'''
        payload = {
            'file': ("1.bin", open('1.bin', 'rb'), 'application/octet-stream')}
        header = {"Content-Type" :'application/octet-stream'}
        response = Test_Add_Task.http.post('/file/upload', files=payload, headers=header)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '上传文件失败')


if __name__ == '__main__':
    unittest.main()
