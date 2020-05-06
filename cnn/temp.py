path = 'data/vocab.txt'
f = open(path, 'r')
data = 'data/data_all.txt'
f1 = open(data, 'r')

cont = f.readline()
word_dict = dict()
count = 0
while cont:
    word = cont.split(' ')
    word_dict[word[0]] = count
    if count == 0:
        word_dict[' '] = 0
    count += 1
    cont = f.readline()

label = dict()
cont = f1.readline()
while cont:
    l = cont[:2]
    label[l] = label.get(l, 0) + 1
    cont = f1.readline()
print(label)
label_dict = dict()
for k in label.keys():
    label_dict[k] = word_dict[k]
print(label_dict)

