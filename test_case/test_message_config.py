# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例

import unittest
from test_project.common.http_requests import HttpRequests
from test_project.config.config_test import Conf
from test_project.common import admin_token


class Message_config(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        token = admin_token.get_token()
        cls.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
            'Authorization': token
        }

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_001_user_list(self):
        '''获取该管辖区域下用户列表:    /api/userServiceZuul/user/getAdministerUserList'''
        data = {"pageSize": "10",
                "currentPage": "1"}
        response = Message_config.http.post(
            '/api/userServiceZuul/user/getAdministerUserList', data=data, headers=self.headers)
        self.assertEqual(response.status_code, 200, '请求返回非200')

    def test_002_query_related_equipment(self):
        '''查询用户下关联设备以及管辖设备:  /api/publicServiceZuul/messageConfig/findRelationDevices'''
        data = {"pageSize": "10",
                "currentPage": "1",
                "deviceTypeId": "911",
                "userId": "198",
                "requestType": "1",
                "keyword": "",
                "provinceId": "省id",
                "cityId": "市id",
                "districtId": "区id"}
        response = Message_config.http.post(
            '/api/publicServiceZuul/messageConfig/findRelationDevices', data=data)
        self.assertEqual(response.status_code, 200, '请求返回非200')

    def test_002_query_associated_alarms(self):
        '''查询用户下关联告警类型:  /api/publicServiceZuul/messageConfig/findRelationAlarmTypes'''
        data = {"userId": "198"}
        response = Message_config.http.post(
            '/api/publicServiceZuul/messageConfig/findRelationAlarmTypes', data=data)
        self.assertEqual(200, response.status_code, '请求返回非200')
        

    def test_003_user_associated_alarm_type(self):
        '''用户关联告警类型:    /api/publicServiceZuul/messageConfig/relationAlarmTypes'''
        payload = {
            "userId": 585,
            "companyId": 98,
            "alarmTypeList": [
                {
                    "alarmIds": "32,33",
                    "deviceTypeId": 311
                },
                {
                    "alarmIds": "30,34",
                    "deviceTypeId": 911
                }
            ]
        }
        response = Message_config.http.post(
            '/api/publicServiceZuul/messageConfig/relationAlarmTypes', data=payload)
        self.assertEqual(200, response.status_code, '请求返回非200')
        

    def test_004_User_associated_equipment(self):
        '''用户关联设备：   /api/publicServiceZuul/messageConfig/relationDevices'''
        payload = {"userId": "198",
                   "companyId": "99",
                   "deviceIds": "23",
                   "deviceTypeId": "911"}
        response = Message_config.http.post(
            '/api/publicServiceZuul/messageConfig/relationDevices', data=payload)
        self.assertEqual(200, response.status_code, '请求返回非200')
       

    def test_005_Query_company_message_configuration(self):
        '''查询公司下消息配置:  /api/publicServiceZuul/messageConfig/findPushTypes'''
        payload = {"companyId": "99"}
        response = Message_config.http.post(
            '/api/publicServiceZuul/messageConfig/findPushTypes', data=payload)
        self.assertEqual(200, response.status_code, '请求返回非200')
        

    def test_006_company_message_configuration(self):
        '''公司下消息配置:  /api/publicServiceZuul/messageConfig/configPushType'''
        payload = {"companyId": "99"}
        response = Message_config.http.post(
            '/api/publicServiceZuul/messageConfig/configPushType', data=payload)
        self.assertEqual(200, response.status_code, '请求返回非200')
       


if __name__ == '__main__':
    unittest.main()
