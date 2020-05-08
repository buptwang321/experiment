import cnn.identify as ii


# 调用cnn网络接口，作文本识别并计算准确率
file = 'edu/edu_all.txt'
f_r = open(file, 'r')
cont = f_r.readline()
right = 0
all = 0
count = 0
while count < 2000:
    label = ii.cnn_p(cont)
    print(count, label)
    if label == '教育':
        right += 1
    all += 1
    count += 1
    cont = f_r.readline()
print(right, all)