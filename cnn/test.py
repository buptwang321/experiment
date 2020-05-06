import json
import pandas as pd

path = 'data/vectors.txt'
word = 'data/vocab.txt'
nums = 'data/vectors_num.txt'

train_data = 'data/train_num.txt'
test_data = 'data/test_num.txt'
train_json = 'data/train_json.json'
test_json = 'data/test_json.json'
train_csv = 'data/train_csv.csv'
test_csv = 'data/test_csv.csv'

# f1 = open(train_csv, 'w')
# f2 = open(test_csv, 'w')

f_train_data = open(train_data, 'r')
f_test_data = open(test_data, 'r')
# f_train_json = open(train_json, 'w')
# f_test_json = open(test_json, 'w')

f = open(path, 'r')
f_w = open(word, 'r')


cont = f_w.readline()
word_dict = dict()
count = 0
while cont:

    word = cont.split(' ')
    word_dict[word[0]] = count
    if count == 0:
        word_dict[' '] = 0
    cont = f_w.readline()
    count += 1
print(word_dict)


def v_num():
    f_n = open(nums, 'w')
    cont = f.readline()
    count = 0
    while cont:
        cont = cont.split(" ", 1)
        res = []
        res.append(str(word_dict.get(cont[0], 126865)))
        res.append(cont[1])
        w = " ".join(res)
        count += 1
        print(w)
        f_n.write(w)
        cont = f.readline()


def to_json(f_data, f_json):
    cont = f_data.readline()
    while cont:
        cont = cont.strip('\n')
        cont = cont.split(" ", 1)
        label = cont[0]
        vector = cont[1]
        temp = dict()
        print(label)
        temp['label'] = label
        temp['text'] = vector
        json.dump(temp, f_json)
        cont = f_data.readline()


def to_csv(f_data, f_csv):
    cont = f_data.readline()
    res = []
    while cont:
        cont = cont.strip('\n')
        cont = cont.split(" ", 1)
        label = cont[0]
        vector = cont[1]
        temp = dict()
        temp['label'] = label
        temp['text'] = vector
        res.append(temp)
        cont = f_data.readline()
    print(res)
    pd.DataFrame(res).to_csv(f_csv)


# to_json(f_test_data, f_test_json)
# to_json(f_train_data, f_train_json)
#v_num()
to_csv(f_train_data, train_csv)
to_csv(f_test_data, test_csv)
