f_r = 'fangchan.txt'
user = 1
name = 'house/house' + str(user)
f_all = 'house/house_all.txt'
f = name + '.txt'
print(f)
ff = open(f_r, 'r')
ff_all = open(f_all, 'w')

# 197， 200

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
        name = 'house/house' + str(user)
        f = name + '.txt'
        f_temp = open(f, 'w')
