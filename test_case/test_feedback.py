# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @File : test_home_page.py
# @Project: 云平台接口测试用例

import os,sys,unittest

dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)
from test_project.common.http_requests import HttpRequests

class Feedback(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = 'http://10.10.100.224:10001'
        cls.http = HttpRequests(cls.url)

    def test_001_query_feedback(self):
        '''查询所有反馈'''
        data = {"currentPage": "<currentPage>",
                "pageSize": "<pageSize>",
                "source": "<source>",
                "handleState": "<handleState>",
                "startTime": "<startTime>",
                "endTime": "<endTime>",
                "keyword": "<keyword>"}
        response = Feedback.http.post('/api/userServiceZuul/feedback/findAllFeedback',data = data)
        self.assertEqual(200,response.status_code,'返回非200')

    def test_002_add_feedback(self):
        '''新增反馈'''
        data = {
                "unit": "<unit>",
                "department": "<department>",
                "telephone": "<telephone>",
                "source": "<source>",
                "feedbackContent": "<feedbackContent>",
                "remarks": "<remarks>",
                "注意token验证": "<注意token验证>"
                }
        response = Feedback.http.post('/api/userServiceZuul/feedback/addFeedback',data = data)
        self.assertEqual(200,response.status_code,'返回非200')

    def test_003_add_feedback(self):
        '''处理反馈'''
        data = {"id": "<id>","remarks": "<remarks>"}
        response = Feedback.http.post('/api/userServiceZuul/feedback/handleFeedback',data = data)
        self.assertEqual(200,response.status_code,'返回非200')

    def test_004_add_feedback(self):
        '''删除反馈'''
        data = {'ids':''}
        response = Feedback.http.post('/api/userServiceZuul/feedback/deleteFeedback',data = data)
        self.assertEqual(200,response.status_code,'返回非200')

    def test_005_add_feedback(self):
        '''导出反馈内容'''
        data = {"source": "<source>",
                "handleState": "<handleState>",
                "startTime": "<startTime>",
                "endTime": "<endTime>",
                "keyword": "<keyword>"}
        response = Feedback.http.post('/api/userServiceZuul/feedback/exportExcel',data = data)
        self.assertEqual(200,response.status_code,'返回非200')