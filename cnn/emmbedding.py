from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
import torch
from torch import nn
from torch.autograd import Variable
# 已有的glove词向量
glove_file = datapath('/Users/yukang/Desktop/bupt_bishe/cnn/data/vectors_num.txt')
# 指定转化为word2vec格式后文件的位置
tmp_file = get_tmpfile("/Users/yukang/Desktop/bupt_bishe/cnn/data/word2vector_test.txt")
# from gensim.scripts.glove2word2vec import glove2word2vec
# glove2word2vec(glove_file, tmp_file)

# 加载转化后的文件
wvmodel = KeyedVectors.load_word2vec_format(tmp_file)
# 使用gensim载入word2vec词向量

weight = torch.FloatTensor(wvmodel.syn0)

#embed
embedding = nn.Embedding.from_pretrained(weight)

print(embedding(Variable(torch.LongTensor([0]))))
