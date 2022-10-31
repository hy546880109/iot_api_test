import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests
from common import logging_test
from common.retry import Retry
from common.doc_value import doc_parameter
uri = '/user/updatePassword'
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_add_task_success(self):
        '''修改密码成功用例：{}{}'''
        payload = {
            "oldPassword": "e10adc3949ba59abbe56e057f20f883e",
            "password": "e10adc3949ba59abbe56e057f20f883e"
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(uri,data=payload)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '修改密码失败')
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '-接口返回:' + response.text)

if __name__ == '__main__':
    unittest.main()
