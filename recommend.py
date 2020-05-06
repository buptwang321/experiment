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


f1 = "house/house_user_bert.npy"
f2 = "recommendation/test_key_bert.npy"
f3 = "recommendation/test_key.txt"

f_test = open(f3, 'r')
user = np.load(f1).tolist()
test = np.load(f2).tolist()


label = []
bert = dict()
i = 0
cont = f_test.readline()
while cont:
    label.append(cont.split('\t')[0])
    bert[i] = test[i]
    i += 1
    cont = f_test.readline()


print(cos_sim(user[0], test[0]))
all = 0
right = 0
for item in user:
    all += 500
    result = dict()
    for i in range(len(label)):
        result[i] = cos_sim(item, bert[i])
    list1 = sorted(result.items(), key=lambda x: x[1], reverse=True)
    # print(list1)
    for r in list1[:500]:
        if label[r[0]] == '房产':
            right += 1
print(right / all)

# 5: 0.267
# 5, 10, 15, 20, 50
# sports: 0.89, 0.881, , 0.836
# finance: 0.618, 0.609, , 0.528
# game: 0.998, 0.995, , 0.965
# house: 0.976, 0.896, , 0.584
# tech: 0.53, 0.536, 0.572, 0.578, 0.538
# edu: 0.63,  0.542, 0.456, 0.405, 0.298
# all: 0.77, 0.743
