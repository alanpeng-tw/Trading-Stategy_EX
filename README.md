
#作者的github : https://github.com/arleigh418/python-and-Taiwan-stock-market

#download github project
	git clone https://github.com/alanpeng-tw/Trading-Stategy_EX.git


#first time to push project
	git status

	git add file_name

	git commit -m "xxxxx"

	git push origin main


#第二次的push file to github前,都要先pull , 然後再做add、commit、push

	git status

	git pull origin main

	git commit -m "xxxxx"

	git push origin main




# Trading-Stategy_EX

「Python金融市場賺大錢聖經：寫出你的專屬指標」一書的自我筆記及練習

1.安裝python

2.設定python  path

3.安裝vscode

4.在vscode下載python的拓展包

5.開發小習慣-虛擬環境
	在開發的目錄中開啟console
	enter command => python -m venv env
	
	上述的command 會在該目錄建立一個 env的目錄
	開啟虛擬環境: D:\PythonProjects\FinTech\Trading Stategy_EX\env\Scripts\activate
	關閉虛擬環境: D:\PythonProjects\FinTech\Trading Stategy_EX\env\Scripts\deactivate
	
	如console 命令列的最前面出現(env) , 則代表現處於虛擬環境上
	pip list => 確認無下載任何套件
	
	回到放置requirment.txt的folder,
	pip install -r requirment.txt

6.在虛擬環境安裝python套件
	
	pip install pandas
	pip install requests
	pip install beautifulsoup4
	pip install lxml
	pip install openpyxl
	pip install yfinance
	pip install ta
	pip install mpl_finance
	
	===經常使用的 pip command ===
	#解除套件
	pip uninstall pandas
	
	#指定安裝版本
	pip install pandas==1.2.1
	
	#列出用pip安裝的套件
	pip list
	
	#套件升級
	pip install pandas -upgrade
	
	#show 出套件資料
	pip show pandas
	
	#將用pip安裝的套件資料匯出至requirement.txt
	pip freeze > requirement.txt
	
	#將requirement.txt中的套件資料全下載安裝
	pip install -r requirement.txt
	
	
	
6.作者的github -> https://github.com/arleigh418

7.作者推薦的 git 學習資源: doggy8088/Learn-Git-in-30-days

8.本國上市證劵編碼公告
https://isin.twse.com.tw/isin/C_public.jsp?strMode=2


=========設置畫布=========

1.要先 install mpl_finance 
2.在程式中要import mpl_finance及 matplotlib

3.設置畫布的一些眉角

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


