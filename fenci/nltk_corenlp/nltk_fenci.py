# coding: utf-8
from nltk.tokenize.stanford_segmenter import StanfordSegmenter
from nltk.tag import StanfordPOSTagger

segmenter = StanfordSegmenter(
    java_class='edu.stanford.nlp.ie.crf.CRFClassifier',
    path_to_slf4j="/home/lcy/stanford-segmenter/slf4j-api.jar",
    path_to_jar="/home/lcy/stanford-segmenter/stanford-segmenter.jar",
    path_to_sihan_corpora_dict="/home/lcy/stanford-segmenter/data/",
    path_to_model="/home/lcy/stanford-segmenter/data/pku.gz",
    path_to_dict="/home/lcy/stanford-segmenter/data/dict-chris6.ser.gz"
)
f = open("wiki.zh.text", "r")  # 读取文本
string = f.read().decode("utf-8")
result = segmenter.segment(string)  # 分词
# print result
f = open("fenci.txt", "w") # 将结果保存到另一个文档中
f.write(result.encode("utf-8"))
f.close()
