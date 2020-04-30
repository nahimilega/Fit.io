from flask import Flask, render_template, redirect, url_for,request, jsonify, session
from flask import make_response
import mysql.connector
from mysql.connector import Error
import updateUserData
import random

# DB connection imports
import healthcaredb
#import insurancedb

from getfoodRecommendation import get_food_recommendation, get_all_food, enter_new_meal, makeConnection
from functools import wraps

import time, threading

app = Flask(__name__)
app.secret_key = 'ButterNaan'  # Change this!



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
userData = []

makeConnection(userCursor, connection)

def fakeQuery():

    userDataCommand = """select sleep from daily_record_1"""
    userCursor.execute(userDataCommand)
    some = userCursor.fetchall()
    dieticianCommand = '''  select * from User_Dieticians where User_ID = %s'''
    healthcaredb.healthCareCursor.execute(dieticianCommand, (1,))
    dieticianData = healthcaredb.healthCareCursor.fetchall()
    threading.Timer(220, fakeQuery).start()

fakeQuery()

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return wrap

@app.route("/logout")
@login_required
def logout():
    del session['logged_id']
    session.clear()
    return render_template('login.html')


@app.route("/login")
def loginPage():
    if 'logged_id' in session:
        return render_template('index.html', username = session['name'])
    return render_template('login.html')


@app.route("/dash")
@login_required
def dashboard():
    return render_template('index.html', username = session['name'])

@app.route("/forgotPass")
def forgotPass():
    return render_template('forgot-password.html')

@app.route("/register")
def register():
    return render_template('register.html')


@app.route("/calendar")
@login_required
def calendar():
    return render_template('calendar.html',
                            username = session['name'])

@app.route("/hospital")
@login_required
def hospital():
    hospitalCommand = ''' select * from Hospital '''
    userCursor.execute(hospitalCommand)
    hospitalData = userCursor.fetchall()
    # nearbyRestData = random.sample(restaurantData, 5)
    data = []
    for d in hospitalData:
        dataDict = {}
        dataDict['name'] = d[1] + " Hospital"
        dataDict['location'] = d[2]
        data.append(dataDict)
    return render_template('hospital.html',
                            username = session['name'],
                            data = data)

@app.route("/coupons")
@login_required
def coupons():
    return render_template('myCoupons.html',
                            username = session['name'])

@app.route("/dieticians")
@login_required
def dietician():
    dietdata = dieticianData()

    return render_template('dieticians.html',
                            username = session['name'],
                            data = dietdata )

@app.route("/editprofile")
@login_required
def editProfile():
    return render_template('edit-profile.html', username = session['name'])


@app.route("/entermeal")
@login_required
def enterMeal():
    food_list = get_all_food()

    return render_template('enterMeal.html', username = session['name'], food_list = food_list)


@app.route('/inputmeal',methods = ['POST', 'GET'])
@login_required
def result():
    if request.method == 'POST':
        result = request.form
        enter_new_meal(result, session['id'])

    food_list = get_all_food()
    return render_template('enterMeal.html', username = session['name'], food_list = food_list)


@app.route("/foodReommendation")
@login_required
def foodRecommendation():
    breakfast = get_food_recommendation(session['id'],0)
    lunch = get_food_recommendation(session['id'],1)
    snacks = get_food_recommendation(session['id'],2)
    dinner = get_food_recommendation(session['id'],3)
    return render_template('foodReommendation.html', username = session['name'],
                           breakfast = breakfast,lunch = lunch, snacks = snacks, dinner = dinner)


@app.route("/mydietician")
@login_required
def myDietician():
    name, designation = getMyDieticianData()
    return render_template('myDietician.html',
                            username = session['name'],
                            dieticianName = name,
                            designation = designation)

@app.route("/nearbyRestraunts")
@login_required
def nearbyRestraunts():
    restaurantCommand = ''' select * from RESTAURANTS '''
    userCursor.execute(restaurantCommand)
    restaurantData = userCursor.fetchall()

    nearbyRestData = random.sample(restaurantData, 5)
    data = []
    for d in nearbyRestData:
        dataDict = {}
        dataDict['name'] = d[1]
        dataDict['location'] = d[2]
        dataDict['rating'] = d[3]
        data.append(dataDict)

    return render_template('nearbyRestraunts.html',
                            username = session['name'],
                            data = data)

@app.route("/dieticianProfile")
@login_required
def dieticianProfile():
    dieticianID = request.args.get('id')

    dieticianCommand = '''  select * from Dieticians where Dietician_ID = %s'''
    healthcaredb.healthCareCursor.execute(dieticianCommand, (dieticianID,))
    dieticianData = healthcaredb.healthCareCursor.fetchall()
    dieticianData = list(dieticianData[0])
    name = dieticianData[1].split()[1]
    dataDict = {}
    email = name+"@iiitd.ac.in"
    dataDict['did'] = dieticianData[0]
    dataDict['id'] = dieticianData[0]
    dataDict['name'] = dieticianData[1]
    dataDict['qualification'] = dieticianData[2]
    dataDict['area_of_interest'] = dieticianData[3]
    dataDict['experience'] = dieticianData[4]
    dataDict['rating'] = dieticianData[5]
    dataDict['email'] = email
    return render_template('dieticianProfile.html',
                            username = session['name'],
                            data = dataDict)


@app.route('/index/getmoreinfo', methods=['GET', 'POST'])
def indexInfo():
    global userData
    userid = session['id']
    userDailyDataCommand = """select * from daily_record_"""+str(userid)
    userCursor.execute(userDailyDataCommand)
    userDailyData = userCursor.fetchall()
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
    message = None
    if request.method == 'POST':
        emailID = request.form['user']
        password = request.form['pass']

        userDataCommand = """select * from users where email = %s"""
        userCursor.execute(userDataCommand, (emailID,))
        userData = userCursor.fetchall()
        if len(userData) == 0 or password != 'temp':
            return jsonify(listData = userData)

        userData = list(userData[0])
        session['logged_in'] = True
        session['id'] = userData[0]
        session['name'] = userData[1] + " " + userData[2]

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

        connection ,userCursor = updateUserData.updateRecord(session['id'], firstName, lastName, DOB, address, contact, weight)

        session['name']  = firstName + " " + lastName

        return jsonify(updated="True")
    return render_template('edit-profile.html', username = session['name'])

@app.route('/dieticianProfile', methods=['GET', 'POST'])
def updatemyDietician():
    if request.method == 'POST':
        dieiticianID = request.form['did']
        uid = session['id']
        updateCommand = '''UPDATE User_Dieticians
                        SET Dietician_ID = %s
                        WHERE User_ID = %s '''
        values = (dieiticianID, uid)
        healthcaredb.healthCareCursor.execute(updateCommand, values)
        healthcaredb.healthCareConnection.commit()
    return "hello"

def dieticianData():
    # Healthcare db contains dietician

    dieticianCommand = '''select * from Dieticians'''
    healthcaredb.healthCareCursor.execute(dieticianCommand)
    dieticianData = healthcaredb.healthCareCursor.fetchall()
    data = []
    for i in range(len(dieticianData)):
        dieticianDict = {}
        dieticianDict['name'] = dieticianData[i][1]
        dieticianDict['designation'] = dieticianData[i][3]
        dieticianDict['id'] = dieticianData[i][0]
        data.append(dieticianDict)
    return data




def getMyDieticianData():
    dieticianCommand = '''  select * from User_Dieticians where User_ID = %s'''

    healthcaredb.healthCareCursor.execute(dieticianCommand, (session['id'],))
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