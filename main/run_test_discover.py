# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例
import os
import unittest

if __name__ == '__main__':
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'test_case')
    print(path)
    suite = unittest.defaultTestLoader.discover(path, pattern='test*.py')
    runner = unittest.TextTestRunner()
    runner.run(suite)
