# -*- coding: utf-8 -*-
import requests

import telebot

from config import token, URL_SERVER
from contains import START_MESSAGE

bot = telebot.TeleBot(token)


def do_api(url, params):
    data = requests.get(URL_SERVER + url, params)
    return data.json()


def format_text_from_json(data):
    try:
        text = '<b>%s</b> %s' % (data[0]['title'], data[0]['description'])
    except:
        text = '<b> not </b> text'
    return text


@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id, START_MESSAGE)


@bot.message_handler(commands=['course'])
def command_get_course(message):
    course = do_api('/api/course/', {'username': message.chat.username})
    text_message = format_text_from_json(course)
    print text_message
    bot.send_message(message.chat.id, text_message, parse_mode='HTML')

if __name__ == '__main__':
    bot.polling(none_stop=True)
