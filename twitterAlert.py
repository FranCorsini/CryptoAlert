from tweepy import OAuthHandler
from tweepy import Stream
from stOutListener import StdOutListener
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


consumer_key="2cLgs8hNW9xIvNvalb3ViS80v"
consumer_secret="Qxo9lH86kU3aq4cYjkdbBoa7yTbNjatM0jWijZGfzDSkRovLNi"


access_token="116003647-JKLsIfJehzIWoP5tuGZWBpqNKB2MJ74u8y8yXbP1"	
access_token_secret="KNG0LfOYO3Nr2Yh2GBy4J6hlBJ0CPoxBD6D1HlnHPzsBM"

l = StdOutListener()


def main():
	#fai partire lo stream listener
	try:
		auth = OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		stream = Stream(auth, l)	
		stream.filter(follow=["877807935493033984"])
	except Exception as e:
		print(e)
		return False


if __name__ == '__main__':
	while 1:
		print('RECONNECTING')
		err = main()
		time.sleep(1)
		#if err == False:
			#todo wait a bi