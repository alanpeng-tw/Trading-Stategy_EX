# Trading-Stategy_EX




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

	pandas及requests、beautifulsoup4、lxml
	
	pip install pandas
	pip install requests
	pip install beautifulsoup4
	pip install lxml
	pip install openpyxl
	
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



