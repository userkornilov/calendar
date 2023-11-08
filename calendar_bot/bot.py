from mimetypes import types_map
from wsgiref import types
import telebot
import config
import random

bot = telebot.TeleBot(config.TOKEN)

def teext():
    with open("text.txt", "r") as file:
        file.readlines()

@bot.message_handler(content_types=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Сгенерировать поздравление")
    
    markup.add(item1)
    bot.send_message(message.chat.id, "Вас приветствует CalndarBot, {0.first_name}".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def resp(message):
    if message.chat.type == 'private':
        if message.text == 'Сгенерировать поздравление':
            bot.send_message(message.chat.id, random.choice(teext()))
        else:
            bot.send_message(message.chat.id, 'Не знаю что ответить:/')
                         

#RUN
bot.polling(none_stop=True)