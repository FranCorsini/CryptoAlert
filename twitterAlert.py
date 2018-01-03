from tweepy import OAuthHandler
from tweepy import Stream
from stOutListener import StdOutListener
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')




l = StdOutListener()


def main():
	#fai partire lo stream listener
	try:
		auth = OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		stream = Stream(auth, l)	

		#to remove
		'''
		print "sending 1"
		l.test("test message")
		print "sending 2"
		l.test("This is a Lists")
		'''
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
