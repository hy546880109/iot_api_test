# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例

# import os,sys
# dir_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(dir_path)
import unittest
from test_project.common.http_requests import HttpRequests
from test_project.config.config_test import Conf


class Test_microservice(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)

    def test_001_query_able(self):
        '''查询所有能力层： /api/publicServiceZuul/architectureChart/findAll'''
        data = {}
        response = Test_microservice.http.post(
            '/api/publicServiceZuul/architectureChart/findAll', data=data)
        self.assertEqual(200, response.status_code, '返回非200')

    def test_002_update_able(self):
        '''新增/修改能力层：    /api/publicServiceZuul/architectureChart/saveAC'''
        data = {"userId": "198",
                "id": "1",
                "blockType": "1",
                "blockName": "super_able",
                "parentId": "7"}
        response = Test_microservice.http.post(
            '/api/publicServiceZuul/architectureChart/saveAC', data=data)
        self.assertEqual(200, response.status_code, '返回非200')

    def test_003_delete_able(self):
        '''删除能力层： /api/publicServiceZuul/architectureChart/deleteAC '''
        data = {"userId": "198",
                "id": "9"}
        response = Test_microservice.http.post(
            '/api/publicServiceZuul/architectureChart/deleteAC', data=data)
        self.assertEqual(200, response.status_code, '返回非200')


if __name__ == '__main__':
    unittest.main()
