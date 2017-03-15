# -*- coding:utf-8 -*-
from BeautifulSoup import BeautifulSoup
from FuncBox import *


class RequestsBox(object):
    useragent_browser_list = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
                      'Macintosh; Intel Mac OS X 10.10; rv:41.0',
                      'Mozilla/5.0 Gecko/20100101 Firefox/41.0',
                      "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0; Baiduspider-ads) Gecko/17.0 Firefox/17.0",
                      "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b4) Gecko/2008030317 Firefox/3.0b4",
                      "Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; BIDUBrowser 7.6)",
                      "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
                      "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
                      "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36",
                      "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko",
                      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                      'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
                      'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko',
                      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
                      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
                      'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
                      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
                      'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
                      'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
                      'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
                      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
                      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
                      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
                      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
                      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
                      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
                      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
                      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)'
                      ]
    useragent_sprider_list = [
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "Baiduspider+(+http://www.baidu.com/search/spider.htm)",
        "Mozilla/5.0 (compatible; Yahoo! Slurp China; http://misc.yahoo.com.cn/help.html)",
        "Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )",
        "Sosospider+(+http://help.soso.com/webspider.htm)",
        "Sogou Web Sprider(compatible; Mozilla 4.0; MSIE 6.0; Windows NT 5.1; SV1; Avant Browser; InfoPath.1; .NET CLR 2.0.50727; .NET CLR1.1.4322)"
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
    proxies = {'http': ''}

    @methodName
    def __init__(self):
        self.response = requests.session()
        self.changeProxy()

    def __del__(self):
        self.response.close()

    @methodName
    def random_character_headers_func(self):
        header_useragent = self.useragent_list[random.randint(0, len(self.useragent_list) - 1)]
        useragent_len = len(header_useragent) - 1
        user_agent = ''
        for item in xrange(random.randint(10, useragent_len)):
            item_n = random.randint(0, useragent_len)
            user_agent += header_useragent[item_n]
        self.headers['User-Agent'] = user_agent

    @methodName
    def changeRandomHeaders(self):
        dict_list = []
        nmax = 0
        for item in self.useragent_browser_list:
            item_list = item.split(' ')
            dict_list += item_list
            nmax = nmax - 1 if len(item_list) < nmax else len(item_list) - 1

        dict_list = list(set(dict_list))
        user_agent = ' '.join(random.sample(dict_list, 5))
        self.headers['User-Agent'] = user_agent

    @methodName
    def changeBrowserHeaders(self):
        self.headers['User-Agent'] = random.choice(self.useragent_browser_list)

    @methodName
    def changeSpriderHeaders(self):
        self.headers['User-Agent'] = random.choice(self.useragent_sprider_list)

    @methodName
    def changeHeaders(self):
        # self.changeSpriderHeaders()
        # self.changeBrowserHeaders()
        self.changeRandomHeaders()

    @methodName
    def changeProxy(self):
        self.clearCookies()
        #变换Headers中user-agent的标示
        self.changeHeaders()
        # 判断协议列表是否为空，如果为空，则获取新的代理
        if len(self.ip_list) < 2:
            self.getDaxiangProxiesIP()
        elif self.proxies['http']:
            print 'Remove ip:', self.proxies['http']
            self.ip_list.remove(self.proxies['http'])

        self.proxies['http'] = random.choice(self.ip_list)

    @methodName
    def clearCookies(self):
        self.response.cookies.clear()

    @methodName
    def proxyGet(self, url):
        while 1:
            try:
                print '==============================================================================='
                print '********************* Start get url and proxies *******************************'
                print url, self.proxies
                print self.headers
                html = self.response.get(url,
                                         headers=self.headers,
                                         proxies=self.proxies,
                                         #timeout=30,
                                         allow_redirects=False)

                print '==============================================================================='
                if html.status_code == 200 and html.content:
                    with open('juzimi.html', 'w') as f:
                        f.write(html.content)

                    return html
                else:
                    raise StatusCodeException((html.status_code, html.content))

            except StatusCodeException, ex:
                print 'Error Status Code:', ex
                self.changeProxy()
            except requests.exceptions.ReadTimeout, ex:
                print 'Proxies Connection Timeout!', ex
                self.changeProxy()
            except requests.exceptions.ConnectionError, ex:
                print 'Proxies Connection Error!', ex
                self.changeProxy()
            except requests.exceptions.ChunkedEncodingError, ex:
                print 'Proxies Connection Error!', ex
                self.changeProxy()
            except requests.exceptions.TooManyRedirects, ex:
                print 'Proxies Connection Error!', ex
                self.changeProxy()
                # except AssertionError:

    @methodName
    def getDaxiangProxiesIP(self):
        time.sleep(1.5)
        try:
            ipUrl = ''
            with open('proxies.conf','r') as f:
                ipUrl += f.read()
            if not ipUrl:
                raise Exception('proxies.conf配置文件有误！')
            html = requests.get(ipUrl)
            ips = re.findall(r'(\d+\.\d+\.\d+\.\d+\:\d+)', html.content)
            #assert ips
            if not ips:
                raise Exception('获取代理IP 失败！')
            self.ip_list = ips
        except Exception as ex:
            print ex
            self.getDaxiangProxiesIP()
            time.sleep(10)

    @methodName
    def getFreeProxiesIP(self):
        try:
            """获取代理IP"""
            headers = {"Accept": "text/html,application/xhtml+xml,application/xml;",
                       "Accept-Encoding": "gzip, deflate, sdch",
                       "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
                       "Referer": "http://www.xicidaili.com",
                       "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) Chrome/42.0.2311.90 Safari/537.36"
                       }
            html = requests.get("http://www.xicidaili.com/nn", headers=headers)
            print html.status_code
            time.sleep(5)
            soup = BeautifulSoup(html.content)
            with open('html.html', 'w') as f:
                f.write(html.content)
            data = soup.table.findAll("td")
            ip_compile = re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')  # 匹配IP
            port_compile = re.compile(r'<td>(\d+)</td>')  # 匹配端口
            ip = re.findall(ip_compile, str(data))  # 获取所有IP
            port = re.findall(port_compile, str(data))  # 获取所有端口
            self.ip_list = [":".join(i) for i in zip(ip, port)]  # 组合IP+端口，如：115.112.88.23:8080
        except Exception as ex:
            print ex
            time.sleep(5)
            self.getProxiesIP()
