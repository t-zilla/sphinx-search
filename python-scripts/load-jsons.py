import json
import pymysql
import time
import datetime

db = pymysql.connect(host='sphinx',port=9306,user='root',passwd='',charset='utf8',db='')
cur = db.cursor()

sql = "truncate rtindex doj"
cur.execute(sql)
row = cur.fetchall()
print(row)
db.commit()

with open('/datasets/doj.json') as json_file:
  data = json.load(json_file)
  for i, doc in enumerate(data):
    try:
      print(doc['id'])
      stamp = int(time.mktime(datetime.datetime.strptime(doc['date'][0:10], "%Y-%m-%d").timetuple()))
      print(stamp)
      doc['date'] = stamp
      sql = f"INSERT INTO doj (id, title, contents, j) VALUES (%s, %s, %s, %s)"
      val = (i, doc['title'], doc['contents'], json.dumps(doc))
      cur.execute(sql, val)
      db.commit()
    except Exception as e:
      print(e)

cur.close()
db.close()
