#-*- coding:utf-8 -*-
import random
import requests
import bs4, re
import functools


class StatusCodeException(Exception):
    pass

class RequestsBox(object): 
    useragent_list = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
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
    headers = {
        'User-Agent': '',
        'Host': 'www.juzimi.com',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive'
    }    
    response = None
    ip_list = []
    proxies = {'http':''}
    
    def outputfuncname(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print 'call %s():' % func.__name__
            return func(*args, **kw)
        return wrapper    
    
    @outputfuncname
    def __init__(self):
        self.response = requests.session()
        self.change_proxies()
    
    @outputfuncname
    def random_character_headers_func(self):       
        header_useragent = self.useragent_list[ random.randint(0,len(self.useragent_list) - 1) ]
        useragent_len = len(header_useragent) - 1
        user_agent = ''
        for item in xrange( random.randint(10,useragent_len) ):
            item_n = random.randint(0, useragent_len)
            user_agent += header_useragent[item_n]
        self.headers['User-Agent'] = user_agent
    
    @outputfuncname
    def change_headers(self):
        dict_list = []
        nmax = 0
        for item in self.useragent_list:
            item_list = item.split(' ')
            dict_list += item_list
            nmax = nmax - 1 if len(item_list) < nmax else len(item_list) - 1
            
        dict_list = list(set(dict_list))
        user_agent = ' '.join(random.sample(dict_list,5))
        self.headers['User-Agent'] = user_agent
        print self.headers
        
    @outputfuncname
    def change_proxies(self):
        self.clear_cookies()
        self.change_headers()
        #判断协议列表是否为空，如果为空，则获取新的代理
        if not self.ip_list:
            self.get_proxies_ip()
        elif self.proxies['http']:
            print 'Remove ip:',self.proxies['http']
            self.ip_list.remove(self.proxies['http'])
        
        self.proxies['http']= random.choice(self.ip_list)
        print self.proxies
    
    @outputfuncname
    def clear_cookies(self):
        self.response.cookies.clear()
    
    @outputfuncname
    def safe_get_fromproxies(self,url):
        while 1:
            try:
                print '****************************************************'
                print 'start requests.get:',url,self.proxies
                html = self.response.get(url, headers=self.headers, proxies=self.proxies, timeout=5)
                if html.status_code != 200:
                    raise StatusCodeException(html.status_code)
                #print html.content
                with open('juzimi.html','w') as f:
                    f.write(html.content)
                return html
            
            except StatusCodeException, ex:
                print 'Error Status Code:',ex
                self.change_proxies()
            except requests.exceptions.ReadTimeout, ex:
                print 'Proxies Connection Timeout!',ex
                self.change_proxies()                
            except requests.exceptions.ConnectionError,ex:
                print 'Proxies Connection Error!',ex
                self.change_proxies()
        #except AssertionError:
    
    @outputfuncname
    def get_proxies_ip(self):
        """获取代理IP"""
        url = "http://www.xicidaili.com/nn"
        headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
                    "Accept-Encoding":"gzip, deflate, sdch",
                    "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
                    "Referer":"http://www.xicidaili.com",
                    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
                    }
        res = requests.get(url,headers=headers)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        data = soup.table.find_all("td")
        ip_compile= re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')    # 匹配IP
        port_compile = re.compile(r'<td>(\d+)</td>')                # 匹配端口
        ip = re.findall(ip_compile,str(data))       # 获取所有IP
        port = re.findall(port_compile,str(data))   # 获取所有端口
        self.ip_list = [":".join(i) for i in zip(ip,port)]  # 组合IP+端口，如：115.112.88.23:8080 
      