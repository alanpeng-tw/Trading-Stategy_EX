from wsgiref import headers
import pandas as pd
import requests

#加入headers
headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

stock_list_url = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=2" 

html_data = requests.get("https://isin.twse.com.tw/isin/C_public.jsp?strMode=2" ,headers=headers)

#使用panda的read_html處理格式,儲存格式為list[dataframe]
x = pd.read_html(html_data.text)
#print(x)

#確認x的type
#print(type(x))

#確認裡面是否只有一組dataframe
#print(len(x))

#因從pd.read_html所存的型態為list,故取出list裡面的第一個元素
x = x[0]

#查看型態,應該為dataframe
#print(type(x))
#使用pandas的method:iloc 切片,指定為dataframe的欄位為第一列
x.columns = x.iloc[0,:]

#欄位雖然變成了正確的,但原來的那一列仍然存在,故再處理一次將它拿掉
x = x.iloc[1:,:]

#使用to_datetime method將無法轉成datatime的資料轉為Nan
x['上市日'] = pd.to_datetime(x['上市日'], errors='coerce')
#把上市日那個欄位為Nan的那一列資料全drop掉
x = x.dropna(subset=['上市日'])

#將「有價證券代號及名稱」的"有價證券代號"切割出來.append到dataframe的最後一欄,並賦予欄位名稱為"代號"
x['代號'] = x['有價證券代號及名稱'].apply(lambda x: x.split()[0])

#將「有價證券代號及名稱」的"名稱"切割出來.append到dataframe的最後一欄,並賦予欄位名稱為"股票名稱"
x['股票名稱'] = x['有價證券代號及名稱'].apply(lambda x: x.split()[-1])

#Drop 掉不要的欄位
x = x.drop(['有價證券代號及名稱','國際證券辨識號碼(ISIN Code)','CFICode','備註'],axis=1)

#把產業別那個欄位為Nan的那一列資料全drop掉
#沒drop前共28814筆, drop後剩992筆
x = x.dropna(subset=['產業別'])

#str.isdigit() => 都是數字的才要
#dataframe 條件篩選式
x = x[x['代號'].str.isdigit()]

#更換剩餘欄位的順序
x = x[['代號','股票名稱','上市日','市場別','產業別']]

print(x)

#存成excel
x.to_excel(".\stock_list.xlsx")