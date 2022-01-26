import Service

number = input('[green]Beeante HOMeP tenedona: (бes + ')

class Tinder(Service):
async def run(self):
await self.post(
"https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
data={"phone_number": number},
)
