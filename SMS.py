from twilio.rest import Client


class Phone(object):

	account_sid = "PNf940f08316a46b3f9cbcfeb198649135"
	auth_token = "1b70aab2e2b8ce322e2b048d95e1b9ea"

	client = Client(account_sid, auth_token)

	def send_all_sms(self,text):
		with open('numbers.txt','r') as numbers:
			for num in numbers:
				self.send_sms(num,text)

	def send_sms(self,number,text):

		print number
		print text

		'''
		self.client.api.account.messages.create(
		    to=number,
		    from_="+17163302683",
		    body=text)
		   '''


		