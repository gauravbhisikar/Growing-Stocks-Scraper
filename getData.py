import selenium
from selenium import webdriver 
import request
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent
import random
from util import *
import requests
import sqlite3
import json

class FundmentalData:
	def __init__(self):
		options = Options()
		ua = UserAgent()
		userAgent = ua.random
		print(userAgent)
		options.add_argument(f'user-agent={userAgent}')
		options.add_argument("--headless")
		options.add_argument("--incognito")
		port = random.randrange(9000,9999)
		options.add_argument(f'--remote-debugging-port={port}')
		self.driver = webdriver.Chrome(options = options)
		self.loginedIn = False

	def getData(self,Ticker):
		print(Ticker)
		fix ={"L&TFH":"SCRIP-220350","M&M":"SCRIP-100520","M&MFIN":"SCRIP-132720","GET&D":"SCRIP-122275","J&KBANK":"SCRIP-132209"}
		fixTradingView = {"NAM-INDIA":"NAM_INDIA","MCDOWELL-N":"MCDOWELL_N","BAJAJ-AUTO":"BAJAJ_AUTO","M&M":"M_M","GET&D":"GET_D","J&KBANK":"J_KBANK","L&TFH":"L_TFH","M&MFIN":"M_MFIN"} 
		finology = ""
		tradingview = ""
		values = {
				"mcap" :0,
				"enp_val" : 0,
				"no_share" : 0,
				"pe" : 0,
				"opm" : 0,
				"debt_to_equity" : 0,
				"pg" :0,
				"debt" : 0,
				"sales_growth" : 0,
				"roe" : 0
				}

		try:
			self.driver.get(f'https://ticker.finology.in/company/{Ticker}')
			finology = self.driver.current_url
			time.sleep(random.randrange(3,4))
			if(self.driver.current_url == f'https://ticker.finology.in/company/{Ticker}'):
				time.sleep(random.randrange(3,4))
				soup = BeautifulSoup(self.driver.page_source,'html.parser')
				meta_data =  soup.find_all('span', class_ = "Number")
				forPe = soup.find_all('p')
				values = {
				"mcap" : float((meta_data[5].text).replace(",","")),
				"enp_val" : float((meta_data[6].text).replace(",","")),
				"no_share" : float((meta_data[7].text).replace(",","").replace("\\n","").replace("Cr.\\n","")),
				"pe" : float(forPe[8].text),
				"opm" : 0,
				"debt_to_equity" : 0,
				"pg" :float((meta_data[15].text).replace(",","")),
				"debt" : float((meta_data[10].text).replace(",","")),
				"sales_growth" : float((meta_data[12].text).replace(",","")),
				"roe" : float((meta_data[13].text).replace(",",""))
				}
				try:
					time.sleep(random.randrange(3,6))
					if Ticker not in fixTradingView:
						self.driver.get(f"https://in.tradingview.com/symbols/NSE-{Ticker}/financials-statistics-and-ratios/")
						tradingview = self.driver.current_url
					else:
						self.driver.get(f"https://in.tradingview.com/symbols/NSE-{fixTradingView[Ticker]}/financials-statistics-and-ratios/")
						tradingview = self.driver.current_url
					time.sleep(random.randrange(4,6))
					soup = BeautifulSoup(self.driver.page_source,'html.parser')
					data = soup.find_all("div") 
					opm = self.driver.find_element_by_xpath('//*[@id="js-category-content"]/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[20]/div[4]/div[5]').text
					debt_to_equity = self.driver.find_element_by_xpath('//*[@id="js-category-content"]/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[30]/div[4]/div[5]').text
					opm = removeNoiseOpm(opm)
					debt_to_equity = removeNoiseDe(debt_to_equity)
					values["opm"] = opm
					values["debt_to_equity"] = debt_to_equity 
				except Exception as e:
					print(1,e)
					print(f"Cant't acces tradingview.com for ticker {Ticker}")
					self.append(Ticker)	

			else:
				raise Exception("Ticker Not exist")
			
		except Exception as e:
			print(2,e)
			if Ticker in fix:
			 	self.driver.get(f'https://ticker.finology.in/company/{fix[Ticker]}')
			 	finology = self.driver.current_url
			 	time.sleep(random.randrange(2,5))
			 	soup = BeautifulSoup(self.driver.page_source,'html.parser')
			 	meta_data =  soup.find_all('span', class_ = "Number")
			 	forPe = soup.find_all('p')
			 	values = {
				"mcap" : float((meta_data[5].text).replace(",","")),
				"enp_val" : float((meta_data[6].text).replace(",","")),
				"no_share" : float((meta_data[7].text).replace(",","")),
				"pe" : float((forPe[8].text).replace(",","")),
				"opm" : 0,
				"debt_to_equity" : 0,
				"pg" :float((meta_data[15].text).replace(",","")),
				"debt" : float((meta_data[10].text).replace(",","")),
				"sales_growth" : float((meta_data[12].text).replace(",","")),
				"roe" : float((meta_data[13].text).replace(",",""))
				}

			try:
					time.sleep(random.randrange(3,6))
					if Ticker not in fixTradingView:
						self.driver.get(f"https://in.tradingview.com/symbols/NSE-{Ticker}/financials-statistics-and-ratios/")
						tradingview = self.driver.current_url
					else:
						self.driver.get(f"https://in.tradingview.com/symbols/NSE-{fixTradingView[Ticker]}/financials-statistics-and-ratios/")
						tradingview = self.driver.current_url
					time.sleep(random.randrange(3,5))
					soup = BeautifulSoup(self.driver.page_source,'html.parser')
					data = soup.find_all("div")  
					opm = self.driver.find_element_by_xpath('//*[@id="js-category-content"]/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[20]/div[4]/div[5]').text
					debt_to_equity = self.driver.find_element_by_xpath('//*[@id="js-category-content"]/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[30]/div[4]/div[5]').text
					opm = removeNoiseOpm(opm)
					debt_to_equity = removeNoiseDe(debt_to_equity)
					values["opm"] = opm
					values["debt_to_equity"] = debt_to_equity 
			except Exception as e:
					print(3,e)
					print(f"Cant't acces tradingview.com for ticker {Ticker}")
			

		print(values)
		return values, finology, tradingview

	def getDataBank(self,Ticker):
		print(Ticker)
		fix ={"L&TFH":"SCRIP-220350","M&M":"SCRIP-100520","M&MFIN":"SCRIP-132720","GET&D":"SCRIP-122275","J&KBANK":"SCRIP-132209"}
		fixTradingView = {"NAM-INDIA":"NAM_INDIA","MCDOWELL-N":"MCDOWELL_N","BAJAJ-AUTO":"BAJAJ_AUTO","M&M":"M_M","GET&D":"GET_D","J&KBANK":"J_KBANK","L&TFH":"L_TFH","M&MFIN":"M_MFIN"} 
		mcap = 0
		values = {
				"mcap" :0,
				"casaRatio" : 0,
				"no_share" : 0,
				"pe" : 0,
				"opm" : 0,
				"debt_to_equity" : 0,
				"pg" :0,
				"carPercentage" : 0,
				"roe" : 0
				}

		try:
			self.driver.get(f'https://ticker.finology.in/company/{Ticker}')
			time.sleep(random.randrange(3,4))
			if(self.driver.current_url == f'https://ticker.finology.in/company/{Ticker}'):
				time.sleep(random.randrange(3,4))
				soup = BeautifulSoup(self.driver.page_source,'html.parser')
				meta_data =  soup.find_all('span', class_ = "Number")
				forPe = soup.find_all('p')
				values = {
				"mcap" : float((meta_data[5].text).replace(",","")),
				"casaRatio" : float((meta_data[6].text).replace(",","")),
				"no_share" : float((meta_data[7].text).replace(",","").replace("\\n","").replace("Cr.\\n","")),
				"pe" : float(forPe[8].text),
				"opm" : 0,
				"debt_to_equity" : 0,
				"pg" :float((meta_data[14].text).replace(",","")),
				"carPercentage" : float((meta_data[15].text).replace(",","")),
				"roe" : float((meta_data[12].text).replace(",",""))
				}	
				try:
					time.sleep(random.randrange(3,6))
					if Ticker not in fixTradingView:
						self.driver.get(f"https://in.tradingview.com/symbols/NSE-{Ticker}/financials-statistics-and-ratios/")
					else:
						self.driver.get(f"https://in.tradingview.com/symbols/NSE-{fixTradingView[Ticker]}/financials-statistics-and-ratios/")
					time.sleep(random.randrange(4,6))
					soup = BeautifulSoup(self.driver.page_source,'html.parser')
					data = soup.find_all("div") 
					opm = self.driver.find_element_by_xpath('//*[@id="js-category-content"]/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[20]/div[4]/div[5]').text
					debt_to_equity = self.driver.find_element_by_xpath('//*[@id="js-category-content"]/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[30]/div[4]/div[5]').text
					opm = removeNoiseOpm(opm)
					debt_to_equity = removeNoiseDe(debt_to_equity)
					values["opm"] = opm
					values["debt_to_equity"] = debt_to_equity 
				except Exception as e:
					print(1,e)
					print(f"Cant't acces tradingview.com for ticker {Ticker}")
					self.append(Ticker)	

			else:
				raise Exception("Ticker Not exist")
			
		except Exception as e:
			print(2,e)
			if Ticker in fix:
			 	self.driver.get(f'https://ticker.finology.in/company/{fix[Ticker]}')
			 	time.sleep(random.randrange(2,5))
			 	soup = BeautifulSoup(self.driver.page_source,'html.parser')
			 	meta_data =  soup.find_all('span', class_ = "Number")
			 	forPe = soup.find_all('p')
			 	values = {
				"mcap" : float((meta_data[5].text).replace(",","")),
				"casaRatio" : float((meta_data[6].text).replace(",","")),
				"no_share" : float((meta_data[7].text).replace(",","")),
				"pe" : float((forPe[8].text).replace(",","")),
				"opm" : 0,
				"debt_to_equity" : 0,
				"pg" :float((meta_data[14].text).replace(",","")),
				"carPercentage" : float((meta_data[15].text).replace(",","")),
				"roe" : float((meta_data[12].text).replace(",",""))
				}

			try:
					time.sleep(random.randrange(3,6))
					if Ticker not in fixTradingView:
						self.driver.get(f"https://in.tradingview.com/symbols/NSE-{Ticker}/financials-statistics-and-ratios/")
					else:
						self.driver.get(f"https://in.tradingview.com/symbols/NSE-{fixTradingView[Ticker]}/financials-statistics-and-ratios/")
					time.sleep(random.randrange(3,5))
					soup = BeautifulSoup(self.driver.page_source,'html.parser')
					data = soup.find_all("div")  
					opm = self.driver.find_element_by_xpath('//*[@id="js-category-content"]/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[20]/div[4]/div[5]').text
					debt_to_equity = self.driver.find_element_by_xpath('//*[@id="js-category-content"]/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[30]/div[4]/div[5]').text
					opm = removeNoiseOpm(opm)
					debt_to_equity = removeNoiseDe(debt_to_equity)
					values["opm"] = opm
					values["debt_to_equity"] = debt_to_equity 
			except Exception as e:
					print(3,e)
					print(f"Cant't acces tradingview.com for ticker {Ticker}")
					self.append(Ticker)			

		print(values)
		return values			

	def updateRow(self,table,ticker,close=False):
		connection = sqlite3.connect("growing_stocks.db")
		cursor = connection.cursor()
		if(table != ('psu_bank' or 'bank')):
			values,f,t = self.getData(ticker)
			statement =  f"""UPDATE {table}
			SET mcap = '{values['mcap']}',enp_val = '{values['enp_val']}',no_share = '{values['no_share']}',pe = '{values['pe']}',opm = '{values['opm']}',debt_to_equity = '{values['debt_to_equity']}',pg = '{values['pg']}',debt = '{values['debt']}',sales_growth = '{values['sales_growth']}',roe = '{values['roe']}'
			WHERE ticker = '{ticker}'
			"""
		else:
			values = self.getDataBank(ticker)
			statement =  f"""UPDATE {table}
			SET mcap = '{values['mcap']}',casaRatio = '{values['casaRatio']}',no_share = '{values['no_share']}',pe = '{values['pe']}',opm = '{values['opm']}',debt_to_equity = '{values['debt_to_equity']}',pg = '{values['pg']}',carPercentage = '{values['carPercentage']}',roe = '{values['roe']}'
			WHERE ticker = '{ticker}'
			"""	
		cursor.execute(statement)
		if(close):
			self.closeDriver()
		connection.commit()
		print("Update Success")
		connection.close()

	def showData(self,table):
		self.driver.close()
		connection = sqlite3.connect("growing_stocks.db")
		cursor = connection.cursor()
		cursor.execute(f"SELECT * FROM {table}")
		print(cursor.description)
		print(cursor.fetchall())
		connection.close()

	def updateAll(self):
		auto = ['AMARAJABAT', 'ASHOKLEY', 'BAJAJ-AUTO', 'BALKRISIND', 'BHARATFORG', 'BOSCHLTD', 'EICHERMOT', 'EXIDEIND', 'HEROMOTOCO', 'MRF', 'M&M', 'MARUTI', 'MOTHERSUMI', 'TVSMOTOR', 'TATAMOTORS']
		bank = ['AUBANK', 'AXISBANK', 'BANDHANBNK', 'FEDERALBNK', 'HDFCBANK', 'ICICIBANK', 'IDFCFIRSTB', 'INDUSINDBK', 'KOTAKBANK', 'PNB', 'RBLBANK', 'SBIN']
		IT = ['HCLTECH', 'INFY', 'LTI', 'MINDTREE', 'MPHASIS', 'OFSS', 'TCS', 'TECHM', 'WIPRO']
		consumerDurables = ['AMBER', 'BATAINDIA', 'BLUESTARCO', 'CROMPTON', 'DIXON', 'HAVELLS', 'KAJARIACER', 'ORIENTELEC', 'RAJESHEXPO', 'RELAXO', 'TTKPRESTIG', 'TITAN', 'VGUARD', 'VOLTAS', 'WHIRLPOOL']
		financeServices = ['BAJFINANCE', 'BAJAJFINSV', 'CHOLAFIN', 'HDFCAMC', 'HDFCLIFE', 'HDFC', 'ICICIPRULI', 'M&MFIN', 'MUTHOOTFIN', 'PEL', 'PFC', 'RECLTD', 'SBILIFE', 'SRTRANSFIN']
		fmcg = ['BRITANNIA', 'COLPAL', 'DABUR', 'EMAMILTD', 'GODREJCP', 'HINDUNILVR', 'ITC', 'JUBLFOOD', 'MARICO', 'NESTLEIND', 'PGHH', 'TATACONSUM', 'UBL', 'MCDOWELL-N', 'VBL']
		healthCare = ['ABBOTINDIA', 'ALKEM', 'APOLLOHOSP', 'AUROPHARMA', 'BIOCON', 'CADILAHC', 'CIPLA', 'DIVISLAB', 'LALPATHLAB', 'DRREDDY', 'FORTIS', 'GLAXO', 'GLENMARK', 'IPCALAB', 'LUPIN', 'NATCOPHARM', 'PFIZER', 'SANOFI', 'SUNPHARMA', 'TORNTPHARM']
		media = ['DBCORP', 'DISHTV', 'INOXLEISUR', 'JAGRAN', 'NETWORK18', 'PVR', 'SUNTV', 'TVTODAY', 'TV18BRDCST', 'ZEEL']
		metal = ['APLAPOLLO', 'COALINDIA', 'HINDALCO', 'HINDZINC', 'JSWSTEEL', 'JINDALSTEL', 'MOIL', 'NMDC', 'NATIONALUM', 'RATNAMANI', 'SAIL', 'TATASTEEL', 'VEDL', 'WELCORP']
		oil_Gas = ['BPCL', 'CASTROLIND', 'GAIL', 'GUJGASLTD', 'GSPL', 'GULFOILLUB', 'HINDPETRO', 'IOC', 'IGL', 'MGL', 'ONGC', 'OIL', 'PETRONET', 'RELIANCE']
		pharma = ['ALKEM', 'AUROPHARMA', 'BIOCON', 'CADILAHC', 'CIPLA', 'DIVISLAB', 'DRREDDY', 'LUPIN', 'SUNPHARMA', 'TORNTPHARM']
		psuBank = ['BANKBARODA', 'BANKINDIA', 'MAHABANK', 'CANBK', 'CENTRALBK', 'INDIANB', 'IOB', 'J&KBANK', 'PNB', 'SBIN', 'UCOBANK', 'UNIONBANK']

		sectors = {'auto':auto, 'bank': bank, 'IT' : IT,'consumer_durables':consumerDurables,'finance_services':financeServices,  'fmcg' :fmcg , 'health_care': healthCare, 'media' : media, 'metal' : metal, 'oil_gas': oil_Gas , 'pharma' :pharma, 'psu_bank': psuBank}
		secc = ''
		for sector in sectors:
			secc = sector
			for i in range(len(sectors[sector])):
				self.updateRow(sector,sectors[sector][i])
				print(sector,sectors[sector][i])
				print("Update Success")
		self.closeDriver()		

	def getGrowingStocks(self):
		response = {} 
		connection = sqlite3.connect("growing_stocks.db")
		cursor = connection.cursor()
		sectorTables = ['auto','IT','consumer_durables','finance_services','fmcg','health_care','metal','media','oil_gas','pharma','bank','psu_bank']
		values = {'ticker':0 ,'sales_growth': 9 ,'pg': 7,'opm': 5,'debt_to_equity': 6, 'roe': 10,'mcap' : 1,'pe': 4}
		valuesBank = {'ticker':0,'casaRatio':2,'pe':4,'opm':5,'debt_to_equity':6,'pg':7,'carPercentage':8,'roe':9}
		for i in sectorTables:
			if i!="psu_bank" and i!="bank":
				insert = f"SELECT * FROM {i}	WHERE (sales_growth >= 0 OR pg >=15) AND opm >=15 AND debt_to_equity <= 0.5 AND roe > 15 AND mcap > 500 AND pe < 40"
				cursor.execute(insert)
				fetch = cursor.fetchall()
				response[i] = {}
				for value in range(len(fetch)):
					response[i][fetch[value][0]] = {}
					for keys in values:
						response[i][fetch[value][0]][keys] = fetch[value][values[keys]]
			else:
				insert = f"SELECT * FROM {i}	WHERE pg >=15 AND opm >=15 AND debt_to_equity <= 1 AND roe > 10 AND mcap > 500 AND pe < 40 AND casaRatio >=15"
				cursor.execute(insert)
				fetch = cursor.fetchall()
				response[i] = {}
				for value in range(len(fetch)):
					response[i][fetch[value][0]] = {}
					for keys in valuesBank:
						response[i][fetch[value][0]][keys] = fetch[value][valuesBank[keys]]	

		return response			 

	def closeDriver(self):
		self.driver.close()	
		