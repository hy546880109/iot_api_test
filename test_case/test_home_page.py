# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @time :  2020/12/2
# @Project: 云平台接口测试用例

import unittest
import os
import sys

dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)
from test_project.common.http_requests import HttpRequests

class Home_page(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = 'http://10.10.100.224:10001'
        cls.http = HttpRequests(cls.url)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


    def test_001_user_statistics(self):
        '''设备、用户总数统计'''
        data = {'userId':198}
        response = Home_page.http.post('/api/statisticServiceZuul/statistic/deviceAndUserCount',data=data)
        self.assertEqual(response.status_code,200,'请求返回非200')

    def test_002_status_statistics(self):
        '''设备状态统计'''
        data = {'userId':198,'deviceTypeId':1,'provinceId':1,'cityId':1,'districtId':1}
        response = Home_page.http.post('/api/statisticServiceZuul/statistic/deviceAll',data=data)
        self.assertEqual(response.status_code, 200, '请求返回非200')

    def test_002_activity_statistics(self):
        '''用户活跃度统计'''
        data = {'userId': 'mikezhou', 'dateTime': 123456}
        response = Home_page.http.post('/api/statisticServiceZuul/statistic/userActivity',data=data)
        self.assertEqual(200, response.status_code, '请求返回非200')
        self.assertIn('10001', response.text, '响应不包含10001')

    def test_003_trend_statistics(self):
        '''设备状态趋势统计'''
        payload = {'userId': globals()["equipmentid"],'dateTime':1}
        response = Home_page.http.post('/api/statisticServiceZuul/statistic/deviceStatusTrend',data=payload)
        self.assertEqual(200, response.status_code, '请求返回非200')
        self.assertIn('equipmentid', response.text, '响应不包含equipmentid')

    def test_004_chang(self):
        '''设备状态较前一日变化'''
        payload = {'userId': globals()["equipmentid"], 'deviceTypeId': '20001','provinceId':1,'cityId':1,'districtId':1}
        response = Home_page.http.post('/api/statisticServiceZuul/statistic/deviceStatusChange',data=payload)
        self.assertEqual(200, response.status_code, '请求返回非200')
        self.assertIn('win', response.text, '响应不包含win')

if __name__ == '__main__':
    unittest.main()