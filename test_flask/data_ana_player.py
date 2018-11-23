import numpy as np
import pandas as pd
import pandas as pd
import requests
import json
import sys
import sqlite3
import pandas.io.sql as psql
#import pandas.tseries.offsets as offsets

# sqlite3に接続
con = sqlite3.connect("data.db")
cur = con.cursor()

# サンプルテーブルを作成
cur.execute('CREATE TABLE IF NOT EXISTS tut5  (年俸"（"推定"）" int, 打率 int, 打数 int, 安打 int, 打点 int, 本塁打 int, 三振 int, 盗塁 int, 四死球 int, 年棒"("変化")" int)')
#cur.execute('CREATE TABLE IF NOT EXISTS https://www.gurazeni.com/player/420 (年俸"（"推定"）" int, 打率 int, 打数 int, 安打 int, 打点 int, 本塁打 int, 三振 int, 盗塁 int, 四死球 int, 年棒"("変化")" int)')
#cur.execute('CREATE TABLE IF NOT EXISTS https://www.gurazeni.com/player/421 (年俸"（"推定"）" int, 打率 int, 打数 int, 安打 int, 打点 int, 本塁打 int, 三振 int, 盗塁 int, 四死球 int, 年棒"("変化")" int)')

#urlをリスト形式で取得
df_all = []
yearsSalary = range(420, 422, 1)
urlsSalary = []

#URLを入力
for year in yearsSalary:
    urlsSalary.append("https://www.gurazeni.com/player/"+ str(year))

#データをURLから取得
for url in urlsSalary:
    print('取得URL：'+url)
    df_raw = pd.io.html.read_html(url)
    df_salary = df_raw[1].drop("チーム", axis=1).drop("背番号", axis=1).replace('年', '', regex=True)

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

    df_record = df_raw[2].drop("二塁打", axis=1).drop("三塁打", axis=1).replace('年', '', regex=True)
    df_record['安打'] = df_record['安打'] - df_record['本塁打']
    df_record['四死球'] = df_record['四球'] + df_record['死球']
    df_record = df_record.drop("四球", axis=1).drop("死球", axis=1)
    reindex =[]    
    for i in range(int(df_record[0:1]['年']) + 1, int(df_record[0:1]['年']) - int(len(df_record)) + 1, -1):
        reindex.append(i)
    #print(reindex)
    df_record['reindex'] = reindex
    df_record = df_record.drop("年", axis=1).set_index('reindex')

    #print(df_record)

    df_marged = pd.concat([df_all_info, df_record], axis=1, join_axes=[df_all_info.index])
    df_marged = df_marged.replace('万円', '', regex=True).replace('億円', '0000', regex=True).replace('億', '', regex=True).replace(',', '', regex=True)

    l = ['X2']
    for i in range(0,int(len(df_marged)) - 2,1):
        l.append(int(df_marged.iat[i+1, 0]) - int(df_marged.iat[i+2, 0]))
    l.append(None)
    df_marged['年棒（変化）'] = l

    #df_marged.to_sql('tutu5', con, if_exists='append', index=None)
    #変化率 print(df_marged.diff())
    #df['date'] = pd.to_datetime(df['date'])
    #print(df['date'].dtype)
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
#df_sql = psql.read_sql("SELECT * FROM tutu5", con)
#print(df_sql)


# サンプルテーブルを作成
#cur.execute('CREATE TABLE tut4  (年俸"（"推定"）" int, 打率 int, 打数 int, 安打 int, 打点 int, 本塁打 int, 三振 int, 盗塁 int, 四死球 int, 年棒"("変化")" int)')
"""
# サンプルデータを挿入
cur.execute('insert into articles  values (1, "sample1", "AAAA", "2017-07-14 00:00:00")')
cur.execute('insert into articles  values (2, "sample2", "BBBB", "2017-07-15 00:00:00")')

# Select文からDataFrameを作成
df_sql = psql.read_sql("SELECT * FROM articles;", con)

# Dataframeをsqlに保存
df_sql2 = pd.DataFrame([['sample3', 'CCC', '2017-07-16 00:00:00']], columns=['title', 'body', 'created'], index=[2])
"""
#df_marged.to_sql('tutu4', con, if_exists='append', index=None)
#df_sql = psql.read_sql("SELECT * FROM tutu4;", con)
#print(df_sql)
