# !/usr/bin/env python
# -*- coding:utf-8 -*-
from mysql import database_trains
import config
from api import Api
class trains(object):
    def __init__(self):
        self.trains_db = database_trains()
        self.api = Api()
        pass

    def get_one_suggest_train_number(self, raw1):
        pass

    def get_one_train_detail(self):
        pass

    def get_one_train_arrive_time(self):
        pass

    def get_suggest_train_numbers(self):
        sql = config.sql_select_raw_train_number
        result = self.trains_db.sql_exec(sql)
        for res in result:
            sugests = self.get_one_suggest_train_number(res[0])
        pass

    def get_train_details(self):
        pass

    def get_train_arrive_times(self):
        pass