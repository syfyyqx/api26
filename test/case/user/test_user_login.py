#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/5/7 8:55
# Author    : zhangqi
# @File     : test_user_login.py
# @Software : PyCharm
from test.case.basecase import BaseCase
class test_user_login(BaseCase):
    def test_user_reg_ok(self):
        """level1: 测试用户登录成功"""
        case_data = self.get_case_data("login_ok")
        self.send_requset(case_data)
    def test_login_fail(self):
        #level2: 测试登录失败
        case_data = self.get_case_data("login_err")
        self.send_requset(case_data)
