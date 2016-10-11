
import requests
import config
import json

class Api(object):
    def __init__(self):
        pass
    def api_suggest_train_name(self, keyword):
        url = config.url_qunar_suggest_name % keyword
        result = requests.get(url)
        suggest_list = []
        if result.status_code == 200:
            res = result.json()
            try:
                suggest_list = res["dataMap"]["result"]
            except Exception,e:
                print e.message
        else:
            print "The Result Code is " % result.status_code
        return suggest_list


