import os
import datetime
import torch
import cnn.train as train
import cnn.model as model
import cnn.dataset as dataset
import cnn.config as config
import cnn.predict as predict

# path = '/Users/yukang/Desktop/Django-2.2.5/testdj/cnn/data/save/snapshot/2019-10-31_13-41-31/best_steps_6800.pt'
path = '/Users/yukang/Desktop/weibo/pre/cnn/data/save/bert_cnn.pt'
args = config.CNN()
cnn = model.CNN_Text(args)
cnn.load_state_dict(torch.load(path))
# print(args.embed_dim)
# print(args.embed_num)
args.save_dir = os.path.join(args.save_dir, datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
# print(args.save_dir)

# train_iter, val_iter, test_iter = dataset.get_iter()

# train.train(train_iter, val_iter, cnn, args)
# print("训练完成！***********************************************************")
# train.eval(test_iter, cnn, args)
# print(type(cnn))
#train.eval(test_iter, cnn, args)

text_field, label_field = dataset.get_field()
# label = train.predict(predict.predict(args.predict), cnn, text_field, label_field, args.cuda)
# print('\n[Text]  {}\n[Label] {}\n'.format(args.predict, label.item()))
label_dict = {
    0: '体育', 1: '娱乐', 2: '家居', 3: '房产', 4: '教育', 5: '时尚', 6: '时政', 7: '游戏', 8: '科技', 9: '财经'
}


def cnn_p(text):
    # path = ''
    # args = config.CNN()
    # cnn = model.CNN_Text(args)
    # cnn.load_state_dict(torch.load(path))
    # text_field, label_field = dataset.get_field()
    label = train.predict(predict.predict(text), cnn, text_field, label_field, args.cuda)
    return label_dict[label.item()]
