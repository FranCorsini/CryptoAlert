from twilio.rest import Client


class Phone(object):

	account_sid = "PNf940f08316a46b3f9cbcfeb198649135"
	auth_token = "1b70aab2e2b8ce322e2b048d95e1b9ea"

	client = Client(account_sid, auth_token)

	def send_all_sms(text):
		with open('phone_numbers.txt','r') as numbers:
			for num in numbers:
				send_sms(num,text)

	def send_sms(number,text):
		client.api.account.messages.create(
		    to=number,
		    from_="+17163302683",
		    body=text)


	"""docstring for Phone"""
	def __init__(self, arg):
		super(Phone, self).__init__()
		self.arg = arg
		