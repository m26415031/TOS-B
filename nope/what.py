#!/usr/bin/python

from flask import Flask, json, request, render_template, session, abort, redirect, url_for
import os
import mysql.connector
from werkzeug import generate_password_hash, check_password_hash
from flaskext.mysql import MySQL

app = Flask(__name__)
app.secret_key = os.urandom(20)


@app.route("/main")
def main():
    	return render_template('index.html')
	
@app.route('/signup')
def signup():
    	return render_template('signup.html')

@app.route('/signupmethod',methods=['POST','GET'])
def signupmethod():
	db=mysql.connector.connect(username="m26415031",password="tos",host="localhost",database="m26415031")
	cursor=db.cursor() 
	check = None
	try:
		if request.method == "POST": 
			name = request.form['inputName']
			user = request.form['inputUsername']
			email = request.form['inputEmail']
			password = request.form['inputPassword']
			sql="SELECT COUNT(*) FROM users WHERE username = user";
			cursor.execute(sql)
			check=cursor.fetchone()
			if check:
				return json.dumps({'message':'Username is taken, choose another one'})
			else:
				if name and username and email and password and cursor and db:
					hashedpass = generate_password_hash(password)
					sql="INSERT INTO users VALUES (NULL,user,name,email,hashedpass)";
					cursor.execute(sql)
					db.commit()
					cursor.close() 
					db.close()
					#session['userisin'] = True
					#session['username'] = username
					#return redirect(url_for('isi'))
					return json.dumps({'message':'Account created'})
	except Exception as e:
		#db.text()
		db.rollback()
		#return json.dumps({'error':str(e)})
		return(str(e))

			
@app.route('/signin',)
def signin():
    	return render_template('signin.html')
	
@app.route('/signinmethod/', methods=["GET","POST"])
def signinmethod():
	db=mysql.connector.connect(username="m26415031",password="tos",host="localhost",database="m26415031")
	cursor=db.cursor()
	check = None
    	try:
		#if 'username' in session:
			#return redirect(url_for('isi'))
        	if request.method == "POST":
			username = request.form['inputUsername']
			password = request.form['inputPassword']
			sql="SELECT COUNT(*) FROM users WHERE username = user";
			cursor.execute(sql)
			check=cursor.fetchone()
		if check:
			userpw="SELECT password FROM users where username = user";
			if check_password_hash(userpw,password) == True:
				return redirect(url_for('isi')) 
			else:
				return json.dumps({'message':'Wrong username/password'})
		if check <= 0:
			return json.dumps({'message':'Wrong username/password'})
	except Exception as e:
        	return(str(e))  

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=15031, debug=True)

