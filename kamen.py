import telebot
from telebot import types
n =''
m =''
token=''
bot= telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def start(message):
  if message.text == '/start':
    bot.send_message(message.chat.id, "ход игрока 1: камень/ножницы/бумага" )
    bot.register_next_step_handler(message, get_hod1)

def get_hod1(message):
  global n
  n = message.text
  print (n)
  if n == 'камень' or n == 'ножницы'or n == 'бумага':
    bot.send_message(message.chat.id, "ход игрока 2:камень/ножницы/бумага")
    bot.register_next_step_handler(message, get_hod2)
  
  elif n != 'камень' or n != 'ножницы'or n != 'бумага':
    bot.send_message(message.chat.id, "введено некорректное значение, попробуйте еще раз")
    bot.register_next_step_handler(message, get_hod1)
  

def get_hod2(message):
  global m
  m = message.text
  
  if m == 'камень' or m == 'ножницы'or m == 'бумага': 
    print (m)   
    if n == m:
      bot.send_message(message.chat.id, "ничья")
    elif n == 'камень' and m == 'бумага':
      bot.send_message(message.chat.id, "победил игрок 1")
    elif n == 'бумага' and m == 'камень':
      bot.send_message(message.chat.id, "победил игрок 2")
    elif n == 'камень' and m == 'ножницы':
      bot.send_message(message.chat.id, "победил игрок 1")
    elif n == 'ножницы' and m == 'камень':
      bot.send_message(message.chat.id, "победил игрок 2")
    elif n == 'ножницы' and m == 'бумага':
      bot.send_message(message.chat.id, "победил игрок 1")
    elif n == 'бумага' and m == 'ножницы':
      bot.send_message(message.chat.id, "победил игрок 2")
  elif m != 'камень' or m != 'ножницы'or m != 'бумага':
    bot.send_message(message.chat.id, "введено некорректное значение, попробуйте еще раз")
    bot.register_next_step_handler(message, get_hod2)  


bot.polling(non_stop = True)