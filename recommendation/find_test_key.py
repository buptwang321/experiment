import jieba.analyse


def key(sentence, k):
    keywords1 = jieba.analyse.extract_tags(sentence, topK=20, withWeight=True, allowPOS=('n', 'nr', 'ns'))
    keywords2 = jieba.analyse.textrank(sentence, topK=20, withWeight=True, allowPOS=('n', 'nr', 'ns'))
    res = []
    for item in keywords2[:k]:
        res.append(item[0])
    # 三个关键词用，连接为一个string
    return ', '.join(res)


file = 'test_all.txt'
f_r = open(file, 'r')
f_w = open('test_key.txt', 'w')
cont = f_r.readline()
count = 0
while cont:
    temp = cont.split('\t')
    k = key(temp[1], 3)
    f_w.write(temp[0] + '\t' + k + '\n')
    cont = f_r.readline()
    count += 1
    print(count)
