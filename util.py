import selenium
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import time
from fake_useragent import UserAgent
import pandas as pd 
import os
import sqlite3

def getDelistedData():
	url = "https://archives.nseindia.com/content/equities/delisted.xlsx"
	options = Options()
	ua = UserAgent()
	userAgent = ua.random
	options.add_argument(f'user-agent={userAgent}')
	options.add_argument("--headless")
	options.add_argument("--incognito")
	options.add_argument('--remote-debugging-port=9222')
	cwd = os.getcwd()
	prefs = {"download.default_directory" : cwd+"\\download"}
	options.add_experimental_option("prefs",prefs)
	driver = webdriver.Chrome(options = options)
	driver.get(url)
	time.sleep(3)
	data = pd.read_excel(cwd+"\\download\\delisted.xlsx")
	data = data.drop(["Company","Board","Delisted Date","Type of Delisting"],axis=1)
	dataList = data["Symbol"].tolist()
	os.remove(cwd+"\\download\\delisted.xlsx")
	driver.close()
	return dataList
	

def removeNoiseOpm(text):
	if(text == '—'):
		return 0
	text = repr(text)
	out1 = ""
	out2 = ""
	temp = []
	for i in range(len(text)):
		temp.append(text[i])	
	try:
		temp1 = temp[7:12]
		for i in temp1:
			out1 += i
		return float(out1)
	except Exception as e:
		temp2 = temp[7:11]
		for i in temp2:
			out2 += i
		return out2
				

def removeNoiseDe(text):
	if("-" in text):
		text = repr(text)
		out = ""
		temp = []
		for i in range(len(text)):
			temp.append(text[i])
		temp = temp[7:12]
		for i in temp:
			out += i
		return float(out)
	if(text == '—'):
		return 0	
	text = repr(text)
	out = ""
	temp = []
	for i in range(len(text)):
		temp.append(text[i])
	temp = temp[7:11]
	for i in temp:
		out += i
	return float(out)

def createTable(name):
	connection = sqlite3.connect("growing_stocks.db")
	cursor = connection.cursor()
	cursor.execute(f"""CREATE TABLE {name}(
	ticker text,	
	mcap real,
	enp_val real,
	no_share real,
	pe real,
	opm real,
	debt_to_equity real,
	pg real,
	debt real,
	sales_growth real,
	roe real,
	finology_url text,
	tradingView_url text
	)""")
	print("Table Created")
	connection.close()





	







		


