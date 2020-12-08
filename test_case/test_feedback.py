# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例


import unittest
# import os,sys
# dir_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(dir_path)
from test_project.common.http_requests import HttpRequests
from test_project.config.config_test import Conf
from test_project.common import admin_token

class Feedback(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        token = admin_token.get_token()
        cls.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        'Authorization':token
        }
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_001_query_feedback(self):
        # token = admin_token.get_token
        # headers = {'Authorization':token}
        '''查询所有反馈:    /api/userServiceZuul/feedback/findAllFeedback'''
        data = {"currentPage": "10",
                "pageSize": "1",
                "source": "<source>",
                "handleState": "<handleState>",
                "startTime": "<startTime>",
                "endTime": "<endTime>",
                "keyword": "<keyword>"}
        response = Feedback.http.post(
            '/api/userServiceZuul/feedback/findAllFeedback', data=data,headers=self.headers)
        self.assertEqual(200, response.status_code, '返回非200')

    def test_002_add_feedback(self):
        '''新增反馈:    /api/userServiceZuul/feedback/addFeedback'''
        data = {
            "unit": "<unit>",
            "department": "<department>",
            "telephone": "<telephone>",
            "source": "<source>",
            "feedbackContent": "<feedbackContent>",
            "remarks": "<remarks>"
        }
        response = Feedback.http.post(
            '/api/userServiceZuul/feedback/addFeedback', data=data,headers=self.headers)
        self.assertEqual(200, response.status_code, '返回非200')

    def test_003_add_processing_feedback(self):
        '''处理反馈:    /api/userServiceZuul/feedback/handleFeedback'''
        data = {"id": "<id>", "remarks": "<remarks>"}
        response = Feedback.http.post(
            '/api/userServiceZuul/feedback/handleFeedback', data=data,headers=self.headers)
        self.assertEqual(200, response.status_code, '返回非200')

    def test_004_add_delete_feedback(self):
        '''删除反馈:    /api/userServiceZuul/feedback/deleteFeedback'''
        data = {'ids': ''}
        response = Feedback.http.post(
            '/api/userServiceZuul/feedback/deleteFeedback', data=data,headers=self.headers)
        self.assertEqual(200, response.status_code, '返回非200')

    def test_005_add_export_feedback(self):
        '''导出反馈内容:    /api/userServiceZuul/feedback/exportExcel'''
        data = {"source": "<source>",
                "handleState": "<handleState>",
                "startTime": "<startTime>",
                "endTime": "<endTime>",
                "keyword": "<keyword>"}
        response = Feedback.http.post(
            '/api/userServiceZuul/feedback/exportExcel', data=data,headers=self.headers)
        self.assertEqual(200, response.status_code, '返回非200')


if __name__ == '__main__':
    unittest.main()
