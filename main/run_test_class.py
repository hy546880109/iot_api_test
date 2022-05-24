# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例
'''
按指定类运行测试用例
'''
import os
import sys
import unittest

path = os.path.join(os.path.dirname(os.path.dirname(
    (os.path.abspath(__file__)))))
sys.path.append(path)


from test_case.web_test_case.cellar_well_controller.test_get_device_by_id import Test_get_device


if __name__ == '__main__':

    # 根据给定的测试类，获取其中所有以test开头的测试方法，并返回一个测试套件
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Test_get_device)

    # 将多个测试类加载到测试套件中
    suite = unittest.TestSuite([suite1])

    # 设置verbosity = 2，可以打印出更详细的执行信息
    unittest.TextTestRunner(verbosity=2).run(suite)