#!/usr/bin/python

from flask import Flask, json, request, render_template, session, abort, redirect, url_for
from flaskext.mysql import MySQL
import os

mysql = MySQL();

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'm26415031'
app.config['MYSQL_DATABASE_PASSWORD'] = 'tos'
app.config['MYSQL_DATABASE_DB'] = 'm26415031'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

#cursor = mysql.get_db().cursor()

@app.route("/main")
def main():
    return render_template('index.html')

@app.route('/signup',methods=['POST','GET'])
def signup():
'''    
    cursor = None
    conn = None
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:
            
            # All Good, let's call MySQL
            
            conn = mysql.connect()
            cursor = conn.cursor()
            _hashed_password = generate_password_hash(_password)
            #cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
            
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'User created successfully !'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        if cursor:
            cursor.close() 
        if conn:
            conn.close()
'''

@app.route('/signin')
def signin():
    return render_template('signin.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=15031, debug=True)
