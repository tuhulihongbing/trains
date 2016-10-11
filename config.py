
sql = ("INSERT INTO bishe (title, uploadtime, img, url, pages, nav_ui, keywords, visits, huanhang,types)"
            "SELECT %s,%s,%s,%s,%s,%s,%s,%s,%s,%s" )
            # (item["title"], item["uploadtime"], item["img"], item["url"],
            #  item["pages"], item["nav_ui"], item["keywords"], item["visits"], item["huanhang"], item["types"])")

sql_select_raw_train_number = (" SELECT raw1 FROM raw_train_list ")

sql_insert_suggest_train_number = (" INSERT INTO suggest_train_list (raw1, suggest_name) "
                                   "SELECT '%s', '%s' ")
url_qunar_suggest_name = "http://touch.train.qunar.com/api/train/TrainNumSuggest?keyword=%s&q=&_n="

