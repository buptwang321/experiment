train_num = 'data/test_num.txt'
f = open(train_num, 'r')

cont = True
count = 0
while cont:
    cont = f.readline()
    print(cont)
