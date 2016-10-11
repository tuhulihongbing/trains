
import requests
import config
import json

class Api(object):
    def __init__(self):
        pass
    def api_suggest_train_name(self, keyword):
        url = config.url_qunar_suggest_name % keyword
        result = requests.get(url)
        res = result.json()
