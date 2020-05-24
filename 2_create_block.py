import pandas as pd
import numpy as np
import tweepy
import glob

glob.glob('./*.csv') # İçinde bulunduğunuz klasördeki .csv uzantılı dosyaları listeler

!python 0_twitter_OAuthHandler.py

df = pd.DataFrame()
# .csv uzantılı dosyaların tamamını okur, tek DataFrame'de birleştirir.
for file_name in glob.glob('*.csv'):
    x = pd.read_csv(file_name, low_memory=False, index_col=False,na_values='NaN')
    df = pd.concat([df,x],axis=0,ignore_index=True)

df = df.drop_duplicates(['tweet_id'])
df.reset_index(inplace=True)
df.drop(['index'], axis = 1, inplace=True)
df.set_index('tweet_id', inplace=True)

df['username'] = df['username'].str.lower()

### Bloklamak istediğiniz hesapları listeye alır;
block_list=list(df['username'].unique())
len(block_list)


blocked = []
i=0
for user in block_list:
    try:
        i +=1
        print(i, '. ', 'username: ', user)
        api.create_block(user)
    except tweepy.TweepError:
        time.sleep(20)
        continue
    blocked.append(user)