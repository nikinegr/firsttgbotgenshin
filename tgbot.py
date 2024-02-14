import telebot
from telebot import types
import schedule
from time import sleep
from threading import Thread

bot = telebot.TeleBot('5697062049:AAGcSg54-dFtf_iADUPByT8Vqu7e4g7W8SE')

number1 = 0
number2 = 0


def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)


@bot.message_handler(commands=['start', 'help', 'hi', 'bye', 'solve'])
def reply(message):
    if message.text == '/start':
        bot.reply_to(message, 'i have this is command(/start,/help,/hi,/bye)')
    if message.text == '/hi':
        bot.reply_to(message, 'hi,what do you want leather dont bother me')
    if message.text == '/bye':
        bot.reply_to(message, 'goodbye user')
    if message.text == '/help':
        bot.reply_to(message, 'This is help command')
    if message.text == '/solve':
        bot.reply_to(message, 'pleas write you name')
        bot.register_next_step_handler(message, nam1)
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row('people(personazhi)')
    keyboard.row('weapon(zdroya)')
    bot.send_message(message.chat.id, 'Chose a file', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def buttons2(message):
    keyboard = types.InlineKeyboardMarkup()
    if message.text=='people(personazhi)':
        Button1 = types.InlineKeyboardButton('Hu tao', url='https://genshin-info.ru/wiki/personazhi/hu-tao/')
        keyboard.row = types.InlineKeyboardButton('Kokomi', url='https://genshin-info.ru/wiki/personazhi/kokomi/')
        keyboard.row = types.InlineKeyboardButton('Ayaka', url='https://genshin-info.ru/wiki/personazhi/ayaka/')
        keyboard.row = types.InlineKeyboardButton('kadzuha', url='https://genshin-info.ru/wiki/personazhi/kadzukha/')
        keyboard.row = types.InlineKeyboardButton('Noelle', url='https://genshin-info.ru/wiki/personazhi/noelle/')
        keyboard.row = types.InlineKeyboardButton('Tignari', url='https://genshin-info.ru/wiki/personazhi/tignari/')
        keyboard.row = types.InlineKeyboardButton('Rayden', url='https://genshin-info.ru/wiki/personazhi/rayden/')
        bot.send_message(message.chat.id, 'Chose a file', reply_markup=keyboard)
    keyboard = types.ReplyKeyboardMarkup()


    if message.text == 'weapon(zdroya)':
        keyboard.row = types.InlineKeyboardButton('kopya Homa', url='https://genshin-info.ru/wiki/oruzhie/kopya/posokh-khomy/')
        keyboard.row = types.InlineKeyboardButton('katalizator Pritotip', url='https://genshin-info.ru/wiki/oruzhie/katalizatory/prototip-yantar/')
        keyboard.row = types.InlineKeyboardButton('mech Kharan-geppaku-futsu', url='https://genshin-info.ru/wiki/oruzhie/mechi/kharan-geppaku-futsu/')
        keyboard.row = types.InlineKeyboardButton('mech Omut', url='https://genshin-info.ru/wiki/oruzhie/mechi/dragotsennyy-omut/')
        keyboard.row = types.InlineKeyboardButton('Dvuruk favonia', url='https://genshin-info.ru/wiki/oruzhie/dvuruchnye-mechi/dvuruchnyy-mech-favoniya/')
        keyboard.row = types.InlineKeyboardButton('luk akva', url='https://genshin-info.ru/wiki/oruzhie/luki/akva-simulyakrum/')
        keyboard.row = types.InlineKeyboardButton('kapya favoniya', url='https://genshin-info.ru/wiki/oruzhie/kopya/kopye-favoniya/')
        bot.send_message(message.chat.id, 'Chose a file', reply_markup=keyboard)



def nam1(message):
    global number1
    number1 = message.text
    bot.register_next_step_handler(message, nam2)


def nam2(message):
    global number2
    number2 = message.text
    bot.register_next_step_handler(message, opr)


def opr(message):
    global operation1
    operation1 = message.text
    if operation1 == '+':
        bot.send_message(message.from_user.id, (number1) + (number2))


scheduleThread = Thread(target=schedule_checker)
scheduleThread.daemon = True
scheduleThread.start()

bot.infinity_polling()




