from flask import Flask, render_template, request, redirect, url_for, session, g
import os

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='whyapar', password='12345'))
users.append(User(id=2, username='pp_seen2825', password='12345'))
users.append(User(id=3, username='wawawawhannnn', password='12345'))
users.append(User(id=3, username='nuttakitt_', password='12345'))

app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

@app.route('/')
def index_template():
    return render_template('home.html')

@app.route('/home')
def home_template():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login_template():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            # print(user.id)
            if user.id == 1:
                return redirect(url_for('whyapar_template'))
            elif user.id == 2:
                return redirect(url_for('pp_seen2825_template'))
            elif user.id == 3:
                return redirect(url_for('wawawawhannnn_template'))
            elif user.id == 4:
                return redirect(url_for('nuttakitt__template'))
        return redirect(url_for('login_template'))
    return render_template('login.html')

@app.route('/whyapar')
def whyapar_template():
    if not g.user:
        return redirect(url_for('login_template'))
    return render_template('whyapar.html')

@app.route('/pp_seen2825')
def pp_seen2825_template():
    if not g.user:
        return redirect(url_for('login_template'))
    return render_template('pp_seen2825.html')

@app.route('/wawawawhannnn')
def wawawawhannnn_template():
    if not g.user:
        return redirect(url_for('login_template'))
    return render_template('wawawawhannnn.html')

@app.route('/nuttakitt_')
def nuttakitt__template():
    if not g.user:
        return redirect(url_for('login_template'))
    return render_template('nuttakitt_.html')

@app.route('/contact')
def contact_template():
    return render_template('contact.html')

if __name__ == "__main__":
    app.debug=False
    app.run(host='0.0.0.0', port=5000)