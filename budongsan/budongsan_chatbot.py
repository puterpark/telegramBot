# -*- coding: utf-8 -*-
import telegram
import sys
import mysql.connector
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

# telegram bot token
bot = telegram.Bot(token = '{token}')

# chat id for sending message
chat_id = '{chat_id}'

# declare variables
config = {
   'user' : '{db_user}',
   'password' : '{db_password}',
   'host' : '{db_host}',
   'port' : '{db_port}',
   'database' : '{db_database}'
}

db = None

def rm(update, context):
  atclNo = context.args[0]

  try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    sql = 'insert into budongsan (budongsanUid) values (' + atclNo + ')'
    cursor.execute(sql)
    db.commit()

    if cursor.rowcount > 0:
      bot.sendMessage(chat_id = update.message.chat_id, text = '매물번호[' + atclNo + ']는 예외처리되었습니다.')
  
  except Exception as e:
    print(e)
    msg = 'DB 작업 중 문제가 발생했습니다.\n' + str(type(e))
    bot.sendMessage(char_id = chat_id, text = msg)

  finally:
    if (db != None):
      db.close()

try:
  updater = Updater(token = '{token}', use_context = True)

  updater.dispatcher.add_handler(CommandHandler('rm', rm))

  updater.start_polling()
  updater.idle()

except Exception as e:
  print(e)
  msg = '문제가 발생했습니다.\n' + str(type(e))
  bot.sendMessage(chat_id = chat_id, text = msg)

finally:
  if (db != None):
    db.close()
