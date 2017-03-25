# -*- coding:utf-8 -*-
from BeautifulSoup import BeautifulSoup
from RequestsBox import *
#from PhantomjsBox import *


class ExtractWebFrame:
    url = 'http://www.juzimi.com'
    resBox = None

    def __init__(self):
        self.resBox = RequestsBox()

    @methodName
    def createDBID(self):
        timestamp = time.time()
        timestamp = '%f' % timestamp
        timestamp = ''.join(timestamp.split('.'))

        random_number = random.uniform(1000, 9999)
        random_number = '%.6f' % random_number
        random_number = ''.join(random_number.split('.'))
        return timestamp + random_number

    @methodName
    def createMD5(self, src):
        md = hashlib.md5()
        md.update(src.encode('utf-8'))
        return md.hexdigest()

    @methodName
    def setUrl(self, url):
        self.url = url

    @methodName
    def now_time(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # 提取主要分类，如：名人名言、书籍、电影、小说、散文、电视剧台词等类型的获取
    # 返回list参数为：URL、type（类型如：writers）、类型名称（如：名人名言）
    @methodName
    def sortType(self):
        html = self.resBox.proxyGet(self.url)

        soup = BeautifulSoup(html.content)
        element_content = soup('div', id="navbar")[0].div.div.div
        # id/type/type's name/url/type's md5/state/create_time/update_time

        return [
            {'url': self.url + item['href'],
             'type': item['href'].split('/')[-1],
             'name': item.string,
             'md5': self.createMD5(item.string),
             'id': self.createDBID(),
             'create_time': self.now_time(),
             'update_time': self.now_time(),
             'state': 'updated'
             } for item in element_content('a')
        ]
        # return [(self.url + item['href'], item['href'].split('/')[-1],
        # item.string) for item in element_content('a')]

    # 进入名人名言后，对按名人朝代（如：先秦、汉朝等）、按名人国家（如：美国、英国等）
    # 返回list参数为：URL、背景信息（如：先秦、美国）
    @methodName
    def sortWritersBkgd(self, url):
        bkgbList = []
        while 1:
            html = self.resBox.proxyGet(url)

            soup = BeautifulSoup(html.content)
            element_content = soup('div', id="block-block-20")[0]
            wrlist = element_content.findAll('div', 'wrlist')[0](
                'a') + element_content.findAll('div', 'wrlist')[1]('a')

            bkgbList += [{'url': self.url + item['href'],
                          'bkgd': item.string,
                          'md5': self.createMD5(item.string),
                          'id': self.createDBID(),
                          'create_time': self.now_time(),
                          'update_time': self.now_time(),
                          'state': 'updated'
                          } for item in wrlist]

            exist_next = soup.findAll('a', rel="next")
            if exist_next:
                url = self.url + exist_next[0]['href']
            else:
                break
        return bkgbList

    @methodName
    def sortWritersTarget(self, typestr, pkgd, url):
        targetList = []

        while 1:
            html = self.resBox.proxyGet(url)

            soup = BeautifulSoup(html.content)
            element_content = soup.findAll('div', 'views-field-name')
            # url/时代或者地区
            targetList += [{'url': self.url + item.a['href'],
                            'name': item.a.string,
                            'type': typestr,
                            'bkgd': pkgd,
                            'md5': self.createMD5(item.a.string),
                            'id': self.createDBID(),
                            'create_time': self.now_time(),
                            'update_time': self.now_time(),
                            'state': 'updated'
                            } for item in element_content]

            #targetList += [(self.url + item.a['href'], item.a.string) for item in element_content]

            exist_next = soup.findAll('a', rel="next")
            if exist_next:
                url = self.url + exist_next[0]['href']
            else:
                break
        return targetList

    # 进入（除名人名言外）其它类型（如：散文、电影等）
    # 返回list参数为：URL、出处名称
    @methodName
    def sortTarget(self, url):
        targetList = []
        while 1:
            html = self.resBox.proxyGet(url)

            soup = BeautifulSoup(html.content)
            element_content = soup.findAll('span', 'xqallarticletilelinkspan')

            targetList += [{'url': self.url + item.a['href'],
                            'name': item.a.string,
                            'md5': self.createMD5(item.a.string),
                            'id': self.createDBID(),
                            'create_time': self.now_time(),
                            'update_time': self.now_time(),
                            'state': 'updated'
                            } for item in element_content]

            exist_next = soup.findAll('a', rel="next")
            if exist_next:
                url = self.url + exist_next[0]['href']
            else:
                break
        return targetList

    @methodName
    def sortContents(self, url):
        contentList = []
        while 1:
            html = self.resBox.proxyGet(url)

            soup = BeautifulSoup(html.content)
            element_content = soup.findAll('div', "views-field-phpcode")

            for item in element_content:
                item_contents = item.findAll(
                    'a', {'class': 'xlistju'})[0].getText()
                item_origin = item.findAll('a', 'active')
                item_origin = item_origin[0].getText() if item_origin else ''

                contentList += [{
                    'id': self.createDBID(),
                    'content': item_contents,
                    'content_md5': self.createMD5(item_contents),
                    'origin': item_origin,
                    'create_time': self.now_time(),
                    'update_time': self.now_time(),
                    'state': 'updated'
                }]

            print len(contentList)
            exist_next = soup.findAll('a', rel="next")
            if exist_next:
                url = self.url + exist_next[0]['href']
            else:
                break

        return contentList
