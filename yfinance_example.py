import yfinance as yf


stock = yf.Ticker("2330.Tw")

'''呼叫歷史資料
start&end為指定區間,period="max"為全部區間
'''
stock.history

# 取得yahoo所擁有的指定股票的所有歷史資料
'''
hist = stock.history(period="max")
print(hist)
'''

#取得指定區間的歷史股價
'''
df = stock.history(start="2022-01-01",end="2022-09-30")
print(df)
'''

# get stock info(股票基本資訊)
stock.info

#獲取主要持有人
stock.major_holders

#主要持有之機構法人
stock.institutional_holders

#取得損益表
stock.financials

#取得資產負債表
stock.balance_sheet

#取得流量表
stock.cashflow

#分析師建議(僅有美股資料)
stock.recommendations