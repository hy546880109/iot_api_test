# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Mike Zhou
# @Email : 公众号：测试开发技术
# @File : run_test_class.py
# @Project: 第25课时

'''
按指定类运行测试用例
'''

import unittest
from test_project.test_case.test_battal import TestBattal


if __name__ == '__main__':

    # 根据给定的测试类，获取其中所有以test开头的测试方法，并返回一个测试套件
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestBattal)

    # 将多个测试类加载到测试套件中
    suite = unittest.TestSuite([suite1])

    # 设置verbosity = 2，可以打印出更详细的执行信息
    unittest.TextTestRunner(verbosity=2).run(suite)