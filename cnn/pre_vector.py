import config
cnn = config.CNN()

path = 'data/vocab.txt'
data_train = 'data/data_train.txt'
data_test = 'data/data_test.txt'
train_num = 'data/train_num.txt'
test_num = 'data/test_num.txt'
f1 = open(data_train, 'r')
f2 = open(data_test, 'r')
# f3 = open(train_num, 'w')
# f4 = open(test_num, 'w')
f = open(path, 'r')
cont = True
word_dict = dict()
count = 0
while cont:
    cont = f.readline()
    word = cont.split(' ')
    word_dict[word[0]] = count
    if count == 0:
        word_dict[' '] = 0
    count += 1
for k, v in word_dict.items():
    if v == 0:
        print(k)
cont = f1.readline().split()
while cont:
    res = []
    temp = cont[0]
    res.append(str(cnn.label_dict[word_dict[temp]]))
    for word in cont[1:]:
        if word in word_dict and word != ' ':
            res.append(str(word_dict[word]))
    w = ' '.join(res)
    cont = f1.readline().split()
    # f3.write(w + '\n')

cont = f2.readline().split()
while cont:
    res = []
    temp = cont[0]
    res.append(str(cnn.label_dict[word_dict[temp]]))
    for word in cont[1:]:
        if word in word_dict and word != ' ':
            res.append(str(word_dict[word]))
    w = ' '.join(res)
    cont = f2.readline().split()
    # f4.write(w + '\n')
f1.close()
f2.close()
# f3.close()
# f4.close()