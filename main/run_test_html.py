'''
Author: HY\harry hy546880109@qq.com
Date: 2023-02-09 18:20:14
LastEditors: HY\harry hy546880109@qq.com
LastEditTime: 2023-04-24 10:15:41
FilePath: \iot_api_test\main\run_test_html.py
Description: 
'''
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例

'''
按指定类运行测试用例，并生成测试报告
'''

import os
import sys


def add_syspath():
    path = os.path.join((os.path.dirname((
        os.path.dirname(os.path.abspath(__file__))))))
    sys.path.append(path)

add_syspath()

import time
import unittest
from test_case.web_test_case.operation_log_controller.test_page_query import Test_Add_Task
# from test_case.web_test_case.operation_log_controller.test_page_query import Test_Add_Task
# from test_case.app_test_case.cellar_well_controller.test_get_my_info import Test_Add_Task

from config.config_test import Conf
from lib.TestRunner.HTMLTestRunner import HTMLTestRunner
from lib.TestRunner.HTMLTestRunner import SMTP

if __name__ == '__main__':
    
    # 根据给定的测试类，获取其中所有以test开头的测试方法，并返回一个测试套件
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Test_Add_Task)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(Test_Add_Task)
    

    # 将多个测试类加载到测试套件中
    # suite = unittest.TestSuite([suite1,suite2])
    suite = unittest.TestSuite([suite1])

    # 设置verbosity = 2，并生成HTML测试报告s
    project_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    report_dir = os.path.join(project_root, 'report')
    # 测试报告地址
    current_time = time.strftime("%Y-%m-%d_%H-%M-%S")
    report_abspath = os.path.join(report_dir, "HTMLReport_{}.html".format(current_time))
    with open(report_abspath, 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='安天云平台V1.0接口自动化测试报告',
                                description='接口测试用例执行情况',
                                verbosity=2
                                )
        runner.run(suite)
    # smtp = SMTP(user=Conf.SEND_EMAIL.value, password=Conf.SEND_EMAIL_PASSWD.value, host=Conf.foxmail.value) 
    # users = Conf.TO_EMAIL.value
    # smtp.sender(to=users, attachments=report_abspath, subject = '安天云平台V1.0接口自动化测试报告')
    

    smtp = SMTP(user=Conf.SEND_EMAIL.value, password=Conf.SEND_EMAIL_PASSWD.value, host=Conf.qqmail.value)      #qq邮箱
    users = Conf.TO_EMAIL.value
    smtp.sender(to=users, attachments=report_abspath, subject = '安天智慧城市项目V1.0接口自动化测试报告')

