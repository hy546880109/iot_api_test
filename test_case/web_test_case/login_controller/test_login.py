# import pytest

from common.md5 import Md5_add
from common.http_requests import HttpRequests
from config.config_test import Conf
from common.parse_excel import ParseExcel
from common.mysql_data import select_sql
import os
import sys
import json
import ddt
import unittest

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
# print(sys.path)


def get_test_data():
    '''
    从外部获取参数数据
    :return:
    '''
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))), 'test_data')
    excelPath = os.path.join(path, 'test_user_api_data.xlsx')
    # print(excelPath)
    sheetName = '登陆用户'
    return ParseExcel(excelPath, sheetName)


@ddt.ddt
class Test_login(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    @ddt.data(*get_test_data().getDatasFromSheet())
    def test_login_success(self, data):
        '''登陆用例 /login'''
        users,passwd,code,exp = tuple(data)
        password = Md5_add(str(passwd))
        payload = {
            "code": users,
            "password": password,
            # "password": "e10adc3949ba59abbe56e057f20f883e",
            "validateCode": code       #暂时屏蔽验证码用来测试
        }
        payload = json.dumps(payload)
        response = Test_login.http.post('/login',data=payload)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertIn(exp, response.text)


if __name__ == "__main__":
    unittest.main()
