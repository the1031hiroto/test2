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

#urlをリスト形式で取得
df_all = pd.DataFrame(index=[], columns=[])
yearsSalary = range(1286, 1649, 1)
#yearsSalary = range(54, 57, 1)
urlsSalary = []

#URLを入力
for year in yearsSalary:
    urlsSalary.append("https://www.gurazeni.com/player/"+ str(year))

#データをURLから取得
for url in urlsSalary:
    print('取得URL：'+url)
    df_raw = pd.io.html.read_html(url)
    if len(df_raw) >= 3 and (df_raw[0].iat[1,3] == '内野手' or df_raw[0].iat[1,3] == '外野手' or df_raw[0].iat[1,3] == '捕手'):
        df_salary = df_raw[1].drop("チーム", axis=1).drop("背番号", axis=1).replace('年', '', regex=True)
        df_salary = df_salary.replace('万円', '', regex=True).replace('億円', '0000', regex=True).replace('億', '', regex=True).replace(',', '', regex=True)

        #最終年から期間を作成
        reindex =[]    
        for i in range(int(df_salary[0:1]['年']) + 1, int(df_salary[0:1]['年']) - int(len(df_salary)) + 1, -1):
            reindex.append(i)
        df_salary['reindex'] = reindex
        df_salary = df_salary.drop("年", axis=1).set_index('reindex')
        #最新年に空を追加　※この空のとこを予想したい
        df_salary = df_salary.shift()
        #print(df_salary)

        df_all_info = df_salary
        #print(df_all_info)

        #df_record = df_raw[2].replace('年', '', regex=True)
        df_record = df_raw[2].drop("二塁打", axis=1).drop("三塁打", axis=1).replace('年', '', regex=True)
        df_record['安打'] = df_record['安打'] - df_record['本塁打']
        df_record['四死球'] = df_record['四球'] + df_record['死球']
        df_record = df_record.drop("四球", axis=1).drop("死球", axis=1)

        reindex =[]
        last_year = int(df_record[0:1]['年']) - int(len(df_record)) + 1
        for i in range(int(df_record[0:1]['年']) + 1, last_year, -1):
            reindex.append(i)
        df_record['reindex'] = reindex
        df_record = df_record.drop("年", axis=1).set_index('reindex')

        #df_record['年'] = df_record['年'].astype(int)
        #df_record = df_record.set_index('年')
        #df_record = df_record.shift()
        df_record.loc[last_year] = None
        #print(df_record)

        df_marged = pd.concat([df_all_info, df_record], axis=1, join_axes=[df_all_info.index])
        """
        #diff使えよ https://note.nkmk.me/python-pandas-diff-pct-change/
        l = [None]
        for i in range(0,int(len(df_marged)) - 2,1):
            l.append(int(df_marged.iat[i+1, 0]) - int(df_marged.iat[i+2, 0]))
        l.append(None)
        df_marged['年棒（変化）'] = l
        """
        #df_marged.to_sql('tutu5', con, if_exists='append', index=None)
        #変化率 print(df_marged.diff())
        #df['date'] = pd.to_datetime(df['date'])
        #print(df['date'].dtype)

        df_all = pd.concat([df_all, df_marged.dropna()])

#df_all1 = pd.concat([df_all[0], df_all[1]]).dropna()
df_all = df_all.reset_index()
#df_all.to_csv('data/data_all3.csv')
print(df_all)
"""
    #回帰分析
    df_raw = df_marged.drop([2020,2019,2011]).drop("年棒（変化）", axis=1).astype(float)
    data_corr = df_raw.corr()
    df_corr = pd.DataFrame(data_corr)
    df_corr = df_corr.loc['年俸(推定)']
    del df_corr['年俸(推定)']

    mm = preprocessing.MinMaxScaler()
    x = df_raw.drop("年俸(推定)", axis=1)
    #正規化
    X = mm.fit_transform(x)
    Y = df_raw['年俸(推定)']
    print(pd.DataFrame(X))
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
    #print("決定係数:", clf.score(X, Y))

    df_data = pd.DataFrame(x.columns, columns=["column"])
    df_data['data'] = pd.DataFrame(linear_regression.coef_)
    df_data = df_data.set_index('column')
    df_test = pd.concat([df_data, df_corr], axis=1)
    df_test = df_test.rename(columns={'data': '回帰係数', '年俸(推定)': '単相関係数'})
    #予測したい年のデータ
    data_for_calculation = mm.fit_transform(df_marged.drop([2020,2011]).drop("年俸(推定)", axis=1).drop("年棒（変化）", axis=1))
    df_calculation = pd.DataFrame(x.columns, columns=["column"]).set_index('column')
    df_calculation[2019] = data_for_calculation[0]
    #一つにまとめる
    df_marged_corr = pd.concat([df_test, df_calculation], axis=1, join_axes=[df_test.index])
    #予測を計算
    df_marged_corr['result'] = df_marged_corr['回帰係数'] * df_marged_corr['単相関係数'] * df_marged_corr[2019]
    print(df_marged_corr)
    print(df_marged_corr['result'].sum() + 1600)
"""
"""
    #scvで出力
    name = url.replace('https://www.gurazeni.com/player/', '')
    print(name)
    df_marged.to_csv('data/' + name + '.csv')

    df_test = df_marged.as_matrix()
    print(df_test)
    df_all.append(df_test)

print(df_all)
df_m = pd.DataFrame(df_all)
print(df_m)
"""

