# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例
import os,sys,time
import unittest
# path = os.path.join(os.path.dirname(
#     os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(path)
from config.config_test import Conf
from lib.TestRunner.HTMLTestRunner import HTMLTestRunner
from lib.TestRunner.HTMLTestRunner import SMTP

if __name__ == '__main__':
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'test_case')
    print(path)
    suite = unittest.defaultTestLoader.discover(path, pattern='test*.py')
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    project_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    report_dir = os.path.join(project_root, 'report')
    # 测试报告地址
    current_time = time.strftime("%Y-%m-%d_%H-%M-%S")
    report_abspath = os.path.join(report_dir, "HTMLReport_{}.html".format(current_time))
    with open(report_abspath, 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='安天智慧城市项目V1.0接口自动化测试报告',
                                description='{}接口测试用例执行情况'.format(Conf.TEST_URL.value),
                                verbosity=2
                                )
        runner.run(suite)
    # smtp = SMTP(user=Conf.SEND_EMAIL.value, password=Conf.SEND_EMAIL_PASSWD.value, host=Conf.foxmail.value)   #foxmail邮箱
    smtp = SMTP(user=Conf.SEND_EMAIL.value, password=Conf.SEND_EMAIL_PASSWD.value, host=Conf.qqmail.value)      #qq邮箱
    users = Conf.TO_EMAIL.value
    smtp.sender(to=users, attachments=report_abspath, subject = '安天智慧城市项目V1.0接口自动化测试报告')



