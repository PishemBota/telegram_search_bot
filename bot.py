import re
import telebot
from telebot import types

TOKEN = '<ваштокен>'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add('Поиск', 'Как пользоваться ботом?')
	
	msg = bot.send_message(m.chat.id, 'Привет. Это бот для поиска по Wikipedia. Нажимай на кнопку и вводи свой поиск!',
		reply_markup=keyboard) # Вместо Wikipedia вы можете писать другое
	bot.register_next_step_handler(msg, poisk)
def poisk(m):
	if m.text == "Поиск": 
		msg1 = bot.send_message(m.chat.id, 'Хорошо. Теперь введи поиск:')
		bot.register_next_step_handler(msg1, echo_message)
	elif m.text == "Как пользоваться ботом?": 
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add('Назад')
		msg = bot.send_message(m.chat.id, 'Тут должна быть инструкция, но есть мой замечательный канал @pishembota',
			reply_markup=keyboard)
		bot.register_next_step_handler(msg, poisk)
	elif m.text == "Назад":
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add('Поиск', 'Как пользоваться ботом?')
	
		msg = bot.send_message(m.chat.id, 'Привет. Это бот для поиска по Wikipedia. Нажимай на кнопку и вводи свой поиск!',
			reply_markup=keyboard)
		bot.register_next_step_handler(msg, poisk)
@bot.message_handler(func=lambda message: True)
def echo_message(m): 
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add('Назад')
	msg = bot.send_message(m.chat.id, 'Вот твой поиск: https://ru.wikipedia.org/w/index.php?search=' + re.sub(' +', '%20', m.text),
		reply_markup=keyboard)

	bot.register_next_step_handler(msg, poisk)

bot.polling()