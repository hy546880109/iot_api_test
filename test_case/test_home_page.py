# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例

import random
import unittest
# import os,sys
# dir_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(dir_path)
from test_project.common.http_requests import HttpRequests
from test_project.config.config_test import Conf


class Home_page(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_001_user_statistics(self):
        '''设备、用户总数统计:  /api/statisticServiceZuul/statistic/deviceAndUserCount'''
        data = {'userId': 198}
        response = Home_page.http.post(
            '/api/statisticServiceZuul/statistic/deviceAndUserCount', data=data)
        self.assertEqual(response.status_code, 200, '请求返回非200')

    def test_002_status_statistics(self):
        '''设备状态统计:    /api/statisticServiceZuul/statistic/deviceAll'''
        data = {'userId': 198, 'deviceTypeId': 1,
                'provinceId': 1, 'cityId': 1, 'districtId': 1}
        response = Home_page.http.post(
            '/api/statisticServiceZuul/statistic/deviceAll', data=data)
        self.assertEqual(response.status_code, 200, '请求返回非200')

    def test_003_activity_statistics(self):
        '''用户活跃度统计:  /api/statisticServiceZuul/statistic/userActivity'''
        data = {'userId': 198, 'dateTime': 123456}
        response = Home_page.http.post(
            '/api/statisticServiceZuul/statistic/userActivity', data=data)
        self.assertEqual(200, response.status_code, '请求返回非200')
        self.assertIn('success', response.text, '响应不包含success')

    def test_004_trend_statistics(self):
        '''设备状态趋势统计:    /api/statisticServiceZuul/statistic/deviceStatusTrend'''
        payload = {'userId': 198, 'dateTime': 1}
        response = Home_page.http.post(
            '/api/statisticServiceZuul/statistic/deviceStatusTrend', data=payload)
        self.assertEqual(200, response.status_code, '请求返回非200')
        self.assertIn('success', response.text, '响应不包含success')

    def test_005_chang(self):
        '''设备状态较前一日变化:    /api/statisticServiceZuul/statistic/deviceStatusChange'''
        payload = {'userId': 198, 'deviceTypeId': '20001',
                   'provinceId': 1, 'cityId': 1, 'districtId': 1}
        response = Home_page.http.post(
            '/api/statisticServiceZuul/statistic/deviceStatusChange', data=payload)
        self.assertEqual(200, response.status_code, '请求返回非200')
        self.assertIn('success', response.text, '响应不包含success')


if __name__ == '__main__':
    unittest.main()
