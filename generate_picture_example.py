import ta
import yfinance as yf
import pandas as pd
import mpl_finance as mpf
import matplotlib.pyplot as plt

#yfinance產出台積電股價資料
stock = yf.Ticker('2330.TW')
#get 20200101-20220922
df = stock.history(start="2020-01-01", end="2022-09-22")



# ===== 呼叫布林通道 =====
indicator_bb = ta.volatility.BollingerBands(close=df["Close"],window=20,window_dev=2)

# ===== 布林中線 =====
df['bbm'] = indicator_bb.bollinger_mavg()
# ===== 布林上線 =====
df['bbh'] = indicator_bb.bollinger_hband()
# ===== 布林下線 =====
df['bbl'] = indicator_bb.bollinger_lband()


################ create a canvas ################
#figsize可以不設, 但default是小小的一張 canvas 
fig = plt.figure(figsize=(24,8))

'''
在畫布上增加區塊
add_subplot() => 一張畫布上只有一個區塊
add_subplot(x,y,z) => 一張畫布上有多個區塊
x:橫向切割成 x 個區塊
y:直向切割成 y 個區塊
z:指定這張圖應該放的位置

以下列圖表為例,假設畫布是 3 x 2 的大小
而台積電的圖要放在 z=1 ,則參數為 add_subplot(3,2,1)
若聯電的圖要放在 z=2 , 則參數為 add_subplot(3,2,2)
----------------
| z=1   | z=2   |
----------------
| z=3   | z=4   |
----------------
| z=5   | z=6   |
----------------
'''

#add_subplot設置為１，並將ax指定為此區塊
ax = fig.add_subplot(1,1,1)


#畫分K , 依序填入開、收、高、低、寬、紅綠K以及透明度
mpf.candlestick2_ochl(ax, df['Open'], df['Close'], df['High'],
    df['Low'], width=0.6, colorup='r', colordown='g',alpha=0.75)



'''
把日期資料放在X軸,使用 set_xticks 來設定刻度
再使用 set_xticklabels 將值依序放到每一個刻度裡
所以設定 set_xticks的大小的值 必須和放到 set_xticklabels 的值數量相同
'''

#設置刻度
'''
df.index:因 yfinance 給的資料日期放在 index, 所以要傳入 index 長度的 range
並每30個資料為一個區間
'''
ax.set_xticks(range(0,len(df.index),30))

#設置刻度's value
#將日期放入刻度內,因刻度是每30個資料為一個區間刻度,故這裡也要每30個資料取一次
#rotation=90 是將X軸的值由橫變直


#因 dataframe 不允許直接對 index 做任何相關運算,故下面的程式會掛掉
#ax.set_xticklabels(df.index[::30].apply(lambda x: x.strftime('%Y-%m-%d')),rotation=90)

#先用DateFrame 將 'Date'的值取出後,再使用lambda做日期的轉換
convert_date = pd.DataFrame(df.index[::30])['Date'].apply(lambda x: x.strftime('%Y-%m-%d'))

ax.set_xticklabels(convert_date,rotation=90,fontsize=6)


#在ax區塊上畫上布林上中下通道
'''
plot() : 畫線
.values : 將 dataframe 轉為 numpy.array 的格式
'''
ax.plot(df['bbm'].values,color='b',label='bbm')
ax.plot(df['bbh'].values,color='g',label='bbh')
ax.plot(df['bbl'].values,color='r',label='bbl')


#設置圖片標題
plt.title(f'2330 Stock Price')
#設置X軸名稱
plt.xlabel('Date')
#設置Y軸名稱
plt.ylabel('Price')
#設置legend才會有label跑出來
plt.legend(loc='best')


plt.show()