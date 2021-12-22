# -*- coding: utf-8 -*-
import telegram

# telegram bot token
bot = telegram.Bot(token = '{token}')

# chat id for sending message
chat_id = '{chat_id}'

# send message
bot.sendMessage(chat_id = chat_id, text = 'LIST in the SPAMHAUS RBL!!!')
