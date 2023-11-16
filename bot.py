import telebot
from telebot import types
from telebot.types import InlineKeyboardButton
from tensorflow import keras
import numpy as np
from tensorflow.keras.layers import Dense, Flatten
import csv
from heapq import nlargest


a = []
token = "6709862201:AAFoJucC34d5ltXa-xrQ-GAI0K0Kiiorge8"
bot = telebot.TeleBot(token)

alltegs = []
a = ''
testtegs = []
tegs = []
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Приветствуем тебя на ShareMeBot!")
    bot.send_message(message.from_user.id, "Отправь мне через запятую любые слова, а я в ответ вышлю 10 наиболее подходящих под них фото.")
    a = message.text
    tegs = list(a.split(','))

    for i in tegs:  #   проверка тегов на наличие в системе (обучалась ли нейронная сеть распознавать данный тег
        if i not in alltegs:
            bot.send_message(message.from_user.id, "Попробуйте использовать другие слова.")
            break
        else:
            testtegs.append(i)  #   добавляем проверенный тег в массив, который после полной проверки уйдет в нейросеть для определения нужного изображения

    model1 = keras.models.load_model('model1')  #   Файл с полученными данными обученной нейросети (имеется в файлах репозитория на GitHub)
    res = []

    empty = []

    for i in range(25963):
        empty.append(0)
    z = empty
    for j in testtegs:
        z[alltegs.index(j)] = 1
    res.append(z)
    res = model1.predict(np.array(res))
    res = nlargest(10, res)
    res = res[0]
    

    bot.send_message(message.from_user.id, "Вот топ-10 подходящих ссылок на фото:")

    for i in range(10):
        print(c[np.argmax(res[i:])])

bot.polling(none_stop=True, interval=0)
