from flask import Flask, render_template, redirect, url_for,request
from flask import make_response
import mysql.connector

userdb = mysql.connector.connect(
	host="bfg8ldijk5ukggyco7j2-mysql.services.clever-cloud.com",
	user="ug7yaayxgn0b773v",
	passwd="FRIWs9XAaP8PeGxjP9a2",
	database="bfg8ldijk5ukggyco7j2"
)

userCursor = userdb.cursor(buffered=True)

app = Flask(__name__)

currentUser = ''


# @app.route("/")
# def home():
#     return "hi"
# # @app.route("/index")

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#    message = None
#    if request.method == 'POST':
#         datafromjs = request.form['mydata']
#         print(datafromjs)
        
#         result = "Hello From Python"
#         resp = make_response('{"response": '+result+'}')
#         resp.headers['Content-Type'] = "application/json"
#         return resp
#         # return render_template('loging.html', message='')

# @app.after_request
# def add_headers(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     return response

@app.route('/userPage')
def userPage():
	print(currentUser)
	return currentUser

@app.route('/home')
def homePage():
	return render_template('home.html')

@app.route('/home', methods=['POST'])
def my_form_post():

	global currentUser, userCursor
	currentUser = request.form['user']
	userDataCommand = """select * from users where first_name = %s"""
	userCursor.execute(userDataCommand, (currentUser,))
	userData = userCursor.fetchall()
	
	
	if(len(userData)==0):
		return redirect(url_for('homePage'))
	print("userdata: ", userData)
	return redirect(url_for('userPage'))


if __name__ == "__main__":
    # app.run(host="127.0.0.1", port="5000", debug = True)
    # app.run(debug = True)
    # app.run(host='0.0.0.0', port="5000", debug=True)
	app.run(debug=True)