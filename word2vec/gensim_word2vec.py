# coding: utf-8
from gensim.models import word2vec
import logging

# 主程序
logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus(u"fenci_head.txt")  # 加载语料
model = word2vec.Word2Vec(sentences, size=200, sg=1)  # 训练skip-gram模型，默认window=5
# 保存模型，以便重用
model.save(u"head.model")
