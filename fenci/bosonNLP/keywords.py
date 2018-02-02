# -*- encoding: utf-8 -*-

"""
function：利用bosonnlp的api实现文本的关键词提取和情感分析
token：*******************************
author：lcy@ncepu.com
"""
# from __future__ import print_function, unicode_literals
import json
import requests
from bosonnlp import BosonNLP

nlp = BosonNLP('********************')  # 密令
KEYWORDS_URL = 'http://api.bosonnlp.com/keywords/analysis'  # api

f = open("NBA.txt", "r")  # 读取文本
string = f.read().decode("utf-8")
params = {'top_k': 15}   # 设置获取关键词的个数
data = json.dumps(string)  # 转成json模式
f.close()
headers = {'X-Token': '*******************'}  # 传入密令
resp = requests.post(KEYWORDS_URL, headers=headers, params=params, data=data.encode('utf-8'))  # 发送请求
# print(resp.json())  # 查看数据格式
for weight, word in resp.json():
    print (word)   # 关键词
    print(weight, word)  # 关键词和权重
result = nlp.sentiment(string)   # 返回情感分析结果
print result
