# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例

from enum import Enum
from sys import argv

if len(argv) == 1:
    ip = '106.52.198.240'
else:
    ip = argv[1]
class Conf(Enum):
    '''
    环境配置枚举类
    '''
    # TEST_URL = 'http://124.71.31.43:9527/admin/v1.0'
    # TEST_URL = 'http://139.159.199.99:9527/admin/v1.0'
    # TEST_URL = 'http://106.52.198.240:9527/admin/v1.0'
    TEST_URL =   'http://' + ip + ':9527/admin/v1.0'


    # TEST_APP_URL = 'http://124.71.31.43:9527/api/v1.0'
    # TEST_APP_URL = 'http://139.159.199.99:9527/api/v1.0'
    # TEST_APP_URL = 'http://106.52.198.240:9527/api/v1.0'
    TEST_APP_URL =   'http://' + ip + ':9527/api/v1.0'

    host = '106.52.198.240'
    port = 3306
    user = 'root'
    # password = 'Antian!2020'
    password = 'Root_2021'

    # host = '139.159.202.43'
    # port = 3306
    # user = 'root'
    # password = 'Antian!2020'

    SEND_EMAIL = 'hy546880109@qq.com'
    SEND_EMAIL_PASSWD = 'lwveldyrecfybdce'  # 邮箱授权码
    TO_EMAIL = ['hy546880109@qq.com']

    foxmail = 'smtp.263.net'
    qqmail = 'smtp.qq.com'

if __name__ == '__main__':

    print(Conf.TEST_URL)
    print(Conf.TEST_URL.value)
    print(','.join(Conf.TO_EMAIL.value))
