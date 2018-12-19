import numpy
import pandas as pd
#import matplotlib.pylab as plt

#urlをリスト形式で取得
df_all = []
years = range(18,8,-1)
urls = []

#URLを入力：2017年だけ命名規則が違う
for year in years:
    urls.append('https://www.gurazeni.com/perform_batching/avg/year:'+ "{0:02d}".format(year))

#データをURLから取得
for url in urls:
    print('取得URL：'+url)
    df = pd.io.html.read_html(url)
    df = df[0]
    df_all.append(df)

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

#カラム名に年を付ける
for i in range(len(df_all)):
    for col_name in df_all[i].columns:
        df_all[i] = df_all[i].rename(columns = {col_name:col_name+"20"+"{0:02d}".format(years[i])})

df_m = pd.concat(df_all,axis=1)

data = '打率'
data_col = ['名前2018']
for col in df_m.columns:
    if '打率' in col:
        data_col.append(col)
df_m = pd.concat(df_all,axis=1)
df_m = df_m.sort_values('打率2018',ascending=False)
df_m = df_m[data_col]
df_m.head(20)

print(df_m.head(20))

#df_test = df_m[['名前2018', '勝利2018']]

#datatest = datatest.dropna(axis=1)
#if datatest = 6:
    #print(datatest)
#print(datatest['6.0':'9.0'])

#df2 = df_m.copy()
#df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
#print(df2.head(20))

#df_test = df_test[df_m['勝利2018'].isin(['6.0'])]
#print(df_test)
#df_test = df_m[df_m['名前2018'].isin(['菅野　智之'])]
#print(df_test)

#print(df_test['ID','名前2018','勝利2018'])
#df_test2 = del df_test['勝利2009']