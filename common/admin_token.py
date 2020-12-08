# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例

# from test_project.common.http_requests import HttpRequests
# from test_project.config.config_test import Conf

# class Get_Token():
#     @classmethod
#     def setUpClass(cls) -> None:
#         # cls.url = Conf.TEST_URL.value
#         cls.url = 'http://10.10.100.184:9997'
#         cls.http = HttpRequests(cls.url)

#     def get_tk(self):
#         '''获取token'''
#         uri = '/api/userServiceZuul/visit/login'
#         # headers = {'device_sn': TestUserApi.device_sn,
#         #            'os_platform': TestUserApi.os_platform,
#         #            'app_version': TestUserApi.app_version,
#         #            'Content-Type': 'application/json'}

#         # args = (TestUserApi.device_sn, TestUserApi.os_platform,
#         #         TestUserApi.app_version)
#         # content = ''.join(args).encode('ascii')
#         # sign_key = TestUserApi.SECRET_KEY.encode('ascii')
#         # sign = hmac.new(sign_key, content, hashlib.sha1).hexdigest()
#         data = {"username": "kexinSD",
#                 "password": "kexin168999",
#                 "companyId0": "2"}
#         response = Get_Token.http.post(
#             uri, data=data, headers=headers)
#         print(response.text.encode('utf8'))
#         token = response.json().get('token')
#         print(token)


import requests
import json

def get_token():
    url = "http://10.10.100.184:9997/api/userServiceZuul/visit/login"
    payload = {
        "username": "kexinSD",
        "password": "kexin168999",
        "companyId0": "2"
    }
    headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36'
    }

    response = requests.post(url, headers=headers, data = payload)
    responese = response.text
    s = json.loads(responese)
    tk = s['data']['token']
    auth_tk = 'Bearer '+tk
    return auth_tk

if __name__ == '__main__':
    print(get_token())