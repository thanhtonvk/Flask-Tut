from flask import Flask
# render html
from flask import render_template, request, redirect, url_for
from dal.account_dal import login_account

app = Flask(__name__)


@app.route('/user/<user>')
def user(user):
    return "User page %s" % user


@app.route('/user/<int:user_id>')
def get_id(user_id):
    return "User id  = %s" % user_id


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        acc = login_account(username, password)
        if acc != None:
            # điều hướng toi route
            return redirect(url_for('home'))
        else:
            error = 'Tai khoan hoac mat khau khong chinh xac'
    return render_template("login.html", error=error)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
