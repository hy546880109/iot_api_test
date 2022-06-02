import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)

from config.config_test import Conf
import requests
from common.login_token import get_token
# from common.http_requests import HttpRequests
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        # cls.http = HttpRequests(cls.url)

    def test_add_task_success(self):
        '''上传文件用例：/file/upload'''
        file_path = os.path.join(path,'1.bin')

        payload = {
            'file': ("1.bin", open(file_path, 'rb'), 'application/octet-stream')}
        header = {'token': get_token()}
        # response = Test_Add_Task.http.post('/file/upload', files=payload,headers=header)
        response = requests.post(self.url + '/file/upload', files=payload,headers=header)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '上传文件失败')


if __name__ == '__main__':
    unittest.main()
