from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, send_file
import os
app = Flask(__name__)
@app.route('/data.csv')
def csv():
	try:
		return send_file('graph.csv', attachment_filename='graph.csv')
	except Exception as e:
		return str(e)
@app.route("/chart")
def chart():
    return render_template('t.html')  
@app.route('/setalert', methods=['POST'])
def setalert():
    emitent=request.form['alertems']
    email=request.form['alertmail']
    value=request.form['alertval']
    try:
		with open("sendalert.txt","w+") as f:
			f.write(emitent + "," + value + "," + email)
		return redirect(url_for('chart'))
    except Exception as e:
		return str(e)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=15029, debug=True)

