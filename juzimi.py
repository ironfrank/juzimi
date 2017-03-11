#-*- coding:utf-8 -*-
import requests
import chardet
from BeautifulSoup import BeautifulSoup
#from selenium import webdriver

from SafeRequests import *
from funcbox import *
#sys._getframe().f_code.co_name
url = "http://www.juzimi.com"


def outputfuncname(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@outputfuncname
def web_classify_catalogue(res,html):
    soup = BeautifulSoup(html.content)
    element_content = soup('div', id="navbar")[0].div.div.div
    return [(url + item['href'], item['href'].split('/')[-1], item.string) for item in element_content('a')]   

@outputfuncname
def writers_catalogue(res,wr_url,url):
    witers_list = []
    while 1:
        html = res.safe_get_fromproxies(wr_url)
        #time.sleep(2)
        #print html.status_code,html.content
        soup = BeautifulSoup(html.content)
        element_content = soup('div', id="block-block-20")[0]
        wrlist = element_content.findAll('div','wrlist')[0]('a') + element_content.findAll('div','wrlist')[1]('a')    
        witers_list += [(url + item['href'],item.string) for item in wrlist]
        
        exist_next = soup.findAll('a', rel="next")
        if exist_next:
            wr_url = url + exist_next[0]['href']
        else:
            break
    return witers_list

@outputfuncname
def others_target_catalogue(res,wr_url,url):
    witers_list = []
    while 1:
        html = res.safe_get_fromproxies(wr_url)
        #time.sleep(2)
        soup = BeautifulSoup(html.content)
        element_content = soup.findAll('span','xqallarticletilelinkspan')
        witers_list += [ (url + item.a['href'],item.a.string) for item in element_content]
        
        exist_next = soup.findAll('a', rel="next")
        if exist_next:
            wr_url = url + exist_next[0]['href']
        else:
            break
    return witers_list

@outputfuncname
def writers_target_catalogue(res,target_url,url):
    name_list = []
    
    while 1:
        html = res.safe_get_fromproxies(target_url)
        #time.sleep(2)
        soup = BeautifulSoup(html.content)
        element_content = soup.findAll('div','views-field-name')
        name_list += [ (url + item.a['href'],item.a.string) for item in element_content]
        
        exist_next = soup.findAll('a', rel="next")
        if exist_next:
            target_url = url + exist_next[0]['href']
        else:
            break
    return name_list

@outputfuncname
def content_box(res,content_url,url):
    content_list = []
    content_dict = {}
    item_writer = ''
    while 1:
        html = res.safe_get_fromproxies(content_url)
        soup = BeautifulSoup(html.content)
        element_content = soup.findAll('div', "views-field-phpcode")
        
        for item in element_content:
            item_contents = item.findAll('a', {'class':'xlistju'} )[0].getText()
            item_writer = item.findAll('a', 'active')
            item_writer = item_writer[0].getText() if item_writer else ''
            
            content_list += [{'id':create_id(),'contents':item_contents,'contents_md5':create_md5(item_contents.encode('utf-8')),'origin':item_writer}]
            print len(content_list)
        exist_next = soup.findAll('a', rel="next")
        if exist_next:
            content_url = url + exist_next[0]['href']
            #time.sleep(2)
        else:
            content_dict['list'] = content_list
            soup = BeautifulSoup(html.content)
            #element_content = soup.findAll('div', "views-field-phpcode")
            element_content = soup.findAll('a',{'class':'wridescjiajie'})
            if element_content:
                about_url = url + element_content[0]['href']
                html = res.safe_get_fromproxies(about_url)
                soup = BeautifulSoup(html.content)
                element_content = soup.findAll('div',{'class':'jianjiecontent'})
                about = element_content[0].div.getText()
                content_dict['about'] = [create_id(),item_writer,about]
            break
    return content_list
    
#browser=webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')

@outputfuncname
def main():
    res = RequestsBox()
    html = res.safe_get_fromproxies(url)
    #chardit1 = chardet.detect(html.text)
    #print chardit1['encoding']

    web_classify_list = web_classify_catalogue(res, html)
    
    for classify_url in web_classify_list:
        #判断是否为：名人名言或者其它类型
        #当前为名人名言
        if classify_url[1] == 'writers':
            print classify_url[0] 
            witers_list = writers_catalogue(res, classify_url[0],url)
    
            for target_url in witers_list:
                name_list = writers_target_catalogue(res, target_url[0], url)
    
                for content_url in name_list:
                    _ = content_box(res, content_url[0], url)
                
        if classify_url[1] == 'books' or classify_url[1] == 'jingdiantaici' or classify_url[1] == 'zhaichao' or\
           classify_url[1] == 'sanwen' or classify_url[1] == 'ongmantaici' or classify_url[1] == 'lianxujutaici': 
            if classify_url[1] == 'lianxujutaici':
                name_list = others_target_catalogue(res, classify_url[0],url)
                    
                for content_url in name_list:
                    _ = content_box(res, content_url[0], url)
if '__main__' == __name__:
    main()