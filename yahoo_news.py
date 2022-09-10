import requests
from bs4 import BeautifulSoup
import pandas as pd

#加入headers
headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

#指定網址,並帶入headers
data = requests.get("https://tw.stock.yahoo.com/quote/2330/news" ,headers=headers)

#用BeautifulSoup parse html
soup = BeautifulSoup(data.text,features="lxml")


#=====================
#find_all get all
article = soup.find_all('h3',{'class':'Mt(0) Mb(8px)'})


for x in article:
    print(x.text)
    print(x.find('a')['href'])