#!/usr/local/bin/python
# -*- encoding: utf-8 -*-
import oauth2 as oauth
import json
import urllib
import sys, os

CONSUMER_KEY =  "DQyKeYJ5bkBaVu5irMAzDx9CY"
CONSUMER_SECRET = "aCnXZJCPZnuIMM0aB9GAkTSNLwgZmJ0LWsU4BOTbRokrQ0lClr"
ACCESS_KEY = "3221125529-mpTr0WBzQH2aw7Dhgq9siGgtoNmaYeTl8GBl8v4"
ACCESS_SECRET = "hpUXlczLOLKQYX2e8GZdfQ9Q1ZoI3YjEl42FQ2OLJq1dR"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)


def download(url,name):
    """
    download a image in the form of

    url = http://www.example.com
    name = '00000000.jpg'
    """
    image=urllib.URLopener()
    image.retrieve(url,name)  # download image at URL



params = {'screen_name':'LudovicSantos','include_rts':1,'count':50}  
	#con el count cuenta los rts aunque no los incluyas porque es asi de wai D:
twurl = "https://api.twitter.com/1.1/statuses/user_timeline.json?"+urllib.urlencode(params)
response, data = client.request(twurl)


counter=0

tweets = json.loads(data)

os.chdir('./fotos')
for tweet in tweets:
    if 'extended_entities' in tweet:
	    for media in tweet['extended_entities']['media']:
		numero = str('000000'+str(counter))
		nombre = str(numero+".jpg")
		counter+=1
		download(media['media_url'],nombre) 
	    	print media['media_url']














