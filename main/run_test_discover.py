# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例
import threading
import unittest,os,sys,json,time

path = os.path.join(os.path.dirname(os.path.dirname(
    (os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from lib.TestRunner.HTMLTestRunner import HTMLTestRunner
from lib.TestRunner.HTMLTestRunner import SMTP

def run_time(func):
    def wrapper(*args, **kwargs):
        old_time = time.time()
        cs = func(*args, **kwargs)
        new_time = time.time()
        print('程序运行时间：{}s'.format(round(new_time-old_time), 3))
        return cs
    return wrapper

@run_time
def run_test():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'test_case')
    print(path)
    suite = unittest.defaultTestLoader.discover(path, pattern='test*.py')
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


def tThread():
    m = threading.Thread(target=run_test, args=())
    m.run()


if __name__ == '__main__':
    tThread()



