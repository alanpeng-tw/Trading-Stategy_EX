import pandas as pd
import yfinance as yf
import openpyxl

#yfinance產出台積電股價資料
stock = yf.Ticker('2330.TW')
#get 20170101-20210202
df = stock.history(start="2017-01-01", end="2021-02-02")


#rolling以6為單位為移並取最大值
Highest_high = df['High'].rolling(6).max()
#print(Highest_high)

#rolling以6為單位為移並取最小值
Lowest_low = df['Low'].rolling(6).min()
#print("Lowest_low:\n",Lowest_low)

#rolling以6為單位為移並將第一筆減去最後一筆(6個單位的最低價-最高價)取高低的落差
O_C_high = df['High'].rolling(6).apply(lambda x: x[0] -x[-1])
df['O_C_high'] = O_C_high

#save Highest_high & Lowest_low to Excel file
df.to_excel(r'D:\python-workspace\Trading-Stategy_EX\final.xlsx')