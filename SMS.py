from twilio.rest import Client


class Phone(object):



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


		