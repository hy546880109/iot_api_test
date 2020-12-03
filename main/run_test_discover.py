# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @time :  2020/12/2
# @Project: 云平台接口测试用例

import os
import unittest
from HTMLTestRunner import HTMLTestRunner
import time


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'test_case')
    suite = unittest.defaultTestLoader.discover(path, pattern='test*.py')
    test_dir = './report/'
    filename = test_dir  + now + 'api.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp, title='云平台接口测试报告',description='测试用例情况:')
    runner.run(suite)
