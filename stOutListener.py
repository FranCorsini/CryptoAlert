# -*- coding: utf-8 -*-
from tweepy.streaming import StreamListener
from SMS import Phone
import json
import re

class StdOutListener(StreamListener):

    phone = Phone()
    hotwords = ['Lists','lists','List','list']

    def on_data(self, datastream):
        data = json.loads(datastream)
        text = data['text']
        

        #print "Tweet from "
        #print data['user']['id_str']
        if data['user']['id_str'] == "877807935493033984":
            print "TWEET FROM BINACE"
            print text


            if re.search(r"(?=("+'|'.join(self.hotwords)+r"))", text):
        		self.phone.send_all_sms(text)
    '''
    def test(self,text):
        self.hotwords = ['Lists','lists','List','list']

        if re.search(r"(?=("+'|'.join(self.hotwords)+r"))", text):
            self.phone.send_all_sms(text)
    '''

    
