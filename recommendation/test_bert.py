from bert_serving.client import BertClient
import numpy as np


bc = BertClient()
f_r = open('test_key.txt', 'r')
f_w = 'test_key_bert'
cont = f_r.readline()
temp = []
count = 0
while cont:
    key = cont.split('\t')
    print(key)
    if key[1] == '\n':
        temp.append(bc.encode(['空白']))
    else:
        temp.append(bc.encode([key[1]]))
    cont = f_r.readline()
    count += 1
    print(count)
np.save(f_w, temp)
