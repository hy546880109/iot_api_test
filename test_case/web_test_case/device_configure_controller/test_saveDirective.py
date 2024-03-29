import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests
from common import logging_test
from common.retry import Retry
from common.doc_value import doc_parameter
uri = '/device/config/saveDirective'
@Retry
class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    @doc_parameter(Conf.TEST_URL.value,uri)
    def test_add_task_success(self):
        '''保存设备配置参数成功用例：{}{}'''
        payload = {
        "terminalNoList": [
        "ea ex nisi id",
        "dolor non dolore",
        "eiusmod pariatur mollit sit"
            ],
        "deviceParam": {
        "leanangle": 61455829,
        "port": 30686470,
        "siltHigh": 88028942,
        "wakeHeartbeat": 11451439,
        "ip": "243.234.171.86",
        "sensorHeartbeat": -565636,
        "waterLevel1": 75996823,
        "h2s": 24136066,
        "gasHeartbeat": 82786165,
        "logNum": 22702120,
        "openangle": 71452467,
        "currTime": "2000-12-17 07:14:18",
        "waterLevel2": 82763084,
        "ch4": 56476325,
        "c0": 27896988,
        "domain": "k.iqt@qq.com",
        "siltHeartbeat": 3017845
    }
}
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post(uri,data=payload)
        logging_test.log_test()
        logging_test.logging.info(Conf.TEST_URL.value + uri + '-接口返回:' + response.text)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'保存设备配置参数失败')


if __name__ == '__main__':
    unittest.main()
