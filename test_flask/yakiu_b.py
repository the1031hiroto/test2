# -*- coding: utf-8 -*-
import numpy
import pandas as pd
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

#df_daritu_low = df_m[['名前', '打率', '年俸']]
#df_daritu_low.sort_values('打率',ascending=False)
df_daritu_low = df_m

print(df_daritu_low.head(20))
list_daritu = df_daritu_low['打率']
list_daritu = list_daritu.values
#test_num1 = 0.310
#l_even = [i for i in list_daritu if i == test_num1]
#print(l_even)

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

@app.route('/form_b/')
def form():
    return render_template('form_b.html') 

@app.route('/daritu')
def daritu():
    num_request = request.args.get('num_daritu')
    num_request = float(num_request)
    num_daritu = getNearestValue(list, num_request)
    df_daritu = df_daritu_low[df_daritu_low['打率'].isin([num_daritu])]
    df_daritu = df_daritu.to_html()
    return str(df_daritu)

if __name__ == '__main__':
    app.run()


