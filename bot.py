import telebot
from telebot import types
from telebot.types import InlineKeyboardButton

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

    #   здесь располагается код нейросети, который представлен в соседних файлах на GitHub
    bot.send_message(message.from_user.id, "Вот топ-10 подходящих ссылок на фото:")

    #   здесь будут фото


    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, давай зарегистрируемся)")
        bot.register_next_step_handler(message, start)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")





# def get_age(message):
#     global age
#     while age == 0: #проверяем что возраст изменился
#         try:
#              age = int(message.text) #проверяем, что возраст введен корректно
#         except Exception:
#              bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
#         keyboard = types.InlineKeyboardMarkup() #наша клавиатура
#         key_yes: InlineKeyboardButton = types.InlineKeyboardButton(text='Да', callback_data='yes') #кнопка «Да»
#         keyboard.add(key_yes) #добавляем кнопку в клавиатуру
#         key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
#         keyboard.add(key_no)
#         question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?'
#         bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)



bot.polling(none_stop=True, interval=0)
