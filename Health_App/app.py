from flask import Flask, render_template, redirect, url_for,request, jsonify, session
from flask import make_response
import mysql.connector
from mysql.connector import Error
import updateUserData
from getfoodRecommendation import get_food_recommendation, get_all_food, enter_new_meal
from functools import wraps
app = Flask(__name__)
app.secret_key = 'ButterNaan'  # Change this!




connection = mysql.connector.connect(
        host="localhost",
        user="archit",
        passwd="1",
        database="user"
    )
userCursor = connection.cursor(buffered=True)
userData = []




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
    session.clear()
    return render_template('login.html')


@app.route("/login")
def loginPage():
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
    return render_template('calendar.html', username = session['name'])


@app.route("/dieticians")
@login_required
def dietician():
    return render_template('dieticians.html', username = session['name'])


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
    return render_template('myDietician.html', username = session['name'])


@app.route("/nearbyRestraunts")
@login_required
def nearbyRestraunts():
    return render_template('nearbyRestraunts.html', username = session['name'])

@app.route("/")
def home():
    return "hi"
# @app.route("/index")

@app.route('/index/getmoreinfo', methods=['GET', 'POST'])
def indexInfo():
    global userData
    userid = userData[0]
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
    global userData
    message = None
    if request.method == 'POST':
        emailID = request.form['user']
        password = request.form['pass']

        userDataCommand = """select * from users where email = %s"""
        userCursor.execute(userDataCommand, (emailID,))
        userData = userCursor.fetchall()
        print(password)
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


        userDataCommand = """select * from users where U_ID = %s"""
        userCursor.execute(userDataCommand, (session['id'],))
        userData = userCursor.fetchall()

        return jsonify(updated="True")
        return render_template('edit-profile.html', username = session['name'])


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response

if __name__ == "__main__":
    # app.run(host="127.0.0.1", port="5000", debug = True)
    # app.run(debug = True)
    app.run(host='0.0.0.0', port="5000", debug=True)