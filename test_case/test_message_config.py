# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @time :  2020/12/2
# @Project: 云平台接口测试用例

from test_project.common.http_requests import HttpRequests
import unittest


class Message_config(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = 'http://10.10.100.224:10001'
        cls.http = HttpRequests(cls.url)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_001_user_list(self):
        '''获取该管辖区域下用户列表'''
        data = {"pageSize": "<pageSize>",
                "currentPage": "<currentPage>"}
        response = Message_config.http.post(
            '/api/userServiceZuul/user/getAdministerUserList', data=data)
        self.assertEqual(response.status_code, 200, '请求返回非200')

    def test_002_query_related_equipment(self):
        '''查询用户下关联设备以及管辖设备'''
        data = {}
        response = Message_config.http.post(
            '/api/publicServiceZuul/messageConfig/findRelationDevices', data=data)
        self.assertEqual(response.status_code, 200, '请求返回非200')

    def test_002_query_associated_alarms(self):
        '''查询用户下关联告警类型'''
        data = {}
        response = Message_config.http.post(
            '/api/publicServiceZuul/messageConfig/findRelationAlarmTypes', data=data)
        self.assertEqual(200, response.status_code, '请求返回非200')
        self.assertIn('10001', response.text, '响应不包含10001')

    def test_003_user_associated_alarm_type(self):
        '''用户关联告警类型'''
        payload = {'userId': globals()["equipmentid"], 'dateTime': 1}
        response = Message_config.http.post(
            '/api/publicServiceZuul/messageConfig/relationAlarmTypes', data=payload)
        self.assertEqual(200, response.status_code, '请求返回非200')
        self.assertIn('equipmentid', response.text, '响应不包含equipmentid')

    def test_004_User_associated_equipment(self):
        '''用户关联设备'''
        payload = {}
        response = Message_config.http.post(
            '/api/publicServiceZuul/messageConfig/relationDevices', data=payload)
        self.assertEqual(200, response.status_code, '请求返回非200')
        self.assertIn('win', response.text, '响应不包含win')

    def test_005_Query_company_message_configuration(self):
        '''查询公司下消息配置'''
        payload = {}
        response = Message_config.http.post(
            '/api/publicServiceZuul/messageConfig/findPushTypes', data=payload)
        self.assertEqual(200, response.status_code, '请求返回非200')
        self.assertIn('win', response.text, '响应不包含win')

    def test_006_company_message_configuration(self):
        '''公司下消息配置'''
        payload = {}
        response = Message_config.http.post(
            '/api/publicServiceZuul/messageConfig/configPushType', data=payload)
        self.assertEqual(200, response.status_code, '请求返回非200')
        self.assertIn('win', response.text, '响应不包含win')


if __name__ == '__main__':
    unittest.main()
