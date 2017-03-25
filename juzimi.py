# -*- coding:utf-8 -*-
from ExtractBox import *
from juzimidb import *


def UpdateDB():
    res = RequestsBox()#
    db = JuzimiDB()
    exbox = ExtractWebFrame()

    # db.seiriTypeTableSQL(exbox.sortType())
    # db.executeSQL()

    records = db.queryJuzimiTable()
    for sType, name, url in records:
        if name == '经典语录' or name == '名人名言' or name == '热门名人':
            if name == '名人名言':
                db.seiriWritersMapTableSQL(exbox.sortWritersBkgd(url))
                db.executeSQL()

                rows = db.queryWritersMapTable()
                for sType, bkgd, url in rows:
                    db.seiriWritersTableSQL(exbox.sortWritersTarget(sType,  bkgd, url))
                    db.executeSQL()
        else:# 提取（除名人名言外）其它类型（如：散文、电影等）作品列表
            db.seiriTargetTableSQL(sType, exbox.sortTarget(url))
            db.executeSQL()

    for sType, name, url in records:
        if name == '经典语录' or name == '名人名言' or name == '热门名人':
            pass
        else:
            table_names = db.queryTargetTable(sType)
            for item_name, item_url in table_names:
                db.seiriContentsTableSQL(sType, item_name, exbox.sortContents(item_url))
                db.executeSQL()


def main():
    UpdateDB()


if '__main__' == __name__:
    main()
