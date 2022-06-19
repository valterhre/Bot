import time
from pytube import YouTube
import telebot
import os
import requests # to get image from the web
from collections import deque
q=deque(maxlen=3)

token = os.environ['token']
CHAT_NUMBER= os.environ['chat_number']
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["foto"])
def foto(m):
    f= open()
    bot.send_photo(m.chat.id,)
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
    # bot.send_photo(m.chat.id, 'name.png')
    time.sleep(50)
    bot.send_message(m.chat.id, 'op')
@bot.message_handler(commands=["yout"])
def you(m):
    url=q[-1]
    yt = YouTube(url)
    print(url)
    stream = yt.streams.get_by_itag(18)
    stream.download(filename='filmp4.mp4')#download 720
    # name=name.replace(' ','_')
    # os.rename(name,'fil.mp4')
    f=open('filmp4.mp4', 'rb')
    bot.send_video(m.chat.id, f)
    f.close()
    os.remove('filmp4.mp4')
    print('dd')

@bot.message_handler(commands=["po"])
def se(m):
    image_url=q[-1]
    print('qqq')
    img_data = requests.get(image_url).content
    filename = image_url.split('/')
    filename = filename[-1]
    with open(f'./files/{filename}', 'wb') as handler:
        handler.write(img_data)
    f=open(f'./files/{filename}', 'rb')
    bot.send_photo(CHAT_NUMBER, f)
    f.close()
    os.remove(f'./files/{filename}')
    bot.send_message(m.chat.id,'ok')
@bot.message_handler(commands=["help"])
def send_welcome(m, res=False):
    for r in range (1,100):
        bot.send_message(CHAT_NUMBER, r)
        time.sleep(10)

# Получение сообщений от юзера
@bot.message_handler(commands=["help"])
def send_welcome(m, res=False):
    print(m.chat.id, bot.last_update_id)

@bot.message_handler(commands=['io'])
def se(m):
    f=open('name.png', 'rb')
    bot.send_photo(CHAT_NUMBER, f)



@bot.message_handler(commands=["url"])
def i(m):
    image_url=q[-1]
    img_data = requests.get(image_url).content
    filename = image_url.split('/')
    filename = filename[-1]
    with open(f'./files/{filename}', 'wb') as handler:
        handler.write(img_data)
    f=open(f'./files/{filename}', 'rb')
    bot.send_photo(m.chat.id, f)
    f.close()
    os.remove(f'./files/{filename}')
    bot.send_message(m.chat.id,'ok')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    print(message.id)
    q.append(message.text)
    print(q)
    li=['бля',"пизд","ёб","еб",'хуй', "сука", "дебил"]
    for x in li:
        print("ooo",((message.text).lower().startswith(x)))
        if (message.text).lower().startswith(x):
            bot.reply_to(message, 'не матерись, дебил')
            bot.delete_message(message.chat.id, message_id=message.id)

bot.polling(none_stop=True, interval=0)