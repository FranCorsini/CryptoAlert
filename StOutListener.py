# -*- coding: utf-8 -*-
from tweepy.streaming import StreamListener
import json
import re

class StdOutListener(StreamListener):


    def on_data(self, datastream):
        data = json.loads(datastream)
        text = data['text']
        hotwords = ['Lists','Adds','Distributes']
        #text = status.text
        
        if data.user.id_str == "877807935493033984":
            print "TWEET FROM BINACE"
            print text

        #TODO remove
        #only for testing
        #print status

        if re.search(hotwords, text):
    		#matched! need to send 
            #only for testing
			print "matched"

            #TODO add the already done in a list so it does not repeat (the retweets are sent)