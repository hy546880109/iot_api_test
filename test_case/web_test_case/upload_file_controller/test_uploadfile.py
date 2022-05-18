import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)

# from common.http_requests import HttpRequests
from config.config_test import Conf
import requests
from common.login_token import get_token
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        # cls.http = HttpRequests(cls.url)

    def test_add_task_success(self):
        '''上传文件用例：/file/uploadfile'''
        file_path = os.path.join(path,'1.bin')
        data = {'bucketName':'antian-apk'}
        payload = {
            'file': ("1.bin", open(file_path, 'rb'), 'application/x-msdownload')}
        header = {'token': get_token(), 'Accept': 'application/json, text/plain, */*'}    
        # response = Test_Add_Task.http.post('/file/uploadfile', files=payload,headers=header)
        response = requests.post(self.url + '/file/uploadfile', files=payload, data=data, headers=header)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '上传文件失败')


if __name__ == '__main__':
    unittest.main()
