import numpy
import pandas as pd
#import matplotlib.pylab as plt

#urlをリスト形式で取得
df_all_salary = []
yearsSalary = range(17,9,-1)
urlsSalary = []

#URLを入力：2018年だけ命名規則が違う
urlsSalary.append("https://baseball-data.com/ranking-salary/all/h.html")
for year in yearsSalary:
    urlsSalary.append("https://baseball-data.com/"+ "{0:02d}".format(year)+"/ranking-salary/all/h.html")

#データをURLから取得
for url in urlsSalary:
    #print('取得URL：'+url)
    df_salary = pd.io.html.read_html(url)
    df_salary = df_salary[0].loc[:,['選手名', '年俸(推定)']].replace('万円', '', regex=True)
    df_all_salary.append(df_salary)

df_m_salary = pd.concat(df_all_salary,axis=1)

#urlをリスト形式で取得
df_all = []
years = range(17,9,-1)
urls = []

#URLを入力：2018年だけ命名規則が違う
urls.append("https://baseball-data.com/stats/hitter-all/avg-1.html")
for year in years:
    urls.append("https://baseball-data.com/"+ "{0:02d}".format(year)+"/stats/hitter-all/avg-1.html")

#データをURLから取得
for url in urls:
    #print('取得URL：'+url)
    df = pd.io.html.read_html(url)
    df = df[0]
    df = df.drop('順位', axis=1).drop('チーム', axis=1).drop('RC27', axis=1).drop('XR27', axis=1)
    #df[100:116] = None
    df = df.dropna()
    df_all.append(df)

df_m = pd.concat(df_all,axis=1)

#df_m.to_csv('data/to_csv_tutu_year_all.csv')
#df_m_salary.to_csv('data/to_csv_tutu_year_all_salary.csv')
#print(df_all[0].head(10))
#print(df_all_salary[0].head(10))

df_marged = []
for i in range(0,8,1):
    df_marged.append(pd.merge(df_all_salary[i], df_all[i + 1], left_on='選手名', right_on='選手名'))
    print(df_marged[i][df_marged[i]['選手名'].isin(['筒香　嘉智'])])
print(df_marged[0].head(10))

"""
df_tutu = df_m[df_m['選手名2018'].isin(['筒香　嘉智'])]
print(df_tutu)
df_tutu.to_csv('data/to_csv_tutu_year.csv')

df_csv = df_m
df_csv.to_csv('data/to_csv_out_year.csv')
"""
"""
data = '打率'
data_col = ['選手名2018']
for col in df_m.columns:
    if '打率' in col:
        data_col.append(col)
df_m = pd.concat(df_all,axis=1)
df_m = df_m.sort_values('打率2018',ascending=False)
df_m = df_m[data_col]
print(df_m.head(20))
"""

#df_test = df_m[['選手名2018', '勝利2018']]

#datatest = datatest.dropna(axis=1)
#if datatest = 6:
    #print(datatest)
#print(datatest['6.0':'9.0'])

#df2 = df_m.copy()
#df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
#print(df2.head(20))

#df_test = df_test[df_m['勝利2018'].isin(['6.0'])]
#print(df_test)
#df_test = df_m[df_m['選手名2018'].isin(['菅野　智之'])]
#print(df_test)

#print(df_test['ID','選手名2018','勝利2018'])
#df_test2 = del df_test['勝利2009']