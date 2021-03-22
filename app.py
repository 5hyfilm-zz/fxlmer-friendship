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
users.append(User(id=1, username='whyapar', password='04582'))
users.append(User(id=2, username='pp_seen2825', password='04679'))
users.append(User(id=3, username='wawawawhannnn', password='04630'))
users.append(User(id=4, username='nuttakitt_', password='03960'))
users.append(User(id=5, username='cchanya', password='04623'))
users.append(User(id=6, username='linnyy', password='04628'))
users.append(User(id=7, username='_praewr', password='04632'))
users.append(User(id=8, username='ppuiifaii_', password='03948'))
users.append(User(id=9, username='faififfy_23', password='04683'))
users.append(User(id=10, username='tennnnie', password='04631'))
users.append(User(id=11, username='tun_ariy', password='04621'))

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

@app.route('/signin', methods=['GET', 'POST'])
def signin_template():
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
            elif user.id == 5:
                return redirect(url_for('cchanya_template'))
            elif user.id == 6:
                return redirect(url_for('linnyy_template'))
            elif user.id == 7:
                return redirect(url_for('_praewr_template'))
            elif user.id == 8:
                return redirect(url_for('ppuiifaii__template'))
            elif user.id == 9:
                return redirect(url_for('faififfy_23_template'))
            elif user.id == 10:
                return redirect(url_for('tennnnie_template'))
            elif user.id == 11:
                return redirect(url_for('tun_ariy_template'))
        return redirect(url_for('signin_template'))
    return render_template('signin.html')

@app.route('/whyapar')
def whyapar_template():
    if not g.user:
        return redirect(url_for('signin_template'))
    return render_template('friendship/whyapar.html')

@app.route('/pp_seen2825')
def pp_seen2825_template():
    if not g.user:
        return redirect(url_for('signin_template'))
    return render_template('friendship/pp_seen2825.html')

@app.route('/wawawawhannnn')
def wawawawhannnn_template():
    if not g.user:
        return redirect(url_for('signin_template'))
    return render_template('friendship/wawawawhannnn.html')

@app.route('/nuttakitt_')
def nuttakitt__template():
    if not g.user:
        return redirect(url_for('signin_template'))
    return render_template('friendship/nuttakitt_.html')

@app.route('/cchanya')
def cchanya_template():
    if not g.user:
        return redirect(url_for('signin_template'))
    return render_template('friendship/cchanya.html')

@app.route('/linnyy')
def linnyy_template():
    if not g.user:
        return redirect(url_for('signin_template'))
    return render_template('friendship/linnyy.html')

@app.route('/_praewr')
def _praewr_template():
    if not g.user:
        return redirect(url_for('signin_template'))
    return render_template('friendship/_praewr.html')

@app.route('/ppuiifaii_')
def ppuiifaii__template():
    if not g.user:
        return redirect(url_for('signin_template'))
    return render_template('friendship/ppuiifaii_.html')

@app.route('/faififfy_23')
def faififfy_23_template():
    if not g.user:
        return redirect(url_for('signin_template'))
    return render_template('friendship/faififfy_23.html')

@app.route('/tennnnie')
def tennnnie_template():
    if not g.user:
        return redirect(url_for('signin_template'))
    return render_template('friendship/tennnnie.html')

@app.route('/tun_ariy')
def tun_ariy_template():
    if not g.user:
        return redirect(url_for('signin_template'))
    return render_template('friendship/tun_ariy.html')

@app.route('/contactme')
def contact_template():
    return render_template('contactme.html')

if __name__ == "__main__":
    app.debug=False
    app.run(host='0.0.0.0', port=5000)