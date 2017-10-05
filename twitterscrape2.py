#!/usr/bin/env python

'''
    This script uses pulls the Twitter profiles of ONA attendees

'''

import sys
import csv
import string
import tweepy
import json
import time
#import simplejson

#FOR OAUTH AUTHENTICATION -- NEEDED TO ACCESS THE TWITTER API
auth = tweepy.OAuthHandler('vyeS7U4cVnoZohAFMJ7z6NCed', 'CAnsOYr4TiLTH405eX7VtilIxpOOe9vEJKasAS92rAlTd2wncF')
auth.set_access_token('230190627-IXYNWOobg8XVAio5uKXKyVTIxJjVlhBLRhXTeGlX', '26bQPEhGrRftnJBoW2JvwfIoifjQ0l3LwF8tTjLyCTnMK')
api = tweepy.API(auth)

screen_name = []

with open('ona17_clean.csv') as csvfile: 
    reader=csv.reader(csvfile)
    for row in reader: 
        if row[2] != '': 
            screen_name.append(row[2])

def limit_handled(cursor):
	try:
		yield cursor
	except tweepy.RateLimitError:
		time.sleep(15 * 60)


users = { "list": []}
try: 
	for p in screen_name: 
		try:
			users["list"].append(api.get_user(screen_name=p))
			print p + " done"
		except tweepy.RateLimitError as e:
			print e
			print "we are waiting"
			print users
			with open('profiles.json', 'w') as out:
				json.dump(users, out)
			time.sleep(60)
		except Exception as e: 
			print e
			continue
	with open('profiles.json', 'w') as out:
		json.dump(users, out)
except Exception as e:
	print e


#is not JSON serializable