import cnn.identify as ii
import jieba.analyse
from bert_serving.client import BertClient
import numpy as np



finance = "finance/finance"
game = "game/game"
house = "house/house"
sports = "sports/sports"
tech = "tech/tech"
edu = "edu/edu"


# 计算每种类型用户的总关键词，并保存bert向量
def key(sentence, k):
    keywords1 = jieba.analyse.extract_tags(sentence, topK=20, withWeight=True, allowPOS=('n', 'nr', 'ns'))
    keywords2 = jieba.analyse.textrank(sentence, topK=20, withWeight=True, allowPOS=('n', 'nr', 'ns'))
    res = []
    for item in keywords2[:k]:
        res.append(item[0])
    # 三个关键词用，连接为一个string
    return ', '.join(res)


def cal(file):
    f2 = file + '_user.txt'
    f_w = open(f2, 'w')
    user = 1
    bb = []
    while user < 101:
        temp = ''
        f = file + str(user) + '.txt'
        ff = open(f, 'r')
        cont = ff.readline()
        while cont:
            temp += cont
            cont = ff.readline()
        label = ii.cnn_p(temp)
        k = key(temp, 3)
        bb.append(bc.encode([k]))
        w = label + '\t' + k + '\n'
        f_w.write(w)
        print(user, w)
        user += 1
    # 存储bert向量
    np.save(file + '_user_bert.npy', bb)


bc = BertClient()
cal(edu)


