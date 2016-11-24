#!/usr/bin/python

from flask import Flask, request, render_template, session, abort, redirect, url_for
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

#error handling
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

#session
@app.route("/")
def index():
  session['user'] = 'Anthony'
  return 'Ini halaman index, a user logged in.'


@app.route("/getsession")
def getsession():
  if 'user' in session:
    return session['user']
  return 'Not logged in!'


@app.route("/dropsession")
def dropsession():
  session.pop('user', None)
  return 'Dropped!'
#end of session

#redirecting
'''
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
'''
#end of redirecting

#what even is this
'''
@app.route('/')
def index():
  return 'This is the homepage'
'''

@app.route('/tuna')		#bandingkan dengan: ('/tuna/')
def tuna():
  return '<h2>Tuna is good</h2>'

'''
@app.route('/profile/<username>')
def profile(username):
  return "Hey there %s" % username
'''

@app.route('/post/<int:post_id>')               #contoh: harus integer
def show_post(post_id):         #def nama tdk harus sama dg route
  return "<h2>Post ID is %s</h2>" % post_id

'''
@app.route("/")
def index():
  return "Method used: %s" % request.method
'''
#end of whatever it was

#templates
@app.route("/profile/<name>")
def profile(name):
  return render_template("profile.html", name=name)

'''
@app.route("/")
@app.route("/<user>")
def index(user=None):
  return render_template("user.html", user=user)
'''

@app.route("/shopping/")
def shopping():
  food = ["Cheese", "Tuna", "Beef"]
  return render_template("shopping.html", food=food)
#end of templates

#methods
@app.route("/bacon", methods=['GET', 'POST'])
def bacon():
  if request.method == 'POST':		#to get form values:
    return "You are using POST %s" % request.form["inputname"]
  else:
   #return "You are probably using GET (actual method: %s)" % request.method
   return "You are probably using GET %s" % request.form["inputname"]

@app.route("/update",methods=['PUT'])
def update():
  if request.method == 'PUT':
    return "You are using PUT %s" % request.form["inputname"]
  else:
    return "What even are you doing m8, you're using %s instead of PUT" % request.method  

@app.route("/remove",methods=['DELETE'])
def remove():
  if request.method == 'DELETE':
    return "You are using DELETE %s" % request.form["inputname"]
  else:
    return "What even are you doing m8, you're using %s instead of DELETE" % request.method
#end of methods

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=15031, debug=True)



