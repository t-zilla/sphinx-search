import json
import pymysql
import time
import datetime

db = pymysql.connect(host='sphinx',port=9306,user='root',passwd='',charset='utf8',db='')
cur = db.cursor()

#start_time = time.time()

for _ in range(1, 10):
    sql = "SELECT j.id, j.components, j.title, IN(j.components, 'Antitrust Division') AS ad, weight() FROM doj WHERE MATCH('toyota') AND ad = 1;"
    cur.execute(sql)
    row = cur.fetchall()

# print("--- %s seconds ---" % (time.time() - start_time))