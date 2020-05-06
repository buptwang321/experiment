import jieba
import jieba.analyse

sentence = '【勐海测控站圆满完成“吉林一号”卫星发射测控任务】2019年11月13日11时40分，我国在酒泉卫星发射中心成功发射了吉林一号高分02A卫星。西安卫星测控中心勐海测控站圆满完成“吉林一号”卫星发射测控任务。火箭腾空而起数分钟后，一声声铿锵有力的口令声从机房传来。参试人员发现目标并成功捕获，设备跟踪正常，数据获取完整有效，信息处理传递正确，软硬件运行稳定，通信讯息链路畅通。（陈明）'

keywords1 = jieba.analyse.extract_tags(sentence, topK=20, withWeight=True, allowPOS=('n', 'nr', 'ns'))
keywords2 = jieba.analyse.textrank(sentence, topK=20, withWeight=True, allowPOS=('n','nr','ns'))

# print(type(keywords)
# <class 'list'>

for item in keywords1:
    print(item[0], item[1])

print('\n')

for item in keywords2:
    print(item[0], item[1])
