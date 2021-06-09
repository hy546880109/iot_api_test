# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例

from config.config_test import Conf
import requests
import json

url = Conf.TEST_URL.value
payload = {
    "code": 'huangxc',
    "password": "e10adc3949ba59abbe56e057f20f883e",
    "validateCode": 'code'  # 暂时屏蔽验证码用来测试
}
headers = {'Content-Type': 'application/json'}
payload = json.dumps(payload)
url = url + '/login'


def get_token():
    res = requests.post(url, data=payload, headers=headers)
    token = res.json()['data']['token']
    return token


if __name__ == '__main__':
    print('url:', url)
    print('data:', payload)
    print(get_token())
    print(type(get_token()))