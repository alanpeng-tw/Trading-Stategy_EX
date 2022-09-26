import ta
import yfinance as yf
import pandas as pd
import mpl_finance as mpf
import matplotlib.pyplot as plt


'''
畫K線圖及成交量圖的邏輯

1.定義畫布(plt.figure)
2.定義模板(plt.GridSpec(3,20)) - 如有需多張大小不一的圖片,無需要可省略
3.依照模板定義具備不同大小的區塊(fig.add_subplot(grid[0:2,1:]))
  or 定義大小均等的區塊(fig.add_subplot(grid[2,1,1]))
4.在定義出的區塊自由揮灑
'''



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
#ax = fig.add_subplot(1,1,1)

#定義模板大小: 3*20
grid = plt.GridSpec(3,20)

#區塊1畫主圖,給主圖2格block,並在左方保留一格block
ax = fig.add_subplot(grid[0:2,1:])
'''
------------------------
|    | z   | z   | z   |
------------------------
|    | z   | z   | z   |
------------------------
|    |     |     |     |
------------------------
'''


#區塊2畫子圖,給子圖1格block,並在左方保留一格block
ax2 = fig.add_subplot(grid[2:,1:])
'''
------------------------
|    |     |     |     |
------------------------
|    |     |     |     |
------------------------
|    | z   | z   | z   |
------------------------
'''


#畫分K , 依序填入開、收、高、低、寬、紅綠K以及透明度
mpf.candlestick2_ochl(ax, df['Open'], df['Close'], df['High'],
    df['Low'], width=0.6, colorup='r', colordown='g',alpha=0.75)


#使用 mpl_volume_overlay 畫出量,並將之畫在區塊 ax2 
mpf.volume_overlay(ax2, df['Open'], df['Close'], df['Volume'], colorup='r', colordown='g')

#先用DateFrame 將 'Date'的值取出後,再使用lambda做日期的轉換
convert_date = pd.DataFrame(df.index[::30])['Date'].apply(lambda x: x.strftime('%Y-%m-%d'))


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

ax.set_xticklabels(convert_date,rotation=90,fontsize=6)


#在ax區塊上畫上布林上中下通道
'''
plot() : 畫線
.values : 將 dataframe 轉為 numpy.array 的格式
'''
ax.plot(df['bbm'].values,color='b',label='bbm', linestyle="--")
ax.plot(df['bbh'].values,color='g',label='bbh', linestyle="--")
ax.plot(df['bbl'].values,color='r',label='bbl', linestyle="--")


#設置區塊2的刻度
ax2.set_xticks(range(0,len(df.index),30))
#設置區塊2的刻度的值
ax2.set_xticklabels(convert_date,rotation=90,fontsize=6)


#設置圖片標題
ax.set_title(f'2330 Stock Price')
#設置X軸名稱
ax.set_xlabel('Date')
#設置Y軸名稱
ax.set_ylabel('Price')

#防止圖片重疊
fig.tight_layout()

#設置legend才會有label跑出來
#ax.legend(loc='best')
ax.legend()

#儲存圖檔為png
plt.savefig('test.png')

plt.show()