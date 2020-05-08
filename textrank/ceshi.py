from bert_serving.client import BertClient
import time
import numpy as np
# 测试bert运行时间
def cos_sim(vector_a, vector_b):
    """
    计算两个向量之间的余弦相似度
    :param vector_a: 向量 a
    :param vector_b: 向量 b
    :return: sim
    """
    vector_a = np.mat(vector_a)
    vector_b = np.mat(vector_b)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim


def c_time(co, X):
    start = time.time()
    for _ in range(int((co/500))):
        for i in X[:500]:
            cos_sim(i, X[0])
        for i in X[500:]:
            cos_sim(i, X[1])
        for i in X[:500]:
            cos_sim(i, X[2])
    end = time.time()
    return end - start


data = []
f1 = open('data/ciku/THUOCL_it.txt', 'r')
cont = f1.readline()
count = 0
while cont and count < 1000:
    data.append(cont.split('\t')[0])
    cont = f1.readline()
    count += 1
bc = BertClient()
start = time.time()
print("bert begins")
X = bc.encode(data)
print("bert ends")
end = time.time()
print('bert time:', end-start)
print("cos time 500", c_time(500, X))
print("cos time 1000", c_time(1000, X))
print("cos time 1500", c_time(1500, X))
print("cos time 2000", c_time(2000, X))
print("cos time 2500", c_time(2500, X))
print("cos time 3000", c_time(3000, X))
print("cos time 3500", c_time(3500, X))
print("cos time 4000", c_time(4000, X))
print("cos time 4500", c_time(4500, X))
print("cos time 5000", c_time(5000, X))
