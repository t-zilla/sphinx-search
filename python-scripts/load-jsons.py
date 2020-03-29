import json
import pymysql
import time
import datetime

db = pymysql.connect(host='sphinx', port=9306, user='root', passwd='', charset='utf8', db='')
cur = db.cursor()

sql = "TRUNCATE RTINDEX plwiki"
cur.execute(sql)
row = cur.fetchall()
print(row)
db.commit()

with open('/datasets/plwiki.json') as json_file:
  buffer = ''
  count = 0
  for line in json_file:
    if count == 0:
      count += 1
      continue
    buffer += line
    count += 1
    if (count-1) % 8 == 0:
      try:
        buffer = buffer.strip()[:-1]
        doc = json.loads(buffer)
        print(doc['id'])
        stamp = int(time.mktime(datetime.datetime.strptime(doc['datetime'], "%Y-%m-%dT%H:%M:%SZ").timetuple()))
        doc['datetime'] = stamp
        sql = f"INSERT INTO plwiki (id, title, text, j) VALUES (%s, %s, %s, %s)"
        val = (doc['id'], doc['title'], doc['text'], json.dumps(doc))
        cur.execute(sql, val)
        db.commit()
      except Exception as e:
        print(e)
      buffer = ''

cur.close()
db.close()
