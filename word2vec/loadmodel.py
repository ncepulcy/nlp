# coding: utf-8
from gensim.models import word2vec
import logging

# 主程序
logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
model = word2vec.Word2Vec.load("wiki_head.model")
sims = model.most_similar(u"保险", topn=20)  # 20个最相关的
for item in sims:
    print item[0], item[1]
print model[u'保险']
