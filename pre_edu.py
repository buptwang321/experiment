f_r = 'jiaoyu.txt'
user = 1
name = 'edu/edu' + str(user)
f_all = 'edu/edu_all.txt'
f = name + '.txt'
print(f)
ff = open(f_r, 'r')
ff_all = open(f_all, 'w')

# 194， 200

# 82.17

count = 0
count_temp = 0
f_temp = open(f, 'w')
while count < 2000:
    cont = ''
    for _ in range(6):
        cont += ff.readline().strip('\n')
    ff_all.write(cont + '\n')
    f_temp.write(cont + '\n')
    count += 1
    count_temp += 1
    if count_temp == 20:
        count_temp = 0
        user += 1
        f_temp.close()
        name = 'edu/edu' + str(user)
        f = name + '.txt'
        f_temp = open(f, 'w')
