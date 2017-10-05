#!/usr/bin/env python

'''
    This script uses pulls the Twitter profiles of ONA attendees

'''

import sys
import csv
import string
#import simplejson
from twython import Twython

#FOR OAUTH AUTHENTICATION -- NEEDED TO ACCESS THE TWITTER API
t = Twython(app_key='SL40yTFKpyJUauiPmmmu8DG7Y', #REPLACE 'APP_KEY' WITH YOUR APP KEY, ETC., IN THE NEXT 4 LINES
app_secret='OoqCjf0ZOLsTJF3MK3yDqUp9ns4M0R2Y7fj804JyUYxY8yILx9Q',
oauth_token='3983607252-xgaYCTtP1zQgBGvDhXpfK1yu8O2PZlx7RQzKMuS',
oauth_token_secret='OKTwxCS0i5ZpjWvOUe6sKOK6M0lBr4AUW9VziitRyzOgb')


screen_name = []

with open('attendees.csv') as csvfile: 
    reader=csv.reader(csvfile)
    for row in reader: 
        if row[2] != '': 
            screen_name.append(row[2])

users = []
#for user in screen_name: 
    #users.append(t.lookup_user(screen_name = user))
#users = t.lookup_user(screen_name = screen_name)
print users

print t.lookup_user(screen_name = "tristaaan")