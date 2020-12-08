# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例

import requests

# 定义一个HttpRequests的类，它的父类是object
class HttpRequests(object):

  def __init__(self,url):
    self.url = url
    self.req = requests.session()
    # self.token = admin_token.get_token()
    # self.headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    #     'Authorization':self.token
    #     }

  # 封装你自己的get请求,获取资源
  def get(self, uri='', params='', data='', headers=None, cookies=None):
      url = self.url + uri
      response = self.req.get(url, params=params, data=data, headers=headers, cookies=cookies)
      return response

  # 封装你自己的post方法，创建资源
  def post(self, uri='', params='', data='', headers=None, cookies=None):
      url = self.url + uri
      response = self.req.post(url, params=params, data=data, headers=headers, cookies=cookies)
      return response

  # 封装你自己的put方法，更新资源
  def put(self, uri='', params='', data='', headers=None, cookies=None):
      url = self.url + uri
      response = self.req.put(url, params=params, data=data, headers=headers, cookies=cookies)
      return response

  # 封装你自己的delete方法，删除资源
  def delete(self, uri='', params='', data='', headers=None, cookies=None):
      url = self.url + uri
      response = self.req.delete(url, params=params, data=data, headers=headers, cookies=cookies)
      return response