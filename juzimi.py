# -*- coding:utf-8 -*-

# import chardet
# from selenium import webdriver
# browser=webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
from FilterContents import *
from DBOperation import *


# sys._getframe().f_code.co_name

# chardit1 = chardet.detect(html.text)
# print chardit1['encoding']

def main():
    url = "http://www.juzimi.com"

    res = RequestsBox()
    filterBox = FilterContents()
    db = juzimiDB()

    html = res.proxyGet(url)
    typeList = filterBox.sortType(html)

    for itemType in typeList:
        # 名人名言类型
        if itemType[1] == 'writers':
            witersBkgdList = filterBox.sortWritersBkgd(res, itemType[0])

            for itemBKGD in witersBkgdList:
                targetList = filterBox.sortWritersTarget(res, itemBKGD[0])

                for itemTarget in targetList:
                    contentDict = filterBox.sortContents(res, itemTarget[0])
                    sqlList = db.seiriSQL(itemType[1], contentDict)
                    db.insert(sqlList)

        # （除名人名言）小说、散文、电影等
        if itemType[1] == 'books' or itemType[1] == 'jingdiantaici' or itemType[1] == 'zhaichao' or\
            itemType[1] == 'sanwen' or itemType[1] == 'ongmantaici' or itemType[1] == 'lianxujutaici':
            if itemType[1] == 'lianxujutaici':
                targetList = filterBox.sortTarget(res, itemType[0])

                for itemTarget in targetList:
                    contentDict = filterBox.sortContents(res, itemTarget[0])
                    sqlList = db.seiriSQL(itemType[1], contentDict)
                    db.insert(sqlList)

if '__main__' == __name__:
    main()
