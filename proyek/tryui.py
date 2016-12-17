#!/usr/bin/python

from flask import Flask, json, request, render_template, session, abort, redirect, url_for
import os
import mysql.connector
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)

db=mysql.connector.connect(user="m26415031",password="tos",host="localhost",database="m26415031")

cursor=db.cursor()

@app.route("/main")
def main():
    return render_template('index.html')
	
@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signupmethod',methods=['POST','GET'])
def signupmethod(): 
    try:
        _name = request.form['inputName']
	_user = request.form['inputUsername']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:
            _hashed_password = generate_password_hash(_password)
	    sql="INSERT INTO users VALUES (NULL,_name,_user,_password)"
            #data = cursor.fetchall()
	    cursor.execute(sql)
            db.commit()
            return json.dumps({'message':'User created successfully !'})
        #else:
        #    return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        if cursor:
            cursor.close() 
        if db:
            db.close()

			
@app.route('/signin')
def signin():
    return render_template('signin.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=15031, debug=True)
