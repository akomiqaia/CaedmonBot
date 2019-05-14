import json
import  requests
import time
from datetime import datetime, date, timedelta


TOKEN = '686681991:AAF7UZokmM8hfL4QwlYjndSllBefphgePfM'
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


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


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids) 

def handle_updates(updates):
    for update in updates["result"]:
        print(update)
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        user = update["message"]["chat"]["first_name"]
        if text == "/done":
            keyboard = build_keyboard(things_to_be_done)
            send_message("Select an item to delete", chat, keyboard)
        elif text == "/rota":
            send_message(rota_message, chat)
        elif text in things_to_be_done:
            send_message("Thanks {} for doing the {}".format(user,text), chat)
            things_to_be_done.remove(text)
        
        

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id, reply_markup=None):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    if reply_markup:
      url += "&reply_markup={}".format(reply_markup)
    get_url(url)
    


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.5)

def build_keyboard(items):
    keyboard = [[item] for item in items]
    reply_markup = {"keyboard":keyboard, "one_time_keyboard": True}
    return json.dumps(reply_markup)

if __name__ == '__main__':
    main()
