#-*- coding:utf-8 -*-
import psycopg2
import sys

reload(sys)   
sys.setdefaultencoding('utf8')

class juzimiDB(object):
    dbconn = None
    dbcur = None
    def __init__(self):
        # type: () -> object
        self.dbconn = psycopg2.connect(database="juzimi_db", user="frank", password="root", host="127.0.0.1", port="5432")
        self.dbcur = self.dbconn.cursor()
    
    def __del__(self):
        self.dbcur.close()
        self.dbconn.close()
    
    def insert(self,dbsql):
        for sqlitem in dbsql:
            #print sqlitem[0],sqlitem[1]
            self.dbcur.execute(sqlitem[0],sqlitem[1])
        self.dbconn.commit()
    
    def update(self,dbsql):
        pass
    
    def seiriSQL(self,classify,contentDict):
        about = contentDict['about']
        contentList = contentDict['list']
        sqlList = []
        for item in contentList:
 
            sqlstr = 'INSERT INTO juzimi(id, contents, contents_md5, origin, origin_md5, create_time)VALUES(%s,%s,%s,%s,%s,%s)'
            sqlval = (
                item['id'],
                item['contents'],
                item['contents_md5'],
                #about,
                item['origin'],
                item['origin_md5'],
                #item['writers'],
                item['create_time']
            )
            sqltuple = (sqlstr, sqlval)
            sqlList.append(sqltuple)
        return sqlList
