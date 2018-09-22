# -*- coding: utf-8 -*-
import numpy
import pandas as pd
#import matplotlib.pylab as plt

#urlをリスト形式で取得
df_all = []
urls = []

#データをURLから取得
urls.append('https://baseball-data.com/stats/pitcher-all/win-2.html')
urls.append('https://baseball-data.com/ranking-salary/all/p.html')

for url in urls:
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

#カラム名に年を付ける
#for i in range(len(df_all)):
 #   for col_name in df_all[i].columns:
  #      df_all[i] = df_all[i].rename(columns = {col_name:col_name+"20"+"{0:02d}".format(years[i])})

df_m = pd.concat(df_all,axis=1)
#print(df_m)
df_test = df_m[['選手名', '勝利', '年俸(推定)']]
df_test = pd.concat(df_all,axis=1)
df_test.sort_values('年俸(推定)',ascending=False)
#print(df_test)
#print(df_test.head(20))

data = '勝利'
data_col = ['選手名', '年俸(推定)']
for col in df_m.columns:
    if '勝利' in col:
        data_col.append(col)
df_m = pd.concat(df_all,axis=1)
df_m = df_m.sort_values('勝利',ascending=False)
df_m = df_m[data_col]
top20 = df_m.head(20)

print(top20)
top20 = top20.to_html()
num_win = 6.0
df_m_win = df_m[df_m['勝利'].isin([num_win])]
print(df_m_win)
df_m_win = df_m_win.to_html()


from flask import Flask,render_template, render_template, request 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return str(df_m_win)

@app.route('/form/')
def form():
    return render_template('form.html') 

@app.route('/num_win')
def num_win():
    num_win = request.args.get('num_win')
    df_win = df_m[df_m['勝利'].isin([num_win])]
    df_win = df_win.to_html()
    return str(df_win)

if __name__ == '__main__':
    app.run()


