import numpy as np
import pandas as pd
import pandas as pd
import requests
import json
import sys
#hello

#データをURLから取得
df_all = []
url = 'https://www.gurazeni.com/player/420'
print('取得URL：'+url)
df_hello = pd.io.html.read_html(url)
df1 = df_hello[1].drop("チーム", axis=1).drop("背番号", axis=1)
df2 = df_hello[2].drop("打率", axis=1).drop("二塁打", axis=1).drop("三塁打", axis=1)
df2['安打'] = df2['安打'] - df2['本塁打']
df2['四死球'] = df2['四球'] + df2['死球']
df2 = df2.drop("四球", axis=1).drop("死球", axis=1)
df_marged = pd.merge(df1, df2, left_on='年', right_on='年')
df_marged = df_marged.replace('万円', '', regex=True).replace(',', '', regex=True).replace('年', '', regex=True)
print(df_marged)
"""
#scvで出力
df_all = pd.concat(df_all,axis=1)
df_all.to_csv('data/to_csv_data2.csv')


df_m = pd.read_csv('data/to_csv_data2.csv')
df_m2 = pd.read_csv('data/to_csv_data1.csv')
df_need = df_m2.loc[:,['選手名', '年俸(推定)']]
df_need2 = df_m2.loc[:,['選手名', '年数', '年齢']]
df_marged = pd.merge(df_need, df_m, left_on='選手名', right_on='選手名')
df_marged = pd.merge(df_marged, df_need2, left_on='選手名', right_on='選手名')

df_csv = df_marged.drop('順位', axis=1).drop('ID', axis=1)
df_csv.to_csv('data/to_csv_out2.csv')
print(df_csv)

df_marged = df_marged.replace('万円', '', regex=True).replace(',', '', regex=True).replace('年', '', regex=True).replace('歳', '', regex=True)
df_marged = df_marged.drop('順位', axis=1).drop('チーム', axis=1).drop('RC27', axis=1).drop('XR27', axis=1).drop('ID', axis=1)
df_marged = df_marged.drop("打率", axis=1).drop("試合", axis=1).drop("打席数", axis=1).drop("出塁率", axis=1).drop("長打率", axis=1).drop("OPS", axis=1)
df_marged['四死球'] = df_marged['四球'] + df_marged['死球']
df_marged = df_marged.drop("四球", axis=1).drop("死球", axis=1)
df_marged['安打'] = df_marged['安打'] - df_marged['本塁打']
df_marged = df_marged.sort_values('打数', ascending=False)

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
print(pd.DataFrame(X))

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

#正規化した方で計算
X = X[0].T
result2 = X[0] * df_data['data']
print(result2)
result3 = result2.sum(axis=0)
print(result3)
result4 = result3 + b
print(result4)
print(Y[0])


#回帰係数がマイナスのやつを除いて計算したい
df_data = df_data.drop("試合").drop("打数").drop("打点").drop("四球").drop("出塁率").drop("長打率").drop("併殺打")
df_result = pd.DataFrame(x.T)
#df_result = x.drop("試合").drop("打数").drop("打点").drop("四球").drop("出塁率").drop("長打率").drop("併殺打")
#df_result2 = ss.fit_transform(df_result)    ???
#df_result2 = mm.fit_transform(df_result)
#print(df_result)
df_result = df_result[0]
df_test2 = pd.concat([df_data, df_result], axis=1)
df_test2 = df_test2.rename(columns={'data': '回帰係数', 0: '成績'})
#df_test2['成績（正規化）'] = df_result2
#print(df_test2)

"""