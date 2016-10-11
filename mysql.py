# -*- coding: utf-8 -*-

import MySQLdb
class database_trains(object):
    def __init__(self):
        self.db = MySQLdb.connect(host='XXXX',
                         db='XXXX',
                         user='XXXX',
                         passwd='XXXX')        # name of the data base
        # you must create a Cursor object. It will let
        #  you execute all the queries you need
    def sql_exec(self,sql):
        self.__init__()
        # Use all the SQL you like
        cur = self.db.cursor()
        cur.execute(sql)
        # "insert into raw_train_list (raw1) select 'test1'"
        # print all the first cell of all the rows
        result = cur.fetchall()
        self.db.commit()
        cur.close()
        self.db.close()
        return result


