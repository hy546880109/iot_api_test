# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例

import unittest
from test_project.common.http_requests import HttpRequests
from test_project.config.config_test import Conf


class Log(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_001_query_device_log(self):
        '''查询设备日志:    /api/deviceLogServiceZuul/deviceLog/findDeviceLogs '''
        data = {}
        response = Log.http.post(
            '/api/deviceLogServiceZuul/deviceLog/findDeviceLogs', data=data)
        self.assertEqual(200, response.status_code, '返回非200')

    def test_002_query_sys_log(self):
        '''查询系统日志:    /api/deviceLogServiceZuul/deviceLog/findSystemLogs '''
        data = {}
        response = Log.http.post(
            '/api/deviceLogServiceZuul/deviceLog/findSystemLogs', data=data)
        self.assertEqual(200, response.status_code, '返回非200')

    def test_003_delete_device_log(self):
        '''删除设备日志:    /api/deviceLogServiceZuul/deviceLog/deleteDeviceLogs '''
        data = {}
        response = Log.http.post(
            '/api/deviceLogServiceZuul/deviceLog/deleteDeviceLogs', data=data)
        self.assertEqual(200, response.status_code, '返回非200')

    def test_004_delete_sys_log(self):
        '''删除系统日志:    /api/deviceLogServiceZuul/deviceLog/deleteSystemLogs '''
        data = {}
        response = Log.http.post(
            '/api/deviceLogServiceZuul/deviceLog/deleteSystemLogs', data=data)
        self.assertEqual(200, response.status_code, '返回非200')

    def test_005_delete_user_log(self):
        '''删除用户日志:    /api/deviceLogServiceZuul/deviceLog/deleteUserLogs '''
        data = {}
        response = Log.http.post(
            '/api/deviceLogServiceZuul/deviceLog/deleteUserLogs', data=data)
        self.assertEqual(200, response.status_code, '返回非200')

    def test_006_export_device_log(self):
        '''导出设备日志：   /api/deviceLogServiceZuul/deviceLog/deviceLogExport '''
        data = {}
        response = Log.http.post(
            '/api/deviceLogServiceZuul/deviceLog/deviceLogExport', data=data)
        self.assertEqual(200, response.status_code, '返回非200')

    def test_007_export_sys_log(self):
        '''导出系统日志：   /api/deviceLogServiceZuul/deviceLog/systemLogExport '''
        data = {}
        response = Log.http.post(
            '/api/deviceLogServiceZuul/deviceLog/systemLogExport', data=data)
        self.assertEqual(200, response.status_code, '返回非200')

    def test_008_export_user_log(self):
        '''导出用户日志：   /api/deviceLogServiceZuul/deviceLog/userLogExport '''
        data = {}
        response = Log.http.post(
            '/api/deviceLogServiceZuul/deviceLog/userLogExport', data=data)
        self.assertEqual(200, response.status_code, '返回非200')

    def test_009_query_user_log(self):
        '''查询用户操作日志:    /api/deviceLogServiceZuul/deviceLog/findUserLogs '''
        data = {}
        response = Log.http.post(
            '/api/deviceLogServiceZuul/deviceLog/findUserLogs', data=data)
        self.assertEqual(200, response.status_code, '返回非200')


if __name__ == '__main__':
    unittest.main()
