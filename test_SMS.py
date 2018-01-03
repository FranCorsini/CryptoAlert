from twilio.rest import Client




account_sid = "AC70b7cf25025b026fe5b7efb70de758b6"
auth_token = "1b70aab2e2b8ce322e2b048d95e1b9ea"

client = Client(account_sid, auth_token)


client.api.account.messages.create(
	to="+17162071403",
	from_="+17163302683",
	body="Hello from your new phone number :)"
	)
