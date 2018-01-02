from tweepy import OAuthHandler
from tweepy import Stream
from stdoutlistener import StdOutListener

consumer_key="51P3KpeuwPd36GlnprCAkDeym"
consumer_secret="kPVvXepP1ahCqfhDF7disL7eLqiCDh11NSH5MGO55VxbGKnNgC"

access_token="116003647-ELfyysC98T6jIBJu6HC7c6Kj6DYTyVQKAu9fY6Vl"
access_token_secret="IWBDNlcYBWOQa5hdzD05spaplyimvTnswAZcCMBA2gt5w"

l = StdOutListener()


def main():
	#fai partire lo stream listener
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)
	try:
		stream.filter(follow=877807935493033984)
	except Exception as e:
		print(e)
		return False