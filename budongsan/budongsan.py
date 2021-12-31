# -*- coding: utf-8 -*-
import requests
import os
import telegram
import json
import sys
import mysql.connector

# telegram bot token
bot = telegram.Bot(token = '{token}')

# chat id for sending message
chat_id = '{chat_id}'

# current dir
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# declare variables
fileName = 'data/data.txt'
data = {}
tmpMsg = ''
msg = ''
orgSize = ''
config = {
   'user' : '{db_user}',
   'password' : '{db_password}',
   'host' : '{db_host}',
   'port' : '{db_port}',
   'database' : '{db_database}'
}
db = None

try:
  with open(os.path.join(BASE_DIR, 'data/size.txt'), 'r') as f_read:
    orgSize = f_read.readline()

  if int(orgSize) == int(os.path.getsize(BASE_DIR + '/' + fileName)):
    sys.exit()

  with open(os.path.join(BASE_DIR, fileName), 'r') as f_read:
    data = f_read.readline()
    f_read.close()

  data = json.loads(data)

  body = data['body']

  cnt = 0

  db = mysql.connector.connect(**config)
  cursor = db.cursor()

  if len(body) > 0:
    for l in body:
      sql = "select count(*) from budongsan where budongsanUid = " + l['atclNo']
      cursor.execute(sql)
      res = cursor.fetchone()

      if (res[0] == 0):
        tmpMsg += '====================\n'
        tmpMsg += '[' + l['rletTpNm'] + '] ' + l['atclNm'] + ' ' + l['bildNm']  + '\n'
        tmpMsg += str(round(l['spc1']/3.306))  + '평 / ' + l['direction'] + ' / ' + l['flrInfo'] + '\n'
        tmpMsg += l['tradTpNm'] + ' ' + l['hanPrc'] + '\n'
        tmpMsg += 'https://m.land.naver.com/article/info/' + l['atclNo'] + '\n'
        tmpMsg += '====================\n\n'
        cnt += 1

  db.close()

  #print(msg)

  if cnt > 0:
    msg += '총 ' + str(cnt) + '개의 전세 매물이 있습니다.\n\n'
    msg += tmpMsg

    #send message title & url
    bot.sendMessage(chat_id = chat_id, text = msg)

  with open(os.path.join(BASE_DIR, 'budongsan/size.txt'), 'w+') as f_write:
    fileSize = os.path.getsize(BASE_DIR + '/' + fileName)
    f_write.write(str(fileSize))
    f_write.close()

except Exception as e:
  print(e)
  msg = '문제가 발생했습니다.\n' + str(type(e))
  bot.sendMessage(chat_id = chat_id, text = msg)

finally:
  if (db != None):
    db.close()
