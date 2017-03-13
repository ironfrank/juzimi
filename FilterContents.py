#-*- coding:utf-8 -*-
from RequestsBox import *


class FilterContents:
    url = 'http://www.juzimi.com'
     
    @methodName
    def createDBID(self):
        timestamp = time.time()
        timestamp = '%f'%timestamp
        timestamp = ''.join(timestamp.split('.'))
        
        random_number = random.uniform(1000,9999)
        random_number = '%.6f'%random_number
        random_number = ''.join(random_number.split('.'))
        return timestamp + random_number
    
    @methodName
    def createMD5(self,src):
        md = hashlib.md5()
        md.update(src.encode('utf-8') )
        return md.hexdigest()
    
    @methodName
    def setUrl(self,url):
        self.url = url
    
    #提取主要分类，如：名人名言、书籍、电影、小说、散文、电视剧台词等类型的获取
    #返回list参数为：URL、type（类型如：writers）、类型名称（如：名人名言）
    @methodName
    def sortType(self,html):
        soup = BeautifulSoup(html.content)
        element_content = soup('div', id="navbar")[0].div.div.div
        #url\type\content
        return [(self.url + item['href'], item['href'].split('/')[-1], item.string) for item in element_content('a')]   
    
    #进入名人名言后，对按名人朝代（如：先秦、汉朝等）、按名人国家（如：美国、英国等）
    #返回list参数为：URL、背景信息（如：先秦、美国）
    @methodName
    def sortWritersBkgd(self,res,wr_url):
        witers_list = []
        while 1:
            html = res.proxyGet(wr_url)
            soup = BeautifulSoup(html.content)
            element_content = soup('div', id="block-block-20")[0]
            wrlist = element_content.findAll('div','wrlist')[0]('a') + element_content.findAll('div','wrlist')[1]('a')    
            witers_list += [(self.url + item['href'],item.string) for item in wrlist]
            
            exist_next = soup.findAll('a', rel="next")
            if exist_next:
                wr_url = self.url + exist_next[0]['href']
            else:
                break
        return witers_list
    
    #进入（除名人名言外）其它类型（如：散文、电影等）
    #返回list参数为：URL、出处名称
    @methodName
    def sortTarget(self,res,wr_url):
        witers_list = []
        while 1:
            html = res.proxyGet(wr_url)

            soup = BeautifulSoup(html.content)
            element_content = soup.findAll('span','xqallarticletilelinkspan')
            witers_list += [ (self.url + item.a['href'],item.a.string) for item in element_content]
            
            exist_next = soup.findAll('a', rel="next")
            if exist_next:
                wr_url = self.url + exist_next[0]['href']
            else:
                break
        return witers_list
    
    @methodName
    def sortWritersTarget(self,res,target_url):
        name_list = []
        
        while 1:
            html = res.proxyGet(target_url)
            #time.sleep(2)
            soup = BeautifulSoup(html.content)
            element_content = soup.findAll('div','views-field-name')
            #url/时代或者地区
            name_list += [ (self.url + item.a['href'],item.a.string) for item in element_content]
            
            exist_next = soup.findAll('a', rel="next")
            if exist_next:
                target_url = self.url + exist_next[0]['href']
            else:
                break
        return name_list
    
    @methodName
    def sortContents(self,res,url):
        content_list = []
        content_dict = {}
        item_writer = ''
        while 1:
            html = res.proxyGet(url)
            soup = BeautifulSoup(html.content)
            element_content = soup.findAll('div', "views-field-phpcode")
            
            for item in element_content:
                item_contents = item.findAll('a', {'class':'xlistju'} )[0].getText()
                item_writer = item.findAll('a', 'active')
                item_writer = item_writer[0].getText() if item_writer else ''
                
                nts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                content_list += [{
                    'id':self.createDBID(),
                    'contents':item_contents,
                    'contents_md5':self.createMD5(item_contents),
                    'origin':item_writer,
                    'origin_md5':self.createMD5(item_writer),
                    'create_time':nts
                }]
                
            print len(content_list)
            exist_next = soup.findAll('a', rel="next")
            if exist_next:
                url = self.url + exist_next[0]['href']
            else:
                content_dict['list'] = content_list
                soup = BeautifulSoup(html.content)
     
                element_content = soup.findAll('a',{'class':'wridescjiajie'})
                if element_content:
                    about_url = self.url + element_content[0]['href']
                    html = res.proxyGet(about_url)
                    soup = BeautifulSoup(html.content)
                    element_content = soup.findAll('div',{'class':'jianjiecontent'})
                    about = element_content[0].div.getText()
                    content_dict['about'] = [self.createDBID(),item_writer,about]
                else:
                    content_dict['about'] = ''
                break
        return content_dict