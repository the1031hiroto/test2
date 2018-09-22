import numpy as np
import pandas as pd
import pandas as pd
import requests
import json
import sys

"""
#データをURLから取得
df_all = []
url = 'https://baseball-data.com/stats/hitter-all/avg-5.html'
print('取得URL：'+url)
df_hello = pd.io.html.read_html(url)
df_hello = df_hello[0]
df_all.append(df_hello)
#選手IDの作成
name_list = []
dic = {}
for i in range(len(df_all)):
    name_list.extend(df_all[i]['選手名'])
name_list = list(set(name_list))
for i,name in enumerate(name_list):
    dic[name] = i

#選手IDの付与
for i in range(len(df_all)):
    df_all[i]['ID'] = -1
    for j in range(len(df_all[i])):
        df_all[i].loc[j,'ID'] = dic[df_all[i].loc[j,'選手名']]
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
df_all = pd.concat(df_all,axis=1)
df_all.to_csv('data/to_csv_data2.csv')
"""

df_m = pd.read_csv('data/to_csv_data2.csv')
df_m2 = pd.read_csv('data/to_csv_data1.csv')
df_need = df_m2.loc[:,['選手名', '年俸(推定)']]
df_need2 = df_m2.loc[:,['選手名', '年数', '年齢']]
df_marged = pd.merge(df_need, df_m, left_on='選手名', right_on='選手名')
df_marged = pd.merge(df_marged, df_need2, left_on='選手名', right_on='選手名')
"""
df_csv = df_marged.drop('順位', axis=1).drop('ID', axis=1)
df_csv.to_csv('data/to_csv_out2.csv')
print(df_csv)
"""
df_marged = df_marged.replace('万円', '', regex=True).replace(',', '', regex=True).replace('年', '', regex=True).replace('歳', '', regex=True)
df_marged = df_marged.drop('順位', axis=1).drop('チーム', axis=1).drop('RC27', axis=1).drop('XR27', axis=1).drop('ID', axis=1)
#print(df_marged)

df_row = df_marged.drop("選手名", axis=1)
df_row = df_row.astype(float)
data_corr = df_row.corr()
df_corr = pd.DataFrame(data_corr)
df_corr = df_corr.loc['年俸(推定)']
del df_corr['年俸(推定)']

from sklearn import linear_model
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression

mm = preprocessing.MinMaxScaler()
x = df_row.drop("年俸(推定)", axis=1)
X = mm.fit_transform(x)
Y = df_row['年俸(推定)']

linear_regression = LinearRegression()
linear_regression.fit(X,Y)
clf = linear_model.LinearRegression()
# 予測モデルを作成（単回帰）
clf.fit(X, Y)
# 回帰係数と切片の抽出
a = clf.coef_
b = clf.intercept_  
# 回帰係数
print("回帰係数:", a)
print("切片:", b) 
print("決定係数:", clf.score(X, Y))

df_data = pd.DataFrame(x.columns, columns=["column"])
df_data['data'] = pd.DataFrame(linear_regression.coef_)
df_data = df_data.set_index('column')
df_test = pd.concat([df_data, df_corr], axis=1)
df_test = df_test.rename(columns={'data': '回帰係数', '年俸(推定)': '単相関係数'})
print(df_test)

#結果を計算してあってルカ確認
df_x = pd.DataFrame(X)
df_x = df_m.set_index('選手名')
df_x = df_x.T

#正規化した方で計算
X = X[0].T
result2 = X[0] * df_data['data']
print(result2)
result3 = result2.sum(axis=0)
print(result3)
result4 = result3 + b
print(result4)

#回帰係数がマイナスのやつを除いて計算したい
df_data = df_data.drop("試合").drop("打数").drop("打点").drop("四球").drop("出塁率").drop("長打率").drop("併殺打")
df_result = pd.DataFrame(x.T)
df_result = x.drop("試合").drop("打数").drop("打点").drop("四球").drop("出塁率").drop("長打率").drop("併殺打")
#df_result2 = ss.fit_transform(df_result)    ???
#df_result2 = mm.fit_transform(df_result)
#print(df_result)
df_result = df_result[0]
df_test2 = pd.concat([df_data, df_result], axis=1)
df_test2 = df_test2.rename(columns={'data': '回帰係数', 0: '成績'})
#df_test2['成績（正規化）'] = df_result2
print(df_test2)
