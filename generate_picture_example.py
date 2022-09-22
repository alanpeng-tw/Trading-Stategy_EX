import ta
import yfinance as yf
import pandas as pd
import mpl_finance as mpf
import matplotlib.pyplot as plt

#yfinance產出台積電股價資料
stock = yf.Ticker('2330.TW')
#get 20200101-20220922
df = stock.history(start="2020-01-01", end="2022-09-22")


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
'''
ax.set_xticks(range(len(df.index)))

#設置刻度's value
#將日期放入刻度內
ax.set_xticklabels(df.index)



#設置圖片標題
plt.title(f'2330 Stock Price')
#設置X軸名稱
plt.xlabel('Date')
#設置Y軸名稱
plt.ylabel('Price')



plt.show()