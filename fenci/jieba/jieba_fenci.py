# -*- encoding: utf-8 -*-
"""
function：利用jieba的python库实现文本的分词相关功能
author：lcy@ncepu.com
"""
import jieba
import jieba.posseg as pseg

# 分词
from jieba import analyse

f = open("NBA.txt", "r")  # 读取文本
string = f.read().decode("utf-8")

seg_list = jieba.cut(string, cut_all=True)
print("Full Mode: " + " ".join(seg_list))  # 全模式

seg_list = jieba.cut(string, cut_all=False)
print("Default Mode: " + " ".join(seg_list))  # 精确模式

seg_list = jieba.cut_for_search(string)  # 搜索引擎模式
print(" ".join(seg_list))

f = open("jieba_fenci.txt","w")  # 将结果保存到另一个文档中
f.write(" ".join(seg_list).encode("utf-8"))
f.close()

# 词性标注
words = pseg.cut(string)
for word, flag in words:
    print('%s %s' % (word, flag))

# 关键字提取
keywords = analyse.extract_tags(string, topK=15, withWeight=True, allowPOS=())
for a in keywords:
    print str(a[1])+a[0]

# 关键词提取，无权重
keys = analyse.extract_tags(string, topK=15, withWeight=False, allowPOS=())
print " ".join(keys)
