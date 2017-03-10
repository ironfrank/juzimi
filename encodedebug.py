#-*- coding:utf-8 -*-
import hashlib
import requests
import time
import random
import chardet
import itertools
from BeautifulSoup import BeautifulSoup
from selenium import webdriver

random_list = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
               'Macintosh; Intel Mac OS X 10.10; rv:41.0',
               'Mozilla/5.0 Gecko/20100101 Firefox/41.0'
               ]
dict_list = []
for item in random_list:
    dict_list += item.split(' ')
dict_list = list(set(dict_list))
slice=random.sample(dict_list,5)
print ' '.join(slice)

print random.choice("学习Python")
print random.choice(["JGood","is","a","handsome","boy"])
print random.choice(("Tuple","List","Dict"))

p=["Python","is","powerful","simple","andsoon..."]
random.shuffle(p)
print p

l=[1,2,3,4,5,6,7,8,9,10]
slice=random.sample(l,5)#从list中随机获取5个元素，作为一个片断返回
print slice

ids = [1,4,3,3,4,2,3,4,5,6,1]
ids.sort()
it = itertools.groupby(ids)
for k, g in it:
    print k

ids = [1,4,3,3,4,2,3,4,5,6,1]
news_ids = list(set(ids))
news_ids.sort(ids.index)