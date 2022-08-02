from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')



@app.route('/shop')
def shop():
    return render_template('shop.html')


@app.route('/cart')
def cart():
    return render_template('cart.html')


#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)