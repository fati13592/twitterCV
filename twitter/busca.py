#!/usr/local/bin/python
# -*- encoding: utf-8 -*-
import oauth2 as oauth
import json
import urllib
import sys

CONSUMER_KEY =  "lXpuuNKrWgbIdIlktNhDkWax9"
CONSUMER_SECRET = "Tmj4atTY8BJ2UX3wteSMS105zyXevvkp3PNagD9KSTQxYQOm22"
ACCESS_KEY = "3221125529-81rcLninNVXdvC1zjXp4OjrBFyrzollmebqlSJo"
ACCESS_SECRET = "2deMfZxiXIdUIp07J2vjJlvcBhLDQss7x42Rfep600RSl"

term=sys.argv[1]
n=sys.argv[2]

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

params = {'count': n,'q':term,'lang':'es'}
twurl = "https://api.twitter.com/1.1/search/tweets.json?"+urllib.urlencode(params)
response, data = client.request(twurl)

statuses = json.loads(data)
for status in statuses['statuses']:
    print status['text']
    print "\n"
	
