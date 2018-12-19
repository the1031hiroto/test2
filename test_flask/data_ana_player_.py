import numpy as np
import pandas as pd
import pandas as pd
import requests
import json
import sys

#回帰分析
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
#import pandas.tseries.offsets as offsets

df_all = pd.read_csv('data/data_all.csv')
df_all = df_all.drop("Unnamed: 0", axis=1)

df_sort = df_all[df_all['打数'] > 300].sort_values('打数')
print(df_sort.shape)
print(df_sort.head(10))

#回帰分析
df_raw = df_sort
data_corr = df_raw.corr()
df_corr = pd.DataFrame(data_corr)
df_corr = df_corr.loc['年俸(推定)']
del df_corr['年俸(推定)']

mm = preprocessing.MinMaxScaler()
ss = preprocessing.StandardScaler()
x = df_raw.drop("年俸(推定)", axis=1)
#正規化
X = mm.fit_transform(x)
#標準化
#X = ss.fit_transform(x)
print(pd.DataFrame(X).head(10))
Y = df_raw['年俸(推定)']
#print(Y)

linear_regression = LinearRegression()
linear_regression.fit(X,Y)
clf = linear_model.LinearRegression()
# 予測モデルを作成（単回帰）
clf.fit(X, Y)
# 回帰係数と切片の抽出
a = clf.coef_
b = clf.intercept_  
# 回帰係数
#print("回帰係数:", a)
#print("切片:", b) 
print("精度:", clf.score(X, Y))

df_data = pd.DataFrame(x.columns, columns=["column"])
df_data['data'] = pd.DataFrame(linear_regression.coef_)
df_data = df_data.set_index('column')
df_test = pd.concat([df_data, df_corr], axis=1)
df_test = df_test.rename(columns={'data': '回帰係数', '年俸(推定)': '単相関係数'})
#print(df_test)
#df_test.to_csv('data/data_corr_300.csv')

#予測したいデータ
df_calculation = pd.DataFrame(x.columns, columns=["column"]).set_index('column')
df_calculation[2019] = X[0]
#一つにまとめる
df_marged_corr = pd.concat([df_test, df_calculation], axis=1, join_axes=[df_test.index])
#予測を計算
df_marged_corr['result'] = df_marged_corr['回帰係数'] * df_marged_corr['単相関係数'] * df_marged_corr[2019]
print(df_marged_corr)
print(df_marged_corr['result'].sum() + b)
