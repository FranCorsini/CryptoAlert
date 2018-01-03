from twilio.rest import Client






client = Client(account_sid, auth_token)


client.api.account.messages.create(
	to="+17162071403",
	from_="+17163302683",
	body="Hello from your new phone number :)"
	)
