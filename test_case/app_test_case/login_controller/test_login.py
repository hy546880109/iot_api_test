import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)

from common.mysql_data import Mysql_connet
import ddt
from common.parse_excel import ParseExcel
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.md5 import Md5_add
from common.retry import Retry
from common import logging_test

def get_test_data():
    """
    从外部获取参数数据
    :return:
    """
    sys_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))),
        'test_data')
    excelPath = os.path.join(sys_path, 'test_user_api_data.xlsx')
    # print(excelPath)
    sheetName = '登陆用户'
    return ParseExcel(excelPath, sheetName)

@Retry
@ddt.ddt
class Test_login(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_user()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_user()
        cls.mysql.close()   

    @ddt.data(*get_test_data().getDatasFromSheet())
    def test_login_success(self, data):
        """app登陆用例 /login"""
        users, passwd, code, exp = tuple(data)
        password = Md5_add(str(passwd))
        payload = {
            "code": users,
            "password": password,
            # "password": "e10adc3949ba59abbe56e057f20f883e",
            "validateCode": code  # 暂时屏蔽验证码用来测试
        }
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = Test_login.http.post('/login', data=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertIn(exp, response.text, 'app登陆失败')
        logging_test.log_test()
        logging_test.logging.info('接口返回:' + response.text)


if __name__ == '__main__':
    unittest.main()
