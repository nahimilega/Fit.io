from flask import Flask, render_template, redirect, url_for,request, jsonify
from flask import make_response
import mysql.connector
from mysql.connector import Error
import datetime

app = Flask(__name__)

'''
connection = mysql.connector.connect(
		host="localhost",
		user="archit",
		passwd="1",
		database="user"
	)
'''

connection = mysql.connector.connect(user='ug7yaayxgn0b773v', passwd='FRIWs9XAaP8PeGxjP9a2',
				host='bfg8ldijk5ukggyco7j2-mysql.services.clever-cloud.com', database = "bfg8ldijk5ukggyco7j2"
			)

userCursor = connection.cursor(buffered=True)
# userData = []
# userDailyData = []
def updateRecord(uid, firstName, lastName, DOB, address, contact, weight):
	month = int(DOB[:2])
	day = int(DOB[3:5])
	year = int(DOB[6:])
	date = datetime.date(year, month, day)
	updateCommand = '''UPDATE users
	                SET first_name=%s, last_name=%s , date_of_birth=%s, address=%s, contact=%s
	                WHERE U_ID = %s
					'''
	values = (firstName, lastName, date, address, contact, uid)
	userCursor.execute(updateCommand, values)
	connection.commit()
	updateCommand = '''select * from users where U_ID=%s
					'''
	userCursor.execute(updateCommand, (uid,))
	return connection, userCursor
	# user = userCursor.fetchall()




# @app.route("/login")
# def loginPage():
# 	global userData, userDailyData
# 	userData = []
# 	userDailyData = []
# 	return render_template('login.html')

# @app.route("/dash")
# def dashboard():
# 	return render_template('index.html')

# @app.route("/forgotPass")
# def forgotPass():
# 	return render_template('forgot-password.html')

# @app.route("/register")
# def register():
# 	return render_template('register.html')

# @app.route("/calendar")
# def calendar():
# 	return render_template('calendar.html')

# @app.route("/dieticians")
# def dietician():
# 	return render_template('dieticians.html')

# @app.route("/editprofile")
# def editProfile():
# 	return render_template('edit-profile.html')

# @app.route("/entermeal")
# def enterMeal():
# 	return render_template('enterMeal.html')

# @app.route("/foodReommendation")
# def foodRecommendation():
# 	return render_template('foodReommendation.html')

# @app.route("/mydietician")
# def myDietician():
# 	return render_template('myDietician.html')

# @app.route("/nearbyRestraunts")
# def nearbyRestraunts():
# 	return render_template('nearbyRestraunts.html')

# @app.route("/")
# def home():
# 	return "hi"
# # @app.route("/index")

# @app.route('/index/getmoreinfo', methods=['GET', 'POST'])
# def indexInfo():
# 	global userData, userDailyData
# 	userid = userData[0]
# 	userDailyDataCommand = """select * from daily_record_"""+str(userid)
# 	userCursor.execute(userDailyDataCommand)
# 	userDailyData = userCursor.fetchall()
# 	print(userDailyData)
# 	return jsonify(daily = userDailyData)


# @app.route('/index', methods=['GET', 'POST'])
# def index():
# 	global userData
# 	if(type(userData[0])==tuple):
# 		userData = list(userData[0])
# 	return jsonify(listData = userData)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
# 	global userData
# 	message = None
# 	if request.method == 'POST':
# 		username = request.form['user']
# 		password = request.form['pass']

# 		userDataCommand = """select * from users where first_name = %s"""
# 		userCursor.execute(userDataCommand, (username,))
# 		userData = userCursor.fetchall()

# 		print(userData)
# 		return jsonify(listData = userData)

# @app.after_request
# def add_headers(response):
# 	response.headers.add('Access-Control-Allow-Origin', '*')
# 	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
# 	return response

if __name__ == "__main__":
	# app.run(host="127.0.0.1", port="5000", debug = True)
	# app.run(debug = True)
	app.run(host='0.0.0.0', port="5000", debug=True)