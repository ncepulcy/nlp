# coding: utf-8
"""
function：利用bosonnlp的api实现文本的分词和词性标注
token：***************************
author：lcy@ncepu.com
"""
from bosonnlp import BosonNLP
import os
nlp = BosonNLP('****************************')
f = open("NBA.txt", "r")  # 读取文本
string = f.read().decode("utf-8")
result = nlp.tag(string)
# 完整的参数调用格式如下：
# result = nlp.tag(s, space_mode=0, oov_level=3, t2s=0, special_char_conv=0)
# 修改space_mode选项为1，如下：
# result = nlp.tag(s, space_mode=1, oov_level=3, t2s=0, special_char_conv=0)
# 修改oov_level选项为1，如下：
# result = nlp.tag(s, space_mode=0, oov_level=1, t2s=0, special_char_conv=0)
# 修改t2s选项为1，如下：
# result = nlp.tag(s, space_mode=0, oov_level=3, t2s=1, special_char_conv=0)
# 修改特殊字符转换选项为1,如下：
# result = nlp.tag(s, space_mode=0, oov_level=3, t2s=0, special_char_conv=1)
f.close()
for d in result:
    print(' '.join(d['word']))  # 分词结果
for t in result:
    for word, tag in zip(t['word'], t['tag']):
        print word+" "+tag  # 词性标注结果
