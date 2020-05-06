import jieba
train = 'cnews/cnews.train.txt'
test = 'cnews/cnews.test.txt'
count = 0
label = dict()
data_all = 'data/data_all2.txt'
data_train = 'data/data_train2.txt'
data_test = 'data/data_test2.txt'
fo_all = open(data_all, 'r')
fo_train = open(data_train, 'r')
fo_test = open(data_test, 'r')
stopwords = [line.strip() for line in open('data/stopwords.txt',encoding='UTF-8').readlines()]
print(stopwords)
cont = True
count = 0
while cont:
    cont = fo_all.readline()
    print(cont)
    l = cont[:2]
    if l not in label:
        label[l] = 1
    else:
        label[l] += 1
    count += 1
print(count)
print(label)
with open(train, 'r', encoding='utf8') as f1:
    cont = True
    while cont:
        cont = f1.readline()
        cut_line = jieba.cut(cont)
        res = []
        for word in cut_line:
            if word not in stopwords:
                res.append(word)
        w = " ".join(res)
        fo_train.write(w)
        fo_all.write(w)

with open(test, 'r', encoding='utf8') as f2:
    cont = True
    while cont:
        cont = f2.readline()
        cut_line = jieba.cut(cont)
        res = []
        for word in cut_line:
            if word not in stopwords:
                res.append(word)
        w = " ".join(res)
        fo_test.write(w)
        fo_all.write(w)

fo_all.close()
fo_train.close()
fo_test.close()
