# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例

import enum

class Conf(enum.Enum):
    '''
    环境配置枚举类
    '''
    TEST_URL = 'http://10.10.100.184:10001'
    PROD_URL = 'http://10.10.100.224:10001'

    SEND_EMAIL = 'haiy@szkexin.com.cn'
    SEND_EMAIL_PASSWD = '546880109.hy'
    TO_EMAIL = ['haiy@szkexin.com.cn']
    # TO_EMAIL = ['haiy@szkexin.com.cn','zhangliguo@szkexin.com.cn','lishun@szkexin.com.cn','taochenghong@szkexin.com.cn','luqiming@szkexin.com.cn']
    foxmail = 'smtp.263.net'
    qqmail = 'smtp.qq.com'


if __name__ == '__main__':
    print(Conf.TEST_URL)
    print(Conf.TEST_URL.value)