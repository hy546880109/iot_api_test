# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例

import os
import random
import hmac
import hashlib
import json
import unittest
import ddt
from test_project.common.http_requests import HttpRequests
from test_project.common.parse_excel import ParseExcel


def get_test_data():
    '''
    从外部获取参数数据
    :return:
    '''
    path = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'test_data')
    excelPath = os.path.join(path, 'test_user_api_data.xlsx')
    print(excelPath)
    sheetName = '用户参数表'
    return ParseExcel(excelPath, sheetName)


class TestUserApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = 'http://127.0.0.1:5000/'
        cls.http = HttpRequests(cls.url)
        cls.device_sn = '123456789'
        cls.os_platform = 'ios'
        cls.app_version = '1.0'
        cls.SECRET_KEY = "mikezhou"
        cls.user_id = random.randint(10, 100)
        print(cls.user_id)

    @staticmethod
    def get_token():
        '''获取token'''
        uri = '/api/get-token'
        headers = {'device_sn': TestUserApi.device_sn,
                   'os_platform': TestUserApi.os_platform,
                   'app_version': TestUserApi.app_version,
                   'Content-Type': 'application/json'}

        args = (TestUserApi.device_sn, TestUserApi.os_platform,
                TestUserApi.app_version)
        content = ''.join(args).encode('ascii')
        sign_key = TestUserApi.SECRET_KEY.encode('ascii')
        sign = hmac.new(sign_key, content, hashlib.sha1).hexdigest()
        data = {'sign': sign}
        response = TestUserApi.http.post(
            uri, data=json.dumps(data), headers=headers)
        print(response.text)
        token = response.json().get('token')
        print(token)
        return token

    def setUp(self) -> None:
        self.headers = {'device_sn': TestUserApi.device_sn,
                        'token': TestUserApi.get_token(),
                        'Content-Type': 'application/json'}
        self.playload = {'name': 'mikezhou'}

    def test_001_createUser(self):
        '''测试创建用户'''
        uri = '/api/users/{}'.format(TestUserApi.user_id)
        response = TestUserApi.http.post(
            uri, data=json.dumps(self.playload), headers=self.headers)
        print(response.text)
        self.assertEqual(response.status_code, 201, '请求返回非201')

    def test_002_query_users(self):
        '''测试查询用户'''
        uri = '/api/users/{}'.format(TestUserApi.user_id)
        response = TestUserApi.http.get(
            uri, data=json.dumps(self.playload), headers=self.headers)
        print(response.text)
        self.assertEqual(response.status_code, 200, '请求返回非200')
        self.assertIn(json.dumps(self.playload), response.text)

    def test_003_query_all_users(self):
        '''测试查询所有用户'''
        uri = '/api/users'
        response = TestUserApi.http.get(
            uri, data=json.dumps(self.playload), headers=self.headers)
        print(response.text)
        count = response.json().get('count')
        items = response.json().get('items')
        self.assertEqual(response.status_code, 200, '请求返回非200')
        self.assertEqual(count, len(items))

    def test_004_update_users(self):
        '''测试更新用户'''
        uri = '/api/users/{}'.format(TestUserApi.user_id)
        self.playload = {'name': 'mikezhou_{}'.format(random.randint(1, 10))}
        response = TestUserApi.http.put(
            uri, data=json.dumps(self.playload), headers=self.headers)
        print(response.text)
        self.assertEqual(response.status_code, 200, '请求返回非200')
        self.assertIn(json.dumps(self.playload), response.text)

    def test_005_delete_users(self):
        '''测试删除用户'''
        uri = '/api/users/{}'.format(TestUserApi.user_id)
        self.playload = {'name': 'mikezhou_{}'.format(random.randint(1, 10))}
        response = TestUserApi.http.delete(
            uri, data=json.dumps(self.playload), headers=self.headers)
        print(response.text)
        self.assertEqual(response.status_code, 200, '请求返回非200')


@ddt.ddt
class TestUserApiByTDD(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = 'http://127.0.0.1:5000/'
        cls.http = HttpRequests(cls.url)
        cls.device_sn = '123456789'
        cls.os_platform = 'ios'
        cls.app_version = '1.0'
        cls.SECRET_KEY = "mikezhou"
        cls.user_id = random.randint(10, 100)
        print(cls.user_id)

    @staticmethod
    def get_token():
        '''获取token'''
        uri = '/api/get-token'
        headers = {'device_sn': TestUserApiByTDD.device_sn,
                   'os_platform': TestUserApiByTDD.os_platform,
                   'app_version': TestUserApiByTDD.app_version,
                   'Content-Type': 'application/json'}

        args = (TestUserApiByTDD.device_sn,
                TestUserApiByTDD.os_platform, TestUserApiByTDD.app_version)
        content = ''.join(args).encode('ascii')
        sign_key = TestUserApiByTDD.SECRET_KEY.encode('ascii')
        sign = hmac.new(sign_key, content, hashlib.sha1).hexdigest()
        data = {'sign': sign}
        response = TestUserApiByTDD.http.post(
            uri, data=json.dumps(data), headers=headers)
        print(response.text)
        token = response.json().get('token')
        print(token)
        return token

    def setUp(self) -> None:
        self.headers = {'device_sn': TestUserApiByTDD.device_sn,
                        'token': TestUserApiByTDD.get_token(),
                        'Content-Type': 'application/json'}
        self.playload = {'name': 'mikezhou'}

    @ddt.data(*get_test_data().getDatasFromSheet())
    def test_001_createUser(self, data):
        '''测试创建用户'''
        users, exp = tuple(data)
        print(users, exp)
        uri = '/api/users/{}'.format(users)
        response = TestUserApiByTDD.http.post(
            uri, data=json.dumps(self.playload), headers=self.headers)
        print(response.text)
        self.assertEqual(response.status_code, 201, '请求返回非201')
        self.assertIn(exp, response.text)

    def test_002_query_all_users(self):
        '''测试查询所有用户'''
        uri = '/api/users'
        response = TestUserApiByTDD.http.get(
            uri, data=json.dumps(self.playload), headers=self.headers)
        print(response.text)
        count = response.json().get('count')
        items = response.json().get('items')
        self.assertEqual(response.status_code, 200, '请求返回非200')
        self.assertEqual(count, len(items))


if __name__ == '__main__':
    unittest.main()
