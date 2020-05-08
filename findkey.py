import jieba.analyse


# 计算文本关键词并存储
# 原文本
finance = "finance/finance_all.txt"
game = "game/game_all.txt"
house = "house/house_all.txt"
sports = "sports/sports_all.txt"
tech = "tech/tech_all.txt"
edu = "edu/edu_all.txt"
# 存储关键词
finance_key = "finance/finance_key2.txt"
game_key = "game/game_key2.txt"
house_key = "house/house_key2.txt"
sports_key = "sports/sports_key2.txt"
tech_key = "tech/tech_key2.txt"
edu_key = "edu/edu_key2.txt"

f_finance_r = open(finance, 'r')
f_game_r = open(game, 'r')
f_house_r = open(house, 'r')
f_sports_r = open(sports, 'r')
f_tech_r = open(tech, 'r')
f_edu_r = open(edu, 'r')

f_finance_w = open(finance_key, 'w')
f_game_w = open(game_key, 'w')
f_house_w = open(house_key, 'w')
f_sports_w = open(sports_key, 'w')
f_tech_w = open(tech_key, 'w')
f_edu_w = open(edu_key, 'w')


def key(sentence, k):
    keywords1 = jieba.analyse.extract_tags(sentence, topK=20, withWeight=True, allowPOS=('n', 'nr', 'ns'))
    keywords2 = jieba.analyse.textrank(sentence, topK=20, withWeight=True, allowPOS=('n', 'nr', 'ns'))
    res = []
    for item in keywords2[:k]:
        res.append(item[0])
    # 三个关键词用，连接为一个string
    return ', '.join(res)


def write_key(f_r, f_w):
    cont = f_r.readline()
    print(cont)
    count = 0
    while count < 200:
        k = key(cont, 3)
        f_w.write(k + '\n')
        cont =f_r.readline()
        count += 1


write_key(f_finance_r, f_finance_w)
write_key(f_game_r, f_game_w)
write_key(f_house_r, f_house_w)
write_key(f_sports_r, f_sports_w)
write_key(f_tech_r, f_tech_w)
write_key(f_edu_r, f_edu_w)
