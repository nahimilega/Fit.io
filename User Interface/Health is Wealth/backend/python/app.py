from flask import Flask, render_template, redirect, url_for,request, jsonify
from flask import make_response
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

connection = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="scorpio",
		database="testing"
	)
userCursor = connection.cursor(buffered=True)
userData = []
userDailyData = []


@app.route("/")
def home():
	return "hi"
# @app.route("/index")

@app.route('/index/getmoreinfo', methods=['GET', 'POST'])
def indexInfo():
	global userData, userDailyData
	userid = userData[0]
	userDailyDataCommand = """select * from daily_record_"""+str(userid)
	userCursor.execute(userDailyDataCommand)
	userDailyData = userCursor.fetchall()	
	print(userDailyData)
	return jsonify(daily = userDailyData)


@app.route('/index', methods=['GET', 'POST'])
def index():
	global userData
	userData = list(userData[0])
	return jsonify(listData = userData)


@app.route('/login', methods=['GET', 'POST'])
def login():
	global userData
	message = None
	if request.method == 'POST':
		username = request.form['user']
		password = request.form['pass']

		userDataCommand = """select * from users where first_name = %s"""
		userCursor.execute(userDataCommand, (username,))
		userData = userCursor.fetchall()
		print(userData)

		return jsonify(listData = userData)

		# result = "Hello From Python"
		# resp = make_response('{"response": '+result+'}')
		# resp.headers['Content-Type'] = "application/json"
		# return resp
		# return render_template('loging.html', message='')

@app.after_request
def add_headers(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	return response

if __name__ == "__main__":
	# app.run(host="127.0.0.1", port="5000", debug = True)
	# app.run(debug = True)
	app.run(host='0.0.0.0', port="5000", debug=True)