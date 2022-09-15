
import yfinance as yf
import ta

'''
此程式示範如何用 ta 一次性產生42種技術指標
'''

#先取得2330 2017/01/01 ~ 2022/09/30 的股價資料
stock = yf.Ticker('2330.TW')
df = stock.history(start="2017-01-01",end="2022-09-30")

#add_all_ta_teatures => 呼叫出所有的技術指標
data = ta.add_all_ta_features(df,"Open", "High","Low","Close","Volume",fillna=True)
#print(data)


#SMA(Simple Moving Average) 移動平均線
#取得SMA's Object
ma = ta.trend.SMAIndicator(df['Close'],10,fillna=True)

ma = ma.sma_indicator()
print(ma)
