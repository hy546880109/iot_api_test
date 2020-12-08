# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Mike Zhou
# @Email : 公众号：测试开发技术
# @File : run_test_discover.py
# @Project: 第26课时

import os
import unittest

if __name__ == '__main__':
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'test_case')
    print(path)
    suite = unittest.defaultTestLoader.discover(path, pattern='test*.py')
    runner = unittest.TextTestRunner()
    runner.run(suite)
