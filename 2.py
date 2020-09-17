import numpy as np
import jieba
import math
import re
import sys
import os
x1 = open(sys.argv[1], 'r', encoding='UTF-8')
f_x1 = x1.read()
x1.close()
x2 = open(sys.argv[2], 'r', encoding='UTF-8')
f_x2 = x2.read()
x2.close()

#读取停用词
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='UTF-8').readlines()]
    return stopwords

# 加载停用词
stopwords = stopwordslist("sim_0.8/orig.txt")

def cosine_similarity(sentence1: str, sentence2: str) -> float:
    """
    :param sentence1: s
    :param sentence2:
    :return: 两句文本的相识度
    """
    seg1 = [word for word in jieba.cut(sentence1) if word not in stopwords]
    seg2 = [word for word in jieba.cut(sentence2) if word not in stopwords]
    word_list = list(set([word for word in seg1 + seg2]))#建立词库
    word_count_vec_1 = []
    word_count_vec_2 = []
    for word in word_list:
        word_count_vec_1.append(seg1.count(word))#文本1统计在词典里出现词的次数
        word_count_vec_2.append(seg2.count(word))#文本2统计在词典里出现词的次数
    vec_1 = np.array(word_count_vec_1)
    vec_2 = np.array(word_count_vec_2)  #余弦公式

    num = vec_1.dot(vec_2.T)
    denom = np.linalg.norm(vec_1) * np.linalg.norm(vec_2)
    cos = float(num )/ denom
    count = 0.5 + 0.5 * cos
    return count
similarity= cosine_similarity(f_x1, f_x2)#计算相似度
print("\nsimilarity=%f"%similarity)
file0 = open(sys.argv[3],'w',encoding='UTF-8')
print("similarity==%f"%similarity,file=file0)




