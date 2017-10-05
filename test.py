#!/usr/bin/env python

'''
    This script uses pulls the Twitter profiles of ONA attendees

'''

import oauth2

def oauth_req(url, key, secret, http_method="GET", post_body=””, http_headers=None):
    consumer = oauth2.Consumer(key="SL40yTFKpyJUauiPmmmu8DG7Y", secret="oqCjf0ZOLsTJF3MK3yDqUp9ns4M0R2Y7fj804JyUYxY8yILx9Q")
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content

home_timeline = oauth_req( 'https://api.twitter.com/1.1/statuses/home_timeline.json', '3983607252-xgaYCTtP1zQgBGvDhXpfK1yu8O2PZlx7RQzKMuS', 'OKTwxCS0i5ZpjWvOUe6sKOK6M0lBr4AUW9VziitRyzOgb' )