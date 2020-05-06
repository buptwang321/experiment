import jieba


def predict(text):
    f = open('./cnn/data/vocab.txt', 'r')
    stopwords = [line.strip() for line in open('./cnn/data/stopwords.txt', encoding='UTF-8').readlines()]
    cont = f.readline()
    word_dict = dict()
    count = 0
    while cont:

        word = cont.split(' ')
        word_dict[word[0]] = count
        if count == 0:
            word_dict[' '] = 0
        cont = f.readline()
        count += 1
    cut_line = jieba.cut(text)
    res = []
    for word in cut_line:
        if word not in stopwords:
            res.append(word)

    num = []
    for word in res:
        if word in word_dict and word != ' ':
            num.append(str(word_dict[word]))
    return ' '.join(num)
