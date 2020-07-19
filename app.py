import os
import pymysql as mysql
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

#db = mysql.connect(user="root", passwd="password", db="twitterdb", charset="utf8")
#db.autocommit(True)
#c = db.cursor()

cookiename = 'openAMUserCookieName'
amURL = 'https://openam.example.com/' #URL for openam
validTokenAPI = amURL + 'openam/json/sessions/{token}?_action=validate'
loginURL = amURL + 'openam/UI/Login'

'''
#Connecting to forgerock
def session_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        usercookie = request.cookies.get(cookiename)
        if usercookie:
            amQuery = requests.post(validTokenAPI.format(token=usercookie))
            if amQuery.json()['valid']:
                return f(*args, **kwargs)
            return redirect(loginURL)
        return decorated_function


@app.route('/members_page')
@session_required
def members_page():
  pass

'''

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/subscribers')
def subscribers():
    return render_template('subscribers.html')


@app.route('/publishers')
def publishers():
    return render_template('publishers.html')

@app.route('/authorize/forgerock')
def oauth_authorize():
    # function to authorize with AM
    return #oauth.authorize()


if __name__ == "__main__":
    app.run(host="localhost", debug=True)
