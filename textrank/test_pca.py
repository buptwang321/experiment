from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from bert_serving.client import BertClient
import jieba.analyse
from sklearn.cluster import KMeans

# 此部分为制作词向量降维度展示的代码
# 首先要运行bert_client，开启bert服务

# 词向量降维在坐标系中展示

data = []
# 体育
count1 = 0
data1 = []
# 教育
count2 = 0
data2 = []
# 游戏
count3 = 0
data3 = []
# 科技
count4 = 0
data4 = []
# 财经
count5 = 0
data5 = []

# f = open("data/cnews.test.txt", "r")
#
# cont = f.readline()
# while cont:
#     label = cont[:2]
#     if label == '家居' and count1 < 10:
#         keywords1 = jieba.analyse.extract_tags(cont[2:], topK=5, withWeight=True, allowPOS=('n', 'nr', 'ns'))
#         for item in keywords1:
#             data.append(item[0])
#         count1 += 1
#     if label == '教育' and count2 < 10:
#         keywords1 = jieba.analyse.extract_tags(cont[2:], topK=5, withWeight=True, allowPOS=('n', 'nr', 'ns'))
#         for item in keywords1:
#             data.append(item[0])
#         count2 += 1
#     if label == '游戏' and count3 < 10:
#         keywords1 = jieba.analyse.extract_tags(cont[2:], topK=5, withWeight=True, allowPOS=('n', 'nr', 'ns'))
#         for item in keywords1:
#             data.append(item[0])
#         count3 += 1
#     if label == '科技' and count4 < 10:
#         keywords1 = jieba.analyse.extract_tags(cont[2:], topK=5, withWeight=True, allowPOS=('n', 'nr', 'ns'))
#         for item in keywords1:
#             data.append(item[0])
#         count4 += 1
#     if label == '财经' and count5 < 10:
#         keywords1 = jieba.analyse.extract_tags(cont[2:], topK=5, withWeight=True, allowPOS=('n', 'nr', 'ns'))
#         for item in keywords1:
#             data.append(item[0])
#         count5 += 1
#     cont = f.readline()

f1 = open('data/ciku/THUOCL_lishimingren.txt', 'r')
f2 = open('data/ciku/THUOCL_caijing.txt', 'r')
f3 = open('data/ciku/THUOCL_it.txt', 'r')
f4 = open('data/ciku/THUOCL_animal.txt', 'r')
cont = f1.readline()
count = 0
while cont and count < 1000:
    data.append(cont.split('\t')[0])
    cont = f1.readline()
    count += 1

cont = f2.readline()
count = 0
while cont and count < 1000:
    data.append(cont.split('\t')[0])
    cont = f2.readline()
    count += 1

cont = f3.readline()
count = 0
while cont and count < 1000:
    data.append(cont.split('\t')[0])
    cont = f3.readline()
    count += 1

cont = f4.readline()
count = 0
while cont and count < 1000:
    data.append(cont.split('\t')[0])
    cont = f4.readline()
    count += 1

print(data)

bc = BertClient()
X2 = bc.encode(['足球', '乒乓', '体育', '篮球场', '篮球', '苹果手机', '华为手机', '鼠标', '键盘'])
print(data)
print("bert begins")
X = bc.encode(data)
print("bert ends")
pca1 = PCA(n_components=2)
pca1.fit(X)
print(pca1.explained_variance_ratio_)
print(pca1.explained_variance_)
#返回所保留的n个成分各自的方差百分比

X_new = pca1.transform(X)
print(type(X_new))
# plt.scatter(X_new[:, 0], X_new[:, 1], marker='o')
# plt.show()

clf = KMeans(n_clusters=4)
s = clf.fit_predict(X_new)
print(clf.labels_)
res = []
b = np.vsplit(X_new, 4)
for i in range(0, 10):
    data1.append(X[i])

for i in range(10, 20):
    data2.append(X[i])

for i in range(20, 30):
    data3.append(X[i])

for i in range(30, 40):
    data4.append(X[i])

for i in range(40, 50):
    data5.append(X[i])
# plt.scatter(b[0][:, 0], b[0][:, 1], c='m')
# plt.scatter(b[1][:, 0], b[1][:, 1], c='c')
# plt.scatter(b[2][:, 0], b[2][:, 1], c='g')
# plt.scatter(b[3][:, 0], b[3][:, 1], c='b')

plt.scatter(X_new[:, 0], X_new[:, 1], c=s)
plt.show()
