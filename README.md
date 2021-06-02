# Growing Stocks Scraper
<br>
<h2>A tool to get growing stocks based on custom parameters in NIFTY 500 stocks for further analysis 
<br>
<br>
<h2> Installation
<h3> pip install -r requiremnts.txt
<br>
<br>
<h2> Usage
<h3> python api.py
<h3> head on to your browser and type "http://127.0.0.1:5000/growingstocks.json" and Hit Enter to get growing stocks in json format
<br>
<h3> To Update DataBase with Latest Data, type "http://127.0.0.1:5000/updateall" and hit Enter
<br>
<br>
<h2>Sample Response From API
<br>
  
  ```json
  {"IT":{"HCLTECH":{"debt_to_equity":0.11,"mcap":244094.18,"opm":16.71,"pe":27.92,"pg":27.51,"roe":26.48,"sales_growth":25.35,"ticker":"HCLTECH"},"INFY":{"debt_to_equity":0.07,"mcap":576867.96,"opm":24.48,"pe":31.96,"pg":21.01,"roe":27.12,"sales_growth":8.68,"ticker":"INFY"},"LTI":{"debt_to_equity":0.12,"mcap":67975.37,"opm":20.62,"pe":39.14,"pg":15.24,"roe":32.0,"sales_growth":14.34,"ticker":"LTI"},"MINDTREE":{"debt_to_equity":0.12,"mcap":34682.57,"opm":18.55,"pe":31.24,"pg":13.93,"roe":29.79,"sales_growth":2.62,"ticker":"MINDTREE"},"MPHASIS":{"debt_to_equity":0.2,"mcap":33032.1,"opm":16.36,"pe":25.11,"pg":27.72,"roe":35.27,"sales_growth":23.48,"ticker":"MPHASIS"},"OFSS":{"debt_to_equity":0.02,"mcap":29873.76,"opm":47.23,"pe":17.28,"pg":44.89,"roe":34.97,"sales_growth":-1.55,"ticker":"OFSS"},"TCS":{"debt_to_equity":0.09,"mcap":1123919.77,"opm":26.85,"pe":36.3,"pg":22.77,"roe":42.02,"sales_growth":3.55,"ticker":"TCS"},"TECHM":{"debt_to_equity":0.11,"mcap":93143.57,"opm":16.48,"pe":21.97,"pg":15.52,"roe":21.53,"sales_growth":7.34,"ticker":"TECHM"},"WIPRO":{"debt_to_equity":0.19,"mcap":269792.91,"opm":20.49,"pe":26.82,"pg":17.22,"roe":18.19,"sales_growth":4.74,"ticker":"WIPRO"}},"auto":{"BAJAJ-AUTO":{"debt_to_equity":0.0,"mcap":111145.87,"opm":16.93,"pe":24.4,"pg":17.05,"roe":24.46,"sales_growth":-1.45,"ticker":"BAJAJ-AUTO"},"BALKRISIND":{"debt_to_equity":0.16,"mcap":34194.91,"opm":24.85,"pe":32.86,"pg":19.76,"roe":19.47,"sales_growth":-8.81,"ticker":"BALKRISIND"}},"bank":{"BANDHANBNK":{"carPercentage":27.43,"casaRatio":36.84,"debt_to_equity":0.73,"opm":21.89,"pe":19.83,"pg":27.78,"roe":22.91,"ticker":"BANDHANBNK"},"HDFCBANK":{"carPercentage":18.52,"casaRatio":42.23,"debt_to_equity":0.8,"opm":29.65,"pe":26.37,"pg":22.87,"roe":16.4,"ticker":"HDFCBANK"}},"consumer_durables":{},"finance_services":{},"fmcg":{"ITC":{"debt_to_equity":0.0,"mcap":253069.84,"opm":33.42,"pe":19.41,"pg":32.34,"roe":25.66,"sales_growth":1.39,"ticker":"ITC"}},"health_care":{"ALKEM":{"debt_to_equity":0.2,"mcap":32897.11,"opm":19.85,"pe":20.64,"pg":18.1,"roe":21.53,"sales_growth":16.85,"ticker":"ALKEM"},"AUROPHARMA":{"debt_to_equity":0.28,"mcap":56572.37,"opm":17.16,"pe":18.97,"pg":14.07,"roe":15.37,"sales_growth":8.23,"ticker":"AUROPHARMA"},"DRREDDY":{"debt_to_equity":0.12,"mcap":82660.86,"opm":16.4,"pe":34.77,"pg":24.79,"roe":21.22,"sales_growth":11.53,"ticker":"DRREDDY"},"IPCALAB":{"debt_to_equity":0.08,"mcap":27488.85,"opm":22.23,"pe":24.61,"pg":14.94,"roe":19.18,"sales_growth":20.31,"ticker":"IPCALAB"},"SANOFI":{"debt_to_equity":0.01,"mcap":17883.05,"opm":20.35,"pe":37.44,"pg":16.46,"roe":21.39,"sales_growth":-5.49,"ticker":"SANOFI"}},"media":{"SUNTV":{"debt_to_equity":0.01,"mcap":18070.75,"opm":53.71,"pe":13.68,"pg":40.3,"roe":24.8,"sales_growth":-7.07,"ticker":"SUNTV"},"TVTODAY":{"debt_to_equity":0.02,"mcap":1612.54,"opm":29.86,"pe":12.98,"pg":16.6,"roe":16.1,"sales_growth":15.88,"ticker":"TVTODAY"}},"metal":{"COALINDIA":{"debt_to_equity":0.17,"mcap":76818.41,"opm":18.32,"pe":4.9,"pg":1088.58,"roe":73.23,"sales_growth":-8.53,"ticker":"COALINDIA"},"HINDZINC":{"debt_to_equity":0.25,"mcap":119365.26,"opm":43.59,"pe":17.46,"pg":36.66,"roe":18.41,"sales_growth":-12.11,"ticker":"HINDZINC"}},"oil_gas":{"CASTROLIND":{"debt_to_equity":0.01,"mcap":12037.62,"opm":26.96,"pe":20.65,"pg":17.43,"roe":42.58,"sales_growth":-22.7,"ticker":"CASTROLIND"},"GSPL":{"debt_to_equity":0.28,"mcap":14263.26,"opm":26.88,"pe":15.12,"pg":46.8,"roe":17.79,"sales_growth":26.18,"ticker":"GSPL"},"GUJGASLTD":{"debt_to_equity":0.39,"mcap":36670.54,"opm":18.68,"pe":31.3,"pg":11.34,"roe":43.59,"sales_growth":32.83,"ticker":"GUJGASLTD"},"IGL":{"debt_to_equity":0.02,"mcap":34874.04,"opm":29.44,"pe":37.58,"pg":15.86,"roe":24.73,"sales_growth":12.5,"ticker":"IGL"},"MGL":{"debt_to_equity":0.02,"mcap":10677.88,"opm":40.91,"pe":18.62,"pg":24.31,"roe":29.66,"sales_growth":6.49,"ticker":"MGL"}},"pharma":{"ALKEM":{"debt_to_equity":0.2,"mcap":32897.11,"opm":19.85,"pe":20.64,"pg":18.1,"roe":21.53,"sales_growth":16.85,"ticker":"ALKEM"},"AUROPHARMA":{"debt_to_equity":0.28,"mcap":56572.37,"opm":17.16,"pe":18.97,"pg":14.07,"roe":15.37,"sales_growth":8.23,"ticker":"AUROPHARMA"},"DRREDDY":{"debt_to_equity":0.12,"mcap":82660.86,"opm":16.4,"pe":34.77,"pg":24.79,"roe":21.22,"sales_growth":11.53,"ticker":"DRREDDY"}},"psu_bank":{}}

```


