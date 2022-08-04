from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


Config = {
  "apiKey": "AIzaSyDZL2d00nYqnDbljf3gEvtOxEmhFs3K88s",
  "authDomain": "candy-shop-a0749.firebaseapp.com",
  "projectId": "candy-shop-a0749",
  "storageBucket": "candy-shop-a0749.appspot.com",
  "messagingSenderId": "797044916392",
  "appId": "1:797044916392:web:52862eaaa038744253c29d",
  "measurementId": "G-0VFQ9F9JB6",
  "databaseURL": "https://candy-shop-a0749-default-rtdb.firebaseio.com/"
}

firebase=pyrebase.initialize_app(Config)
auth=firebase.auth()
db=firebase.database()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('index'))
        except:
            error = "Authentication failed"
            return error
    else: 
        return render_template('login.html')


@app.route('/loginnsignup', methods=['GET','POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['psw']
        username = request.form['username']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)

            user = {"usename": username, "email": email, "password": password}
            db.child("Users").child(login_session['user']['localId']).set(user)



            
            return redirect(url_for('index'))
        except:
            error = "Authentication failed"
            return error
    return render_template('loginnsignup.html')





@app.route('/shop', methods=['GET','POST'])
def shop():
    error = ""
    return render_template('shop.html')



@app.route('/cart')
def cart():
    return render_template('cart.html')



@app.route('/checkout')
def checkout():
    return render_template('checkout.html')



@app.route('/about')
def about():
    return render_template('about.html')

#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)