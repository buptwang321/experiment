
table = {'体育': 0, '娱乐': 1, '家居': 2, '房产': 3, '教育': 4, '时尚': 5, '时政': 6, '游戏': 7, '科技': 8, '财经': 9}


def pre(r_in, w_out):
    f_in = open(r_in, 'r')
    f_out = open(w_out, 'w')
    cont = f_in.readline().strip()
    count = 0
    while cont:
        res = cont[3:] + '\t' + str(table[cont[:2]]) + '\n'
        f_out.write(res)
        print(res)
        count += 1
        cont = f_in.readline().strip()
    f_in.close()
    f_out.close()


pre('data/cnews.test.txt', 'data/test.txt')
pre('data/cnews.train.txt', 'data/train.txt')
pre('data/cnews.val.txt', 'data/dev.txt')

