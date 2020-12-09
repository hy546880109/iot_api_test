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
import time
import unittest
from test_project.test_case.test_home_page import Home_page
from test_project.test_case.test_microservice import Test_microservice
from test_project.test_case.test_feedback import Feedback
from test_project.test_case.test_message_config import Message_config
from test_project.test_case.test_log import Log
from test_project.test_case.test_websocket import Test_websoket


from test_project.config.config_test import Conf
from test_project.lib.TestRunner.HTMLTestRunner import HTMLTestRunner
from test_project.lib.TestRunner.HTMLTestRunner import SMTP

if __name__ == '__main__':
    
    # 根据给定的测试类，获取其中所有以test开头的测试方法，并返回一个测试套件
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Home_page)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(Test_microservice)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(Feedback)
    suite4 = unittest.TestLoader().loadTestsFromTestCase(Message_config)
    suite5 = unittest.TestLoader().loadTestsFromTestCase(Log)
    suite6 = unittest.TestLoader().loadTestsFromTestCase(Test_websoket)

    # 将多个测试类加载到测试套件中
    suite = unittest.TestSuite([suite1,suite2,suite3,suite4,suite5,suite6])

    # 设置verbosity = 2，并生成HTML测试报告
    project_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    report_dir = os.path.join(project_root, 'report')
    # 测试报告地址
    current_time = time.strftime("%Y-%m-%d_%H-%M-%S")
    report_abspath = os.path.join(report_dir, "HTMLReport_{}.html".format(current_time))
    with open(report_abspath, 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='云平台V3.0接口测试报告',
                                description='测试用例执行情况',
                                verbosity=2
                                )
        runner.run(suite)
    smtp = SMTP(user=Conf.SEND_EMAIL.value, password=Conf.SEND_EMAIL_PASSWD.value, host=Conf.foxmail.value)
    users = Conf.TO_EMAIL.value
    for user in users:
        smtp.sender(to=user, attachments=report_abspath)
    


