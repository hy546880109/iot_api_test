import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)

from config.config_test import Conf
import requests
from common.login_token import get_token
from common.retry import Retry
from common import logging_test
from common.doc_value import doc_parameter
uri = '/file/uploadfile'
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_add_task_success(self):
        '''上传文件用例：{}{}'''
        file_path = os.path.join(path,'1.bin')
        data = {'bucketName':'antian-apk'}
        payload = {
            'file': ("1.bin", open(file_path, 'rb'), 'application/x-msdownload')}
        header = {'token': get_token(), 'Accept': 'application/json, text/plain, */*'}
        response = requests.post(self.url + uri, files=payload, data=data, headers=header)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '上传文件失败')
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '-接口返回:' + response.text)

if __name__ == '__main__':
    unittest.main()
