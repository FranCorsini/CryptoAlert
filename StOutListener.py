from tweepy.streaming import StreamListener

class StdOutListener(tweepy.StreamListener):

    def on_status(self, status):
        text = status.text
        
        #TODO, filter the tweets only to be the listing

