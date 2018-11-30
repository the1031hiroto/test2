import pandas as pd
import numpy as np
from pandas import Series,DataFrame
from sklearn.datasets import load_boston
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression

boston = load_boston()
boston_df = DataFrame(boston.data)
#カラムに先程のboston.feature_namesを指定します。
boston_df.columns = boston.feature_names
boston_df['PRICE'] = DataFrame(boston.target)
#print(boston_df.head(10))

#インスタンス
linear_regression = LinearRegression()

#説明変数を縦(1)の列と指定して削除します！
X = boston_df.drop("PRICE", 1)

#Yに目的変数を入れます！
Y = boston_df.PRICE
linear_regression.fit(X,Y)
print(linear_regression.coef_)

#print(boston_df.index)
df_calculation = pd.DataFrame(linear_regression.coef_)
print(df_calculation)
