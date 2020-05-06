from bert_serving.client import BertClient
import numpy as np


def cos_sim(vector_a, vector_b):
    # 计算向量a，b
    vector_a = np.mat(vector_a)
    vector_b = np.mat(vector_b)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    #返回余弦相似度结果
    return sim


finance_key = "finance/finance_key2.txt"
game_key = "game/game_key2.txt"
house_key = "house/house_key2.txt"
sports_key = "sports/sports_key2.txt"
tech_key = "tech/tech_key2.txt"
edu_key = "edu/edu_key2.txt"

finance_bert = "finance/finance__bert.npy"
game_bert = "game/game__bert.npy"
house_bert = "house/house__bert.npy"
sports_bert = "sports/sports__bert.npy"
tech_bert = "tech/tech__bert.npy"
edu_bert = "edu/edu__bert.npy"


def cal(file, f_bert):
    f_r = open(file, 'r')
    cont = f_r.readline()
    temp = []
    print("start", file)
    while cont:
        temp.append(bc.encode([cont]))
        cont = f_r.readline()
    np.save(f_bert, temp)
    print("finish", f_bert)


bc = BertClient()
cal(finance_key, finance_bert)
cal(game_key, game_bert)
cal(house_key, house_bert)
cal(sports_key, sports_bert)
cal(tech_key, tech_bert)
cal(edu_key, edu_bert)
# temp1 = bc.encode(["中学生, 同学, 几本书"])
# temp2 = bc.encode(["中学生", "同学", "几本书"])
# print("temp1:", type(temp1))
# print("temp2:", temp2)
# print(cos_sim(temp2[0], temp1))
# test = []
# test.append(temp1)
# test.append(temp2[0])
# test.append(temp2[1])
# test.append(temp2[2])
#
# np.save('a.npy', test)
# aa = np.load('a.npy')
# print(type(test), type(aa.tolist()))
# bb = aa.tolist()
# print(bb[0])
# print(test[0])
# print(cos_sim(bb[1], test[0]))
# # if aa.tolist()[0] == test[0]:
# #     print("ok")
# # else:
# #     print('no')
#
