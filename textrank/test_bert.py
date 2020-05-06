from bert_serving.client import BertClient
import numpy as np
from sklearn.cluster import KMeans


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


bc = BertClient()
a, b, c, d, e, f, g = bc.encode(['篮球', '乒乓', '钢琴', '小提琴', '蛋糕', '牛奶', '苹果'])
# temp = bc.encode(['足球', '乒乓', '钢琴', '小提琴', '蛋糕', '牛奶', '面包'])
temp = bc.encode(['乔丹, 队友, 篮球', '篮球, 球馆, 团结', '小米,开源, 贡献', '小米, 科技, 手机'])
x, y = bc.encode(['篮球', '乔丹'])
t = bc.encode(['篮球'])
print(t, t.size, type(t))
print(cos_sim(temp[0], temp[1]))
print(cos_sim(temp[0], temp[2]))
print(cos_sim(temp[1], temp[2]))
print(cos_sim(temp[2], temp[3]))

# print(cos_sim(a, b))
# print(cos_sim(a, c))
# print(cos_sim(b, c))
# print(cos_sim(c, d))
# print(cos_sim(a, d))
# print(cos_sim(a, e))
# print(cos_sim(a, f), cos_sim(c, f), cos_sim(f, g))
# print(cos_sim(x, y))
# print('a:', a, '\n\nb:', b, '\n\nc:', c)


feature = []
feature.append(a)
feature.append(b)
feature.append(e)
feature.append(c)
feature.append(d)
test = []
test.append(x)
test.append(y)
clf = KMeans(n_clusters=2)
s = clf.fit(temp)
print(s)
print(clf.labels_)
print(clf.inertia_)
print(clf.predict(test))
res = [(clf.labels_ == 1)]
print(res)

