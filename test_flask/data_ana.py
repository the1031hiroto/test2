# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import requests
import json
import sys
#import matplotlib.pylab as plt

df_m = pd.read_csv('data/to_csv_out.csv')
df_m = df_m.replace('万円', '', regex=True).replace('億円', '0000', regex=True).replace('億', '', regex=True)
df_m["年俸"] = df_m["年俸"].str.replace(',', '').astype(float).astype(int)

from sklearn import linear_model
from sklearn.linear_model import LinearRegression

df_test10 = df_m.drop("名前", axis=1)
df_test10 = df_test10.drop("チーム", axis=1)
df_test10 = df_test10[df_test10['打数'] > 100]
df_test10 = df_test10.drop("ID", axis=1)
df_corr = df_test10.corr()
print(df_corr)
#df_corr.to_csv('data/corr1.csv')

X = df_test10.drop("年俸", axis=1)
#正規化
#X = (X - X.min()) / (X.max() - X.min())
X = (X - X.mean()) / X.std(ddof=0)
print(X.head(10))
#X.to_csv('data/nomalyz1.csv')

Y = df_test10['年俸']
#Y = (Y - Y.min()) / (Y.max() - Y.min())
print(Y.head(10))

linear_regression = LinearRegression()
linear_regression.fit(X,Y)

df_data = pd.DataFrame(X.columns, columns=["column"])
df_data['data'] = pd.DataFrame(linear_regression.coef_)

data = pd.read_csv("data/to_csv_out.csv", sep=",")
clf = linear_model.LinearRegression()
# 説明変数に "x1"のデータを使用
X = X.as_matrix()
# 目的変数に "x2"のデータを使用
Y = Y.as_matrix()
# 予測モデルを作成（単回帰）
clf.fit(X, Y)
# 回帰係数と切片の抽出
a = clf.coef_
b = clf.intercept_  
# 回帰係数
print("回帰係数:", a)
print("切片:", b) 
print("決定係数:", clf.score(X, Y))
#df_data['data2'] = pd.DataFrame(a)
df_data = df_data.set_index('column')
print(df_data)

#df_data.to_csv('data/ana2.csv')
print(df_corr.loc['年俸',['安打']])
print(df_data.loc['安打',['data']])
print(df_corr.loc['年俸',['安打']] + df_data.loc['安打',['data']])
df_x = pd.DataFrame(X)
df_x = df_m.set_index('名前')
#print(df_x)
print(df_x.loc['柳田　悠岐',['安打']])
