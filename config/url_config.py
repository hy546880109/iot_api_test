# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Mike Zhou
# @Email : 公众号：测试开发技术
# @File : url_config.py
# @Project: 第29课时

import enum

class URLConf(enum.Enum):
    '''
    环境配置枚举类
    '''
    TEST_URL = 'http://10.10.100.184:10001'
    PROD_URL = 'http://10.10.100.224:10001'


if __name__ == '__main__':
    print(URLConf.TEST_URL.name)
    print(URLConf.TEST_URL.value)