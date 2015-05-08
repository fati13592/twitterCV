#!/usr/local/bin/python
# -*- encoding: utf-8 -*-
import oauth2 as oauth
import json
import urllib
import sys

CONSUMER_KEY =  "DQyKeYJ5bkBaVu5irMAzDx9CY"
CONSUMER_SECRET = "aCnXZJCPZnuIMM0aB9GAkTSNLwgZmJ0LWsU4BOTbRokrQ0lClr"
ACCESS_KEY = "3221125529-mpTr0WBzQH2aw7Dhgq9siGgtoNmaYeTl8GBl8v4"
ACCESS_SECRET = "hpUXlczLOLKQYX2e8GZdfQ9Q1ZoI3YjEl42FQ2OLJq1dR"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

params = {'screen_name':'LauraFGandoy','include_rts':1,'count':50}  
	#con el count cuenta los rts aunque no los incluyas porque es asi de wai D:
twurl = "https://api.twitter.com/1.1/statuses/user_timeline.json?"+urllib.urlencode(params)
response, data = client.request(twurl)


tweets = json.loads(data)
for tweet in tweets:
    #print tweet['text']
    #print "\n"
    if 'extended_entities' in tweet:
	    print "\n"
	    #print tweet['geo']
	    for media in tweet['extended_entities']['media']:
	    	print media['media_url']
    #print "\n"

print "\n"
