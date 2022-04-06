# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例

import os
import sys


def add_syspath():
    path = os.path.join((os.path.dirname((
        os.path.dirname(os.path.abspath(__file__))))))
    sys.path.append(path)

add_syspath()
from config.config_test import Conf
import requests
import json
from common.mysql_data import Mysql_connet

def get_token():
    uri = Conf.TEST_URL.value
    mysql = Mysql_connet('user')
    mysql.insert_user()
    code = mysql.select_sql('select code from t_user where code="hy"')
    password = mysql.select_sql('select password from t_user where code="hy"')
    payload = {
    "code": code,
    "password": 'e10adc3949ba59abbe56e057f20f883e'
    # "validateCode": '1234'  # 暂时屏蔽验证码用来测试
    }
    headers = {'Content-Type': 'application/json','Connection': 'close'}
    payload = json.dumps(payload)
    url = uri + '/login'
    res = requests.post(url, data=payload, headers=headers)
    token = res.json()['data']['token']
    mysql.delete_user()
    return token


if __name__ == '__main__':
    print(get_token())
