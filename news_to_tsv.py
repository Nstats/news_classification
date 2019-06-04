import pandas as pd
import os

'''
读取分散的N个新闻txt文件，去掉空格后合并成train.tsv & test.tsv文件，以作为bert的训练集和测试集。
'''

dir_ = './data/news'
num_news = 36

if not os.path.exists(dir_):
    os.mkdir(dir_)
tsv_train = os.path.join(dir_, 'train.tsv')
tsv_test = os.path.join(dir_, 'test.tsv')
target_dir = os.path.join(dir_, 'labels.txt')

test_list = [3, 5, 14, 26, 29, 35]
tsv_train = open(tsv_train, 'w')
tsv_test = open(tsv_test, 'w')
targets = open(target_dir, 'r')
target = targets.readlines()[0].split()  # ['1','1',...,'0']
for news_id in range(num_news):
    news_name = '新闻'+str(news_id+1)+'.txt'
    news_dir = os.path.join(dir_, news_name)
    with open(news_dir, 'r') as file:
        lines = file.readlines()
        a = ''
        for line in lines:
            a += line.strip()
        c = a.split()
        b = ''.join(c)
        if news_id+1 not in test_list:
            tsv_train.write(target[news_id]+'\t'+b+'\n')
        else:
            tsv_test.write(target[news_id]+'\t'+b+'\n')

tsv_train.close()
tsv_test.close()
targets.close()
