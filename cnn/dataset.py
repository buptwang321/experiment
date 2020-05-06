import torchtext.data as data
from sklearn.model_selection import train_test_split
import pandas as pd


def split_val():
    train_data = pd.read_csv('data/train_csv.csv')
    train, val = train_test_split(train_data, test_size=0.2)
    train.to_csv("data/train.csv", index=False)
    val.to_csv("data/val.csv", index=False)


def to_int(text):
    res = []
    for item in text.split():
        item = int(item)
        res.append(item)
    return res


def get_field():
    text_field = data.Field(use_vocab=False, sequential=True, tokenize=to_int, pad_token=0)
    label_field = data.Field(use_vocab=False, sequential=False)
    return text_field, label_field


def get_iter():
    text_field = data.Field(use_vocab=False, sequential=True, tokenize=to_int, pad_token=0)
    label_field = data.Field(use_vocab=False, sequential=False)

    tv_datafields = [("Unnamed: 0", None), # 我们不会需要id，所以我们传入的filed是None
                     ("label", label_field),
                     ("text", text_field)]

    test_datafields = [('id', None),
                       ("label", label_field),
                       ("text", text_field)]

    trn, vld = data.TabularDataset.splits(
                   path="data", # 数据存放的根目录
                   train='train.csv', validation="val.csv",
                   format='csv',
                   skip_header=True, # 如果你的csv有表头, 确保这个表头不会作为数据处理
                   fields=tv_datafields)

    test = data.TabularDataset(
                    path="data/test_csv.csv",
                    format='csv',
                    skip_header=True,
                    fields=test_datafields)

    print(trn[1].__dict__.keys())
    print(vld[0].text)
    print(type(tv_datafields))
    print(test[0].label, test[0].text, '!!!!!!!')

    train_iter, val_iter = data.BucketIterator.splits(
                                                 (trn, vld),
                                                 batch_sizes=(25, 25),
                                                 device=-1,
                                                 # 如果要用GPU，这里指定GPU的编号
                                                 sort_key=lambda x: len(x.text),
                                                 # BucketIterator 依据什么对数据分组
                                                 sort_within_batch=False,
                                                 repeat=False)
    test_iter = data.BucketIterator(
                                test,
                                batch_size=64,
                                device=-1,
                                sort=False,
                                sort_within_batch=False,
                                repeat=False)

    print(val_iter)
    print(val_iter.__dict__.keys())

    return train_iter, val_iter, test_iter
