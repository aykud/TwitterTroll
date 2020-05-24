# -*- coding: utf-8 -*-
"""
Created on Sun May 24

@author: Mehmeta
"""

import pandas as pd
import numpy as np
import tweepy
"""
block_from listesine yazdığınız hesapların takipçilerini çekip,
bu takipçileri bloklama
"""
!python 0_twitter_OAuthHandler.py

block_from = ["hesap_1", "hesap_2"] # Buraya istediğiniz kadar hesap yazabilirsiniz.
  
screen_name_ids = []
i=0
for user in block_from: 
    followers = []
    i +=1
    print(i, '. ', 'username: ', user)
    try:
        for page in tweepy.Cursor(api.followers_ids, screen_name=user).pages():
            followers.extend(page)
    except tweepy.TweepError:  
        time.sleep(20)  
        continue
    for follower_ids in followers:
        screen_name_ids.append([user, follower_ids])
        
df =  np.reshape(screen_name_ids, (-1, 2))
df = pd.DataFrame({'to': df[:, 0], 'follower_id': df[:, 1]})
# to kolonunda takip edilen hesabın kullanıcı adı,
# follower_id kolonunda da bu hesabı takip eden kullanıcıların id'si yer alır.
# Takipçilerin kullanıcı isimlerini çekmek için Twitter API'si ile lookup yapman gerekli.
# Bu da zaman maliyeti getireceği için şu an burada yok.
print(df.head())


# Blok listesi: id'ler tekilleştirilir.
block_list=list(map(int, list(df['follower_id'].unique())))
len(block_list)

blocked = []
i=0
for user in block_list:
    try:
        i +=1
        print(i, '. ', 'user_id: ', user)
        api.create_block(user)
    except tweepy.TweepError:
        time.sleep(20)
        continue
    blocked.append(user)