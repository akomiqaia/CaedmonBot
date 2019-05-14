import telebot
import datetime
from datetime import datetime, date, timedelta

def rotLeft(a, d):
    return a[d:] + a[:d]

people = ['Ako', 'Camila', 'Teressa', 'Zach', 'Molly', 'Matthew', 'Max']
options_of_rota = ['stairs', 'Kitchen', 'bathroomUP', 'bathroomDOWN', 'Living Room', 'Plants and Garden', 'Shopping']
things_to_be_done = []
start_date = date(2019, 5, 10)
today = date.today()
days_passed = (today - start_date).days
number_of_rotation = days_passed // 7 
if number_of_rotation % 7 == 0:
  things_to_be_done = options_of_rota
else:
  things_to_be_done = rotLeft(options_of_rota, number_of_rotation % 7)
  


rota_message = ''
for i in range(len(people)):
  rota_message += people[i] + ' you have to do ' + things_to_be_done[i] + ' for this week \n' 

bot = telebot.TeleBot("686681991:AAF7UZokmM8hfL4QwlYjndSllBefphgePfM")

@bot.message_handler(commands=['rota'])
def send_welcome(message):
	bot.reply_to(message, rota_message)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
