import numpy as np
import pandas as pd
import pandas as pd
import requests

#urlをリスト形式で取得
df_all = pd.DataFrame(index=[], columns=[])
yearsSalary = range(1990, 2019, 1)
urlsSalary = []

#URLを入力
for year in yearsSalary:
    urlsSalary.append("https://www.gurazeni.com/perform_batching/avg/year:"+ str(year))

#データをURLから取得
for url in urlsSalary:
    print('取得URL：'+url)
    df_raw = pd.io.html.read_html(url)
    df_m = df_raw[0].drop("チーム", axis=1)
    df_m = df_m.replace('万円', '', regex=True).replace('億円', '0000', regex=True).replace('億', '', regex=True).replace(',', '', regex=True)
    #df_all.append(df_m)
    df_all = pd.concat([df_all, df_m])

print(df_all)
df_all.to_csv('data/data_all.csv')