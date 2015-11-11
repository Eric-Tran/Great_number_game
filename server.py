from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "SecretKey"
import random

@app.route('/')
def index():
	if session.get('random_num'):
		pass
	else:
		session['random_num'] = random.randrange(0,101)
		session['status'] = 'notset'

	return render_template('index.html')

@app.route('/process', methods=['POST'])
def user_guess():
	guess_num = int(request.form['guess'])

	if guess_num == session['random_num']:
		session['status'] = True

	elif guess_num < session['random_num']:
		session['status'] = 'low'

	elif guess_num > session['random_num']:
		session['status'] = 'high'

	return redirect('/')

@app.route('/reset')
def reset():
	session.pop('random_num')
	return redirect ('/')

app.run(debug = True)