# -*- coding: utf-8 -*-
import requests

import telebot
from telebot import types

from config import token, URL_SERVER
from contains import START_MESSAGE

bot = telebot.TeleBot(token)


def do_api(url, params):
    data = requests.get(URL_SERVER + url, params)
    return data.json()


def format_text_from_json(data):
    try:
        text = '<b>%s</b> \n %s' % (data[0]['title'], data[0]['description'])
    except:
        text = '<b> not </b> text'
    return text


@bot.message_handler(commands=['start'])
def command_start(message):
    print message
    markup = types.ReplyKeyboardMarkup()
    markup.row('Курсы')
    markup.row('Мои курсы')
    print markup.row_width
    bot.send_message(message.chat.id, START_MESSAGE, reply_markup='/course')


@bot.message_handler(commands=['course'])
def command_get_course(message):
    course = do_api('/api/course/', {'username': message.chat.username})
    text_message = format_text_from_json(course)

    bot.send_message(message.chat.id, text_message, parse_mode='HTML')

if __name__ == '__main__':
    bot.polling(none_stop=True)
