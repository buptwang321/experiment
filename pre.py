file = "toutiao_cat_data.txt"
f1 = "tiyu.txt"  # 103
f2 = "caijing.txt"  # 104
f3 = "jiaoyu.txt"  # 108
f4 = "fangchan.txt"  # 106
f5 = "keji.txt"  # 109
f6 = "youxi.txt"  # 116

ff1 = open(f1, "w")
ff2 = open(f2, "w")
ff3 = open(f3, "w")
ff4 = open(f4, "w")
ff5 = open(f5, "w")
ff6 = open(f6, "w")

f = open(file, 'r')
cont1 = f.readline()
count = 0
a1, a2, a3, a4, a5, a6 = 0, 0, 0, 0, 0, 0
while cont1:
    cont = cont1.split('_!_')
    if cont[1] == '103':
        a1 += 1
        ff1.write(cont[3]+'\n')
    elif cont[1] == '104':
        a2 += 1
        ff2.write(cont[3]+'\n')
    elif cont[1] == '108':
        a3 += 1
        ff3.write(cont[3]+'\n')
    elif cont[1] == '106':
        a4 += 1
        ff4.write(cont[3]+'\n')
    elif cont[1] == '109':
        a5 += 1
        ff5.write(cont[3]+'\n')
    elif cont[1] == '116':
        a6 += 1
        ff6.write(cont[3]+'\n')
    cont1 = f.readline()
    count += 1
print(a1, a2, a3, a4, a5, a6)
