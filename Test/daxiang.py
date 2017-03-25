# -*- coding:utf-8 -*-
import requests
import re
'''
北京市，天津市，上海市，重庆市，河北省，山西省，辽宁省，吉林省，黑龙江省，江苏省，浙江省，安徽省，福建省，江西省，山东省，河南省，湖北省，湖南省，广东省，海南省，四川省，贵州省，云南省，陕西省，甘肃省，青海省，台湾省，内蒙古自治区，广西壮族自治区，西藏自治区，宁夏回族自治区，新疆维吾尔自治区，香港特别行政区，澳门特别行政区。
'''
#res = requests.session()
#html = res.get(u'http://tvp.daxiangdaili.com/ip/?tid=556218827354330&num=2&operator=1&delay=5&sortby=time&foreign=only&filter=on')
#with open('daxiang.txt', 'w') as f:
    #f.write(html.text.encode('utf-8'))
#ips= html.content
#ips = ips.split('\r\n')
#print ips
#try:
    #html = ''''''
    #ip_compile = re.compile(r'(\d+\.\d+\.\d+\.\d+\:\d+)')  # 匹配IP
        ##         port_compile = re.compile(r'<td>(\d+)</td>')  # 匹配端口
    #ipl = re.findall(r'(\d+\.\d+\.\d+\.\d+\:\d+)', html)  # 获取所有IP
    
    #assert ipl
    #print ipl
#except AssertionError,ex:
    #print ex
#except Exception as ex:
    #print ex
#print html.status_code

class A(object):
    a = 1
    b = 2
    
    def fun1(self):
        print 'fun1'
        
    def fun2(self):
        print 'fun2'
        
a1 = A()
setattr( A, 'c', 1)
setattr( a1.__class__, 'c', 1)
a1.c = 3
print a1.c