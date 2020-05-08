# thucnews数据集的预处理，选取部分文本进行实验
file = "recommendation/recommend.txt"
file_test = "recommendation/test_all.txt"
test_sports = "recommendation/test_sports.txt"
test_entertainment = "recommendation/test_entertainment.txt"
test_home = "recommendation/test_home.txt"
test_house = "recommendation/test_house.txt"
test_edu = "recommendation/test_edu.txt"
test_fashion = "recommendation/test_fashion.txt"
test_politics = "recommendation/test_politics.txt"
test_game = "recommendation/test_game.txt"
test_tech = "recommendation/test_tech.txt"
test_finance = "recommendation/test_finance.txt"


f_all = open(file_test, 'w')
f_r = open(file, 'r')


def cal(f, label):
    print(label, '!!!!!')
    f_w = open(f, 'w')
    cont = f_r.readline()
    count = 0
    while cont and count < 1000:
        temp = cont.split('\t')
        if temp[0] == label:
            f_w.write(temp[1])
            f_all.write(cont)
            count += 1
            print(count, temp[0])
        cont = f_r.readline()


cal(test_sports, "体育")
cal(test_entertainment, "娱乐")
cal(test_home, "家居")
cal(test_house, "房产")
cal(test_edu, "教育")
cal(test_fashion, "时尚")
cal(test_politics, "时政")
cal(test_game, "游戏")
cal(test_tech, "科技")
cal(test_finance, "财经")




