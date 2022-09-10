import requests
from bs4 import BeautifulSoup


def stock_price(stock:str):
    #加入headers
    headers = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }

    #對網站進行requests, 並加入指定的headers
    #用f-string方法
    data = requests.get(f"https://finance.yahoo.com/quote/{stock}?p={stock}",headers=headers)

    #use BeautifulSoup parse html
    soup = BeautifulSoup(data.text,features="lxml")


    #use find get element
    #尋找單一的tag : soup.find( tag, {class: class name})
    #如果page中有許多相同的tag或要尋找相同的tag時 , 就要用 find_all
    price = soup.find('fin-streamer', {'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)'})
    
    return price.text