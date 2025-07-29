from flask import Flask, request, redirect, render_template, url_for, session
import json

app = Flask(__name__)
app.secret_key = 'password'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']

        with open('users.json') as f:
            users = json.load(f)

        if user in users and users[user] == pw:
            session['user'] = user
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid'
            return render_template('login.html', error=error)
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    user = session.get('user', 'Guest')
    return render_template('dashboard.html', user=user)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/incorrect')
def incorrect():
    return 'Incorrect method used to access login.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
