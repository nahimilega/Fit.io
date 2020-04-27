from flask import Flask, render_template, redirect, url_for,request, jsonify
from flask import make_response
import mysql.connector
from mysql.connector import Error
import updateUserData
from getfoodRecommendation import get_food_recommendation, get_all_food, enter_new_meal
app = Flask(__name__)

connection = mysql.connector.connect(
        host="localhost",
        user="archit",
        passwd="1",
        database="user"
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
    return render_template('dieticians.html', username = userData[1]+" "+userData[2])

@app.route("/editprofile")
def editProfile():
    return render_template('edit-profile.html', username = userData[1]+" "+userData[2])

@app.route("/entermeal")
def enterMeal():
    food_list = get_all_food()
    return render_template('enterMeal.html', username = userData[1]+" "+userData[2], food_list = food_list)

@app.route('/inputmeal',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        enter_new_meal(result, userData[0])

    food_list = get_all_food()
    return render_template('enterMeal.html', username = userData[1]+" "+userData[2], food_list = food_list)


@app.route("/foodReommendation")
def foodRecommendation():
    breakfast = get_food_recommendation(userData[0],0)
    lunch = get_food_recommendation(userData[0],1)
    snacks = get_food_recommendation(userData[0],2)
    dinner = get_food_recommendation(userData[0],3)
    return render_template('foodReommendation.html', username = userData[1]+" "+userData[2],
                           breakfast = breakfast,lunch = lunch, snacks = snacks, dinner = dinner)


@app.route("/mydietician")
def myDietician():
    return render_template('myDietician.html', username = userData[1]+" "+userData[2])

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


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response

if __name__ == "__main__":
    # app.run(host="127.0.0.1", port="5000", debug = True)
    # app.run(debug = True)
    app.run(host='0.0.0.0', port="5000", debug=True)