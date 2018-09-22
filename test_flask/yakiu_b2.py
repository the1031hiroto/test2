# -*- coding: utf-8 -*-
import numpy
import pandas as pd
import requests
import json
import sys
import sqlite3
from contextlib import closing
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

df_m = pd.concat(df_all,axis=1)

df_dic = df_m.to_dict(orient='records')
df_daritu_low = df_m
df_hello = df_m.values

"""
df_daritu_low = df_m[['名前', '打率', '年俸']]
df_daritu_low.sort_values('打率',ascending=False)
df_test = df_m[0:10]
df_test = df_test.reset_index().T.reset_index().T.values.tolist()
print(df_test)
df_dic = df_dic[0:20]
"""

"""
dbname = 'database2.db'

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()

    # executeメソッドでSQL文を実行する
    create_table = '''create table users (id int, 名前 int, チーム, 年俸, 打率, 打数, 安打, 打点, 本塁打, 二塁打, 三塁打, 四球, 死球, 三振, 盗塁)'''
    c.execute(create_table)

    # SQL文に値をセットする場合は，Pythonのformatメソッドなどは使わずに，
    # セットしたい場所に?を記述し，executeメソッドの第2引数に?に当てはめる値を
    # タプルで渡す．
    sql = 'insert into users (id, 名前, チーム, 年俸, 打率, 打数, 安打, 打点, 本塁打, 二塁打, 三塁打, 四球, 死球, 三振, 盗塁) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
    user = (264, '柳田\u3000悠岐', 'ソフトバンク', '5億5000万円', 0.345, 351, 121, 70, 25, 20, 4, 42, 3, 80, 18)
    c.execute(sql, user)

    # 一度に複数のSQL文を実行したいときは，タプルのリストを作成した上で
    # executemanyメソッドを実行する
    insert_sql = 'insert into users (id, 名前, チーム, 年俸, 打率, 打数, 安打, 打点, 本塁打, 二塁打, 三塁打, 四球, 死球, 三振, 盗塁) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
    users = [['ID', '名前', 'チーム', '年俸', '打率', '打数', '安打', '打点', '本塁打', '二塁打', '三塁打', '四球', '死球', '三振', '盗塁'], [246, '柳田\u3000悠岐', 'ソフトバンク', '5億5000万円', 0.345, 351, 121, 70, 25, 20, 4, 42, 3, 80, 18], [440, '近藤\u3000健介', '日本ハム', '5600万円', 0.33399999999999996, 320, 107, 53, 9, 26, 3, 65, 1, 63, 4], [317, '平田\u3000良介', '中日','1億2000万円', 0.33299999999999996, 351, 117, 42, 6, 18, 4, 46, 3, 53, 8], [294, 'ダヤン・ビシエド', '中日', '1億7000万円', 0.331, 372, 123, 72, 17, 23, 1, 41, 11, 47, 1], [474, '鈴木\u3000誠也', '広島', '9000万円', 0.32899999999999996, 280, 92, 69, 22, 23, 0, 59, 4, 74, 4], [69, '坂本\u3000勇人', '巨人', '3億5000万円', 0.32799999999999996, 326, 107, 56, 13, 18, 2, 50, 0, 65, 8], [502, '宮崎\u3000敏郎', 'DeNA', '8000万円', 0.32799999999999996, 399, 131, 55, 20, 30, 0, 24, 0, 34, 0], [394, '秋山\u3000翔吾', '西武', '2億2000万円', 0.327, 431, 141, 56, 16, 30, 7, 57, 4, 73, 10], [279, '山田\u3000哲人', 'ヤクルト', '2億8000万円', 0.321, 377, 121, 69, 28, 17, 3, 74, 2, 84, 27], [482, '丸\u3000佳浩', '広島', '2億1000万円', 0.319, 279, 89,61, 25, 17, 0, 90, 2, 79, 8]]
    c.executemany(insert_sql, users)
    conn.commit()

    select_sql = 'select * from users'
    for row in c.execute(select_sql):
        print(row)
"""

list_daritu = df_daritu_low['打率']
list_daritu = list_daritu.values
#print(list_daritu[0])

list_honrui = df_m['本塁打']
#print(list_honrui)
list_honrui = list_honrui.values

import numpy as np

def getNearestValue(list, num):
    """
    概要: リストからある値に最も近い値を返却する関数
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    """

    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    idx = np.abs(np.asarray(list) - num).argmin()
    return list[idx]


if __name__ == "__main__":

    list = list_daritu
    test_num = 0.30
    num_daritu = getNearestValue(list, test_num)
    print(num_daritu)

from flask import Flask,render_template, render_template, request 
app = Flask(__name__)

@app.route('/')
def test():
    
    if request.args.get('num_daritu') and request.args.get('num_honrui'):
        num_request = request.args.get('num_daritu')
        num_request = float(num_request)
        num_daritu = getNearestValue(list, num_request)
        high_num = num_daritu - 0.005
        low_num = num_daritu + 0.005
        l_daritu = [i for i in list_daritu if (i > high_num) and (i < low_num)]
        df_daritu = df_daritu_low[df_daritu_low['打率'].isin(l_daritu)]

        h_num = request.args.get('num_honrui')
        h_num = int(h_num)
        h_high = h_num + 7
        h_low = h_num - 7
        l_honrui = [i for i in list_honrui if (i > h_low) and (i < h_high)]
        df_daritu = df_daritu[df_daritu['本塁打'].isin(l_honrui)]
        df_daritu = df_daritu.to_html()
        return render_template("index2.html", df_daritu=df_daritu, num_request=num_request, num_honrui=h_num)
    else:
        return render_template("index2.html", num_request="未入力", num_honrui="未入力")    

@app.route('/form_b/')
def form():
    return render_template('form_b.html') 

@app.route('/test/')
def test2():
    test= "Hello world"
    python_data = {
    'some_list': [4, 5, 6],
    'nested_dict': {'foo': 7, 'bar': 'a string'}
    }
    data1 = df_dic
    return render_template('index.html', data1=data1, df_m=df_m, test=python_data, python_data=python_data ) 

@app.route('/test2/')
def test3():
    test= "Hello world"
    return render_template('index3.html', test=test ) 

@app.route('/daritu')
def daritu():
    if request.args.get('num_daritu') and request.args.get('num_honrui'):
        num_request = request.args.get('num_daritu')
        num_request = float(num_request)
        num_daritu = getNearestValue(list, num_request)
        high_num = num_daritu - 0.005
        low_num = num_daritu + 0.005
        l_daritu = [i for i in list_daritu if (i > high_num) and (i < low_num)]
        df_daritu = df_daritu_low[df_daritu_low['打率'].isin(l_daritu)]

        h_num = request.args.get('num_honrui')
        h_num = int(h_num)
        h_high = h_num + 7
        h_low = h_num - 7
        l_honrui = [i for i in list_honrui if (i > h_low) and (i < h_high)]
        df_daritu = df_daritu[df_daritu['本塁打'].isin(l_honrui)]
        
        df_daritu = df_daritu.to_html()
        return render_template("index.html", df_daritu=df_daritu, num_request=num_request, num_honrui=h_num)
    else:
        df_daritu = df_daritu.to_html()
        return render_template("index.html", df_daritu=0, num_request=0, num_honrui=0)

if __name__ == '__main__':
    app.run()


