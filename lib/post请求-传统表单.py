#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/15 15:32
# Author    : zhangqi
# @File     : post请求-传统表单.py
# @Software : PyCharm
import requests

url = "http://httpbin.org/post"

data = {
    "name":"zhangsna",
    "age":'18'

}
header = {
    "content-type":"X-www-from-urlencoded"
}
#默认传统表单
r = requests.post(url=url,data=data,headers=header)
print(r.text)