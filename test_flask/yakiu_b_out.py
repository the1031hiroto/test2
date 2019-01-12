# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import requests
import json
import sys
#import matplotlib.pylab as plt

#urlをリスト形式で取得
df_all = []
urls = []

#データをURLから取得
urls.append('https://www.gurazeni.com/perform_batching/avg/year:2018')

for url in urls:
    print('取得URL：'+url)
    df_hello = pd.io.html.read_html(url)
    df_hello = df_hello[0]
    df_all.append(df_hello)

#選手IDの作成
name_list = []
dic = {}
for i in range(len(df_all)):
    name_list.extend(df_all[i]['名前'])
name_list = list(set(name_list))
for i,name in enumerate(name_list):
    dic[name] = i

#選手IDの付与
for i in range(len(df_all)):
    df_all[i]['ID'] = -1
    for j in range(len(df_all[i])):
        df_all[i].loc[j,'ID'] = dic[df_all[i].loc[j,'名前']]
    df_all[i].index = df_all[i]['ID']
    df_all[i] = df_all[i].drop('ID',axis=1)

#index被りを除去
for i in range(len(df_all)):
    doubled_index = []
    count = df_all[i].index.value_counts()
    for j in count.index:
        if(count.loc[j]>1):
            doubled_index.append(j)
    df_all[i] = df_all[i].drop(doubled_index)

#scvで出力
df_m = pd.concat(df_all,axis=1)

"""
path = 'data/to_json_out.json'
df_m.to_json(path)

df_m.to_csv('data/to_csv_out.tsv', sep='\t')
df_m.to_csv('data/to_csv_out.csv')

#jsonで出力
import json
from collections import OrderedDict
import pprint

df_m_json = df_m.to_json()
with open('data/test2.json', 'w') as f:
    json.dump(df_m_json, f, indent=4)
"""
df_m_grouped = df_m.groupby('チーム').mean()
print(df_m_grouped)
#df_m_grouped = pd.concat(df_m_grouped,axis=1)
#df_m_grouped.to_csv('data/to_csv_out.tsv', sep='\t')
#df_m_grouped.to_csv('data/to_csv_out.csv')