#-*- coding:utf-8 -*-
import psycopg2
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class JuzimiDB(object):
    dbconn = None
    dbcur = None
    sqlQueue = []

    def __init__(self):
        # type: () -> object
        self.dbconn = psycopg2.connect(
            database="juzimi_db", user="frank", password="root", host="127.0.0.1", port="5432")
        self.dbcur = self.dbconn.cursor()

    def __del__(self):
        self.dbcur.close()
        self.dbconn.close()

    # def create_table(self,cursql):
    #     self.dbcur.execute(cursql)

    def executeSQL(self):
        while self.sqlQueue:
            sqlstr = self.sqlQueue.pop()
            print sqlstr
            self.dbcur.execute(sqlstr[0], sqlstr[1])
        self.dbconn.commit()

    def IsRecExist(self, cursql):
        pass

    def Uniquerows(self):
        pass

    def seiriTypeTableSQL(self, param):
        self.dbcur.execute(
            '''
            create table if not exists juzimi(
              "id" VARCHAR(32) NOT NULL PRIMARY KEY,
              "type" VARCHAR(32),
              "name" VARCHAR(64),
              "url"  TEXT,
              "md5"  VARCHAR(128),
              "state" VARCHAR(32),
              "create_time" TIMESTAMP,
              "update_time" TIMESTAMP
            )
            '''
        )
        self.dbconn.commit()

        fields = ['id', 'type', 'name', 'url', 'md5',
                  'state', 'create_time', 'update_time']

        sqlstr = 'INSERT INTO juzimi('
        sqlstr += ', '.join([item for item in fields])
        sqlstr += ')VALUES('
        sqlstr += ', '.join(['%s' for i in fields])
        sqlstr += ')'

        self.sqlQueue = [
            (sqlstr, (item['id'],
                      item['type'],
                      item['name'],
                      item['url'],
                      item['md5'],
                      item['state'],
                      item['create_time'],
                      item['update_time'])) for item in param]

    def seiriTargetTableSQL(self, tbName, param):
        print tbName
        print param
        sqlstr = 'create table if not exists '
        sqlstr += tbName
        sqlstr += '''("id" VARCHAR(32) NOT NULL PRIMARY KEY,
                      "name" VARCHAR(64),
                      "url"  TEXT,
                      "md5"  VARCHAR(128),
                      "state" VARCHAR(32),
                      "create_time" TIMESTAMP,
                      "update_time" TIMESTAMP
                     )
                     '''

        self.dbcur.execute(sqlstr)
        fields = ['id', 'name', 'url', 'md5',
                  'state', 'create_time', 'update_time']

        sqlstr = 'INSERT INTO %s(' % (tbName)
        sqlstr += ', '.join([item for item in fields])
        sqlstr += ')VALUES('
        sqlstr += ', '.join(['%s' for i in fields])
        sqlstr += ')'
        # fields_tuple = tuple()
        # for item in param:
        #     fields_tuple += tuple([val for val in item])

        self.sqlQueue = [
            (sqlstr, (item['id'],
                      item['name'],
                      item['url'],
                      item['md5'],
                      item['state'],
                      item['create_time'],
                      item['update_time'])) for item in param]

    def seiriWritersMapTableSQL(self, param):
        self.dbcur.execute(
            '''
            create table if not exists writers_map(
              "id" VARCHAR(32) NOT NULL PRIMARY KEY,
              "bkgd" VARCHAR(64),
              "url"  TEXT,
              "md5"  VARCHAR(128),
              "state" VARCHAR(32),
              "create_time" TIMESTAMP,
              "update_time" TIMESTAMP
            )
            '''
        )
        self.dbconn.commit()

        fields = ['id', 'bkgd', 'url', 'md5',
                  'state', 'create_time', 'update_time']

        sqlstr = 'INSERT INTO writers_map('
        sqlstr += ', '.join([item for item in fields])
        sqlstr += ')VALUES('
        sqlstr += ', '.join(['%s' for i in fields])
        sqlstr += ')'

        self.sqlQueue = [
            (sqlstr, (item['id'],
                      item['bkgd'],
                      item['url'],
                      item['md5'],
                      item['state'],
                      item['create_time'],
                      item['update_time'])) for item in param]

    def seiriWritersTableSQL(self, param):
        self.dbcur.execute(
            '''
            create table if not exists writers(
              "id" VARCHAR(32) NOT NULL PRIMARY KEY,
              "type" VARCHAR(32),
              "name" VARCHAR(64),
              "bkgd" VARCHAR(64),
              "url"  TEXT,
              "md5"  VARCHAR(128),
              "state" VARCHAR(32),
              "create_time" TIMESTAMP,
              "update_time" TIMESTAMP
            )
            '''
        )
        self.dbconn.commit()

        fields = ['id', 'type', 'name', 'bkgd', 'url',
                  'md5', 'state', 'create_time', 'update_time']

        sqlstr = 'INSERT INTO writers('
        sqlstr += ', '.join([item for item in fields])
        sqlstr += ')VALUES('
        sqlstr += ', '.join(['%s' for i in fields])
        sqlstr += ')'

        self.sqlQueue = [
            (sqlstr, (item['id'],
                      item['type'],
                      item['name'],
                      item['bkgd'],
                      item['url'],
                      item['md5'],
                      item['state'],
                      item['create_time'],
                      item['update_time'])) for item in param]

    def seiriContentsTableSQL(self, sType, name, param):
        self.dbcur.execute(
            '''
            create table if not exists juzimi_contents(
              "id" VARCHAR(32) NOT NULL PRIMARY KEY,
              "origin" VARCHAR(64),
              "type" VARCHAR(32),
              "content" TEXT,
              "content_md5"  VARCHAR(128),
              "state" VARCHAR(32),
              "create_time" TIMESTAMP,
              "update_time" TIMESTAMP
            )
            '''
        )
        self.dbconn.commit()

        fields = ['id', 'origin', 'type', 'content',
                  'content_md5', 'state', 'create_time', 'update_time']

        sqlstr = 'INSERT INTO juzimi_contents('
        sqlstr += ', '.join([item for item in fields])
        sqlstr += ')VALUES('
        sqlstr += ', '.join(['%s' for i in fields])
        sqlstr += ')'

        self.sqlQueue = []
        for item in param:
            if not item['origin']:
                item['state'] = 'Null'
            elif item['origin'] != name:
                item['state'] = 'Problem'
            item['type'] = sType
            self.sqlQueue.append(
                (sqlstr, (item['id'],
                          item['origin'],
                          item['type'],
                          item['content'],
                          item['content_md5'],
                          item['state'],
                          item['create_time'],
                          item['update_time'])
                 )
            )

        # self.sqlQueue = [
        #     (sqlstr, (item['id'],
        #               item['origin'],
        #               item['type'],
        #               item['content'],
        #               item['content_md5'],
        #               item['state'],
        #               item['create_time'],
        #               item['update_time'])) for item in param]

    def queryJuzimiTable(self):
        self.dbcur.execute("SELECT type, name, url FROM juzimi;")
        rows = self.dbcur.fetchall()  # all rows in table
        return rows

    def queryWritersMapTable(self):
        self.dbcur.execute("SELECT type, bkgd, url FROM writers_map;")
        rows = self.dbcur.fetchall()  # all rows in table
        return rows

    def queryTargetTable(self, param):
        self.dbcur.execute("SELECT name, url FROM %s;" % (param))
        rows = self.dbcur.fetchall()  # all rows in table
        return rows
