#-*- coding:utf-8 -*-
import random

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Host': 'www.juzimi.com',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'
}

def random_character_headers_func():
    random_list = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
                   'Macintosh; Intel Mac OS X 10.10; rv:41.0',
                   'Mozilla/5.0 Gecko/20100101 Firefox/41.0',
                   "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0; Baiduspider-ads) Gecko/17.0 Firefox/17.0",
                   "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b4) Gecko/2008030317 Firefox/3.0b4",
                   "Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; BIDUBrowser 7.6)",
                   "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
                   "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
                   "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36",
                   "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko"
                   ]
    
    header_useragent = random_list[ random.randint(0,len(random_list) - 1) ]
    useragent_len = len(header_useragent) - 1
    user_agent = ''
    for item in xrange( random.randint(10,useragent_len) ):
        item_n = random.randint(0, useragent_len)
        user_agent += header_useragent[item_n]
    headers["User-Agent"] = user_agent
    return headers

def random_compose_headers_func():
    random_list = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
                   'Macintosh; Intel Mac OS X 10.10; rv:41.0',
                   'Mozilla/5.0 Gecko/20100101 Firefox/41.0'
                   ]
    dict_list = []
    nmax = 0
    for item in random_list:
        item_list = item.split(' ')
        dict_list += item_list
        nmax = nmax - 1 if len(item_list) < nmax else len(item_list) - 1
        
    dict_list = list(set(dict_list))
    n = random.randint(3, 10)
    headers["User-Agent"] = ' '.join(random.sample(dict_list,5)) 
    return headers