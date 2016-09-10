# -*- coding: utf-8 -*-
import config
import telebot

from contains import START_MESSAGE

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id, START_MESSAGE)

@bot.message_handler(commands=['course'])
def command_get_course(message):
    course = None
    bot.send_message(message.chat.id, course)

if __name__ == '__main__':
    bot.polling(none_stop=True)
