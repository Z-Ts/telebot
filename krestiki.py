import telebot
from telebot import types
count = 0
token=''
bot= telebot.TeleBot(token)
s = {'11':'', '12': '', '13': '','21':'', '22': '', '23': '','31':'', '32': '', '33': ''}
s1 = {'11':'', '12': '', '13': '','21':'', '22': '', '23': '','31':'', '32': '', '33': ''}

@bot.message_handler(content_types=['text'])
def start(message):
  if message.text == '/start':
    bot.send_message(message.chat.id, f"ход игрока 1. выберите ячейку:{s1}" )
    bot.register_next_step_handler(message, get_hod1)
def get_hod1(message):
  global s
  global s1
  n = message.text
  print (n)
  if n not in s1: bot.send_message(message.chat.id, f"введено некорректное значение или ячейка занята. выберите ячейку:{s1}" ), bot.register_next_step_handler(message, get_hod1)
  if n in s1:
    s[n] = 'первый'
    print(s)
    del s1[n]
    global count
    count = count +1
    print (count,'count')
    if count <=9:
      if s['11'] =='первый' or s['11'] =='второй':

        if  s['11'] == s['12'] and  s['12'] == s['13']:
          bot.send_message(message.chat.id, f"выиграл игрок {s['11']}" )
          exit(0)

      if s['21'] =='первый' or s['21'] =='второй':
        if s['21'] == s['22'] and  s['22'] == s['23'] :
          bot.send_message(message.chat.id, f"выиграл игрок {s['21']}" )
          exit(0)

      if s['31'] =='первый' or s['31'] =='второй':
        if s['31'] == s['32'] and  s['32'] == s['33'] :
          bot.send_message(message.chat.id, f"выиграл игрок {s['31']}" )
          exit(0)

      if s['11'] =='первый' or s['11'] =='второй':
        if s['11'] == s['22'] and  s['22'] == s['33'] :
          bot.send_message(message.chat.id, f"выиграл игрок {s['11']}" )
          exit(0)

      if s['13'] =='первый' or s['13'] =='второй':
        if s['13'] == s['22'] and  s['22'] == s['31'] :
          bot.send_message(message.chat.id, f"выиграл игрок {s['13']}" )
          exit(0)

      if s['11'] =='первый' or s['11'] =='второй':
        if s['11'] == s['21'] and  s['21'] == s['31']:
          bot.send_message(message.chat.id, f"выиграл игрок {s['11']}" )
          exit(0)

      if s['12'] =='первый' or s['12'] =='второй':
        if s['12'] == s['22'] and  s['22'] == s['32']:
          bot.send_message(message.chat.id, f"выиграл игрок {s['12']}" )
          exit(0)

      if s['13'] =='первый' or s['13'] =='второй':
        if s['13'] == s['23'] and  s['23'] == s['33'] :
          bot.send_message(message.chat.id, f"выиграл игрок {s['13']}" )
          exit(0)

      bot.send_message(message.chat.id, f"ход игрока 2. выберите ячейку:{s1}" )
      bot.register_next_step_handler(message, get_hod2)
        
    if count==9: bot.send_message(message.chat.id, 'конец игры. ничья' )
    
 
def get_hod2(message):
  global s
  global s1
  n1 = message.text
  s[n1] = 'второй'
  print(s)
  if n1 not in s1: bot.send_message(message.chat.id, f"введено некорректное значение или ячейка занята. выберите ячейку:{s1}" ), bot.register_next_step_handler(message, get_hod2)
  if n1 in s1:
    del s1[n1]
    global count
    count = count +1
    print (count, 'count')
    if count <=9:
      if s['11'] =='первый' or s['11'] =='второй':

        if  s['11'] == s['12'] and  s['12'] == s['13']:
          bot.send_message(message.chat.id, f"выиграл игрок {s['11']}" )
          exit(0)
        

      if s['21'] =='первый' or s['21'] =='второй':
        if s['21'] == s['22'] and  s['22'] == s['23'] :
          bot.send_message(message.chat.id, f"выиграл игрок {s['21']}" )
          exit(0)

      if s['31'] =='первый' or s['31'] =='второй':
        if s['31'] == s['32'] and  s['32'] == s['33'] :
          bot.send_message(message.chat.id, f"выиграл игрок {s['31']}" )
          exit(0)

      if s['11'] =='первый' or s['11'] =='второй':
        if s['11'] == s['22'] and  s['22'] == s['33'] :
          bot.send_message(message.chat.id, f"выиграл игрок {s['11']}" )
          exit(0)

      if s['13'] =='первый' or s['13'] =='второй':
        if s['13'] == s['22'] and  s['22'] == s['31'] :
          bot.send_message(message.chat.id, f"выиграл игрок {s['13']}" )
          exit(0)

      if s['11'] =='первый' or s['11'] =='второй':
        if s['11'] == s['21'] and  s['21'] == s['31']:
          bot.send_message(message.chat.id, f"выиграл игрок {s['11']}" )
          exit(0)

      if s['12'] =='первый' or s['12'] =='второй':
        if s['12'] == s['22'] and  s['22'] == s['32']:
          bot.send_message(message.chat.id, f"выиграл игрок {s['12']}" )
          exit(0)

      if s['13'] =='первый' or s['13'] =='второй':
        if s['13'] == s['23'] and  s['23'] == s['33'] :
          bot.send_message(message.chat.id, f"выиграл игрок {s['13']}" )
          exit(0)

      bot.send_message(message.chat.id, f"ход игрока 1. выберите ячейку:{s1}" )
      bot.register_next_step_handler(message, get_hod1)
    if count==9: bot.send_message(message.chat.id, 'конец игры. ничья' )
   
 


bot.polling(non_stop = True)