# -*- coding: utf-8 -*-
"""
Created on Sun May 24

@author: Mehmeta
"""

import tweepy # Twitter API'sine bağlanmak için

# Twitter'dan alacağınız token-keyler
consumer_key = 'your_consumer_key'
consumer_secret = 'consumer_secret'

access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Twitter API'sine bağlanma
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# tweepy ile twitter zaman sınırlarına bağlı kalarak istek göndermek için;
api = tweepy.API(auth,wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)