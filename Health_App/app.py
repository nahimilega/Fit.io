from flask import Flask, render_template, redirect, url_for,request, jsonify
from flask import make_response
import mysql.connector
from mysql.connector import Error
import updateUserData

# DB connection imports
import healthcaredb
import hospitaldb
import restaurantdb
import insurancedb

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

@app.route("/login")
def loginPage():
	global userData, userDailyData
	userData = []
	userDailyData = []
	return render_template('login.html')

@app.route("/dash")
def dashboard():
	return render_template('index.html', username = userData[1]+" "+userData[2])

@app.route("/forgotPass")
def forgotPass():
	return render_template('forgot-password.html')

@app.route("/register")
def register():
	return render_template('register.html')

@app.route("/calendar")
def calendar():
	return render_template('calendar.html', username = userData[1]+" "+userData[2])

@app.route("/dieticians")
def dietician():
	dietdata = dieticianData()
	template = '<div class="col-md-4 col-sm-4  col-lg-3">'+'<div class="profile-widget">' +'<div class="doctor-img">' +'<a class="avatar" href="#"><img alt="" src="{{ url_for('+ "'static'"+ ', filename='+"'assets/img/doctor-thumb-12.jpg') }}"'></a>'+'</div>' +'<h4 class="doctor-name text-ellipsis"><a href="#">%s</a></h4>'+'<div class="doc-prof">%s</div>'+'<div class="user-country">'+'<i class="fa fa-map-marker"></i> United States, San Francisco'+'</div>'+'</div>'+'</div>' 
	template = template *20
	return render_template('dieticians.html', 
							username = userData[1]+" "+userData[2],
							data = dietdata )

@app.route("/editprofile")
def editProfile():
	return render_template('edit-profile.html', username = userData[1]+" "+userData[2])

@app.route("/entermeal")
def enterMeal():
	return render_template('enterMeal.html', username = userData[1]+" "+userData[2])

@app.route("/foodReommendation")
def foodRecommendation():
	return render_template('foodReommendation.html', username = userData[1]+" "+userData[2])

@app.route("/mydietician")
def myDietician():
	name, designation = getMyDieticianData()
	return render_template('myDietician.html', 
							username = userData[1]+" "+userData[2],
							dieticianName = name,
							designation = designation)

@app.route("/nearbyRestraunts")
def nearbyRestraunts():
	return render_template('nearbyRestraunts.html', username = userData[1]+" "+userData[2])

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
	if(type(userData[0])==tuple):
		print("userData:   ", userData)
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
		userData = list(userData[0])
		if(type(userData[0])==tuple):
			userData = list(userData[0])
		return jsonify(listData = userData)

@app.route('/editprofile', methods=['GET', 'POST'])
def update():
	global userData
	if request.method == 'POST':
		firstName = request.form['firstName']
		lastName = request.form['lastName']
		DOB = request.form['DOB']
		address = request.form['address']
		contact = request.form['contact']
		weight = request.form['weight']
		# print("fuck")
		print(firstName)
		print(lastName)
		connection ,userCursor = updateUserData.updateRecord(userData[0], firstName, lastName, DOB, address, contact, weight)

		
		userDataCommand = """select * from users where U_ID = %s"""
		userCursor.execute(userDataCommand, (userData[0],))
		userData = userCursor.fetchall()
		if(type(userData[0])==tuple):
			userData = list(userData[0])
		return jsonify(updated="True")
		return render_template('edit-profile.html', username = userData[1]+" "+userData[2])


def dieticianData():
	global userData
	
	# Healthcare db contains dietician

	dieticianCommand = '''select * from Dieticians'''
	healthcaredb.healthCareCursor.execute(dieticianCommand)
	dieticianData = healthcaredb.healthCareCursor.fetchall()
	data = []
	for i in range(len(dieticianData)):
		dieticianDict = {}
		dieticianDict['name'] = dieticianData[i][1]
		dieticianDict['designation'] = dieticianData[i][3]
		data.append(dieticianDict)
	return data



def getMyDieticianData():
	dieticianCommand = '''  select * from User_Dietician where User_ID = %s'''

	healthcaredb.healthCareCursor.execute(dieticianCommand, (userData[0],))
	dieticianData = healthcaredb.healthCareCursor.fetchall()
	mydieticianID = dieticianData[0][1]

	dieticianCommand = '''  select * from Dieticians where Dietician_ID = %s'''
	healthcaredb.healthCareCursor.execute(dieticianCommand, (mydieticianID,))
	dieticianData = healthcaredb.healthCareCursor.fetchall()
	dieticianData = list(dieticianData[0])

	return dieticianData[1], dieticianData[3]
	

@app.after_request
def add_headers(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	return response

if __name__ == "__main__":
	# app.run(host="127.0.0.1", port="5000", debug = True)
	# app.run(debug = True)
	app.run(host='0.0.0.0', port="5000", debug=True)