import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common.mysql_data import Mysql_connet
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.retry import Retry
from common import logging_test
from common.doc_value import doc_parameter
uri = '/operate/log/pageQuery'

@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_device()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_device()
        cls.mysql.close()

    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_add_task_success(self):
        '''获取资产用例：{}{}'''
        payload = {"terminalNo": self.mysql.no}
        payload = json.dumps(payload)

        response = Test_Add_Task.http.post('/capital/getCapitalByTerminalNoOrSensorNo', data=payload)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '获取资产失败')
        logging_test.log_test()
        logging_test.logging.info(str(Conf.TEST_URL) + uri +'接口返回:' + response.text)

if __name__ == '__main__':
    unittest.main()
