import os, sys, time, subprocess
import config
from twitter import *
import pandas as pd

xa = config.CONSUMER_KEY
xb = config.CONSUMER_SECRET
xc = config.ACCESS_TOKEN
xd = config.ACCESS_TOKEN_SECRET

print("検索したいハッシュタグを入力してください。（＃はいりません）")
name = input(">>")
t = Twitter(auth=OAuth(xc, xd, xa, xb))
data = t.search.tweets(q='#' + str(name) + ' -RT', count=100)['statuses']
#print(data.keys())
result = []
for row in data:
    p = row['text']
    # print(p)
    result.append(p)

hashtag_column = []
for i in range(len(result)):
    hashtag_column.append(name)

df = pd.DataFrame({"text":result, "hashtag":hashtag_column})

df.to_csv("data/"+name+".csv")

print(df.head())
