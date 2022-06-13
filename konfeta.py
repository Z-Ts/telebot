import telebot
from telebot import types
n = 0
m = 0
igr1 = 0
igr2 = 0
z = 0
token=''
bot= telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def start(message):
  if message.text == '/start':
    bot.send_message(message.chat.id,"введите количество конфет")
    bot.register_next_step_handler(message, get_n)

def get_n(message):
  global n
  n = int (message.text)
  if n >=4 :
    bot.send_message(message.chat.id, "ход игрока 1: возьмите конфеты от 1 до 4")
  else: 
    bot.send_message(message.chat.id, "ход игрока 1:возьмите конфеты от 1 ",n)
  bot.register_next_step_handler(message, get_hod)
 

def get_hod(message):
  global m
  global n
  m = int( message.text ) 
  if m > 4: 
    bot.send_message(message.chat.id, "введено некорректное число")
    bot.register_next_step_handler(message, get_hod)
  if m <=4: 
    if m<=n:
      
      n= n - m
      global igr1
      igr1 = igr1 +1
      print (igr1,igr2)
      if n!=0:
        if n >=4 :
          bot.send_message(message.chat.id, "ход игрока 2: возьмите конфеты от 1 до 4")
        if n<4: 
          bot.send_message(message.chat.id, f"ход игрока 2:возьмите конфеты от 1 до {n}")
          
        bot.register_next_step_handler(message, get_hod2)
      if n==0:
        bot.send_message(message.chat.id, "конец игры,победил игрок 1")
  
def get_hod2(message):
  global m2
  m2 = int( message.text ) 
  global n
  if m2 > 4 : 
    bot.send_message(message.chat.id, "введено некорректное число")
    bot.register_next_step_handler(message, get_hod2) 
  if m2<=4:
    if m2<=n:
      n= n - m2
      global igr2
      igr2 = igr2 +1
      print (igr1,igr2)
      if n!=0:
        if n >=4 :
          bot.send_message(message.chat.id, "ход игрока 1: возьмите конфеты от 1 до 4")
        if n<4: 
          bot.send_message(message.chat.id, f"ход игрока 1:возьмите конфеты от 1 до {n} " )

        bot.register_next_step_handler(message, get_hod)
      if n ==0:
        bot.send_message(message.chat.id, "конец игры, победил игрок 2")

bot.polling(non_stop = True)