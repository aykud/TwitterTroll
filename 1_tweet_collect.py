# -*- coding: utf-8 -*-
"""
Created on Sun May 24

@author: Mehmeta
"""

import pandas as pd
import numpy as np

import GetOldTweets3 as got
# Dokümantasyona buradan ulaşabilirsiniz: https://github.com/Mottl/GetOldTweets3

import time

tweetCriteria = got.manager.TweetCriteria().setQuerySearch('%F0%9F%9F%A2%F0%9F%87%B9%F0%9F%87%B7')\
                                            .setSince("2020-05-12")\
                                            .setUntil("2020-05-13")\
                                            .setMaxTweets(5000)\
                                            .setLang('tr')

""" 
# setQuerySearch: Buraya aramak istediğiniz ifadeyi yazmalısınız
Örnek: setQuerySearch('python') içinde python ifadesi geçen;
		tweetleri, kullanıcı isimlerini, bio'kısmında python geçen tüm profilleri getirir.
		Emoji aratmak isterseniz, https://emojipedia.org/large-green-circle/ sitesinden aratabilirsiniz.
		Sayfanın en altında "Browse" bölümünde twitter'a tıklarsanız, doğrudan twitter search açılır.
		Açılan linkteki "https://twitter.com/search?q="" ifadesinden hemen sonra çıkan ifayeyi bu alana yazabilirsiniz.

# setSince: Aramaya hangi tarihten itibaren başlamak istediğinizi ifade eder. YYYY-MM-DD
# setUntil: Aramanın hangi tarihte sona ermesini istediğinizi ifade eder. YYYY-MM-DD
# setMaxTweets: -1 yazarsanız, aradığınız sorgu ile ilgili kaç tweet varsa, hepsini getirir.
				Ama twitter buna engel olabiliyor. Ben kendi aramalarımda 10.000 civarı seçiyorum genellikle.
				
# setMaxTweets: Aradığınız sorgunun hangi dilde olmasını isterseniz, bunu yazmalısınız.
# Listeye şu linkten ulaşabilirsiniz: https://developer.twitter.com/en/docs/twitter-for-websites/twitter-for-websites-supported-languages/overview
"""

print('Start...')
# Yukarıda girdiğimiz kriterlere uyan tweetler "tweets" objesine alınır.
# Bir hesabın, girdiğimiz kriterler içinde 1'den fazla tweeti varsa, listeye o kadar girer.
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
print('Collecter!')

# Tweets objesindeki elemanları bir listenin içine alıyoruz.
tweets_list = [[twet.username, tweet.id, tweet.permalink, tweet.date, tweet.text, tweet.hashtags, tweet.geo] for tweet in tweets]     
tweets_list =  np.reshape(tweets_list, (-1, 7))


df = pd.DataFrame({'username': tweets_list[:, 0], 'tweet_id': tweets_list[:, 1],
                   'permalink':tweets_list[:, 2], 'date':tweets_list[:, 3],
                   'text':tweets_list[:, 4], 'hashtags':tweets_list[:, 5],
                   'geo':tweets_list[:, 6]})

# tweetin içindeki tüm hashtagler hashtags kolonu içinde yer alıyor.
# Ancak sorun şu ki, hashtagte Türkçe karakter varsa, hashtag orada kesiliyor.
df['hashtags'] = df.text.str.findall(r'#.*?(?=\s|$)') # Bu şekilde daha doğru şekilde alınabilir.

df.to_csv('tweet_data.csv',index=False)

print(df.head(10))
print(df.shape)
# print(df.permalink.value_counts())

print('Sleep...')
time.sleep(60*15) # 15 dakika
