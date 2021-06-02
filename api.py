from flask import Flask,jsonify
from getData import FundmentalData
import time 
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
data = FundmentalData()
@app.route('/')
def index():
	return "hello"


@app.route("/growingstocks.json",methods=['GET'])
def getStocks():	 
	return jsonify(data.getGrowingStocks())

@app.route("/updateall",methods=['POST'])
def updateStocks():
	data.updateAll()

if __name__=="__main__":
	app.run(debug=False)

