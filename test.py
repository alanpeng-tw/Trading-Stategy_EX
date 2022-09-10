import yahoo_finance as yf

stock_list = {'2330.TW','2317.TW','2324.TW'}

for x in stock_list:
    price = yf.stock_price(x)

    print('股票:',x,' | 價格:',price)