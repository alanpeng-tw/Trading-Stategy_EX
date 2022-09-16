
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
#print(ma)


#呼叫布林通道
indicator_bb = ta.volatility.BollingerBands(close=df['Close'],window=20,window_dev=2)
#布林中線
bb_bbm = indicator_bb.bollinger_mavg()
#布林上線
bb_bbh = indicator_bb.bollinger_hband()
#布林下線
bb_bbl = indicator_bb.bollinger_lband()

print('布林中線\n',bb_bbm)


#返回close是否大於布林上軌, true = 1 , false = 0
bb_bbhi = indicator_bb.bollinger_hband_indicator()
#返回close是否大於布林下軌, true = 1 , false = 0
bb_bbli = indicator_bb.bollinger_lband_indicator()
#布林帶寬
bb_bbw = indicator_bb.bollinger_wband()
#布林%b指標(%b值 = (收盤價 布林帶下軌值) / ( 布林帶上軌值 布林帶下軌值))
bb_bbp = indicator_bb.bollinger_pband()