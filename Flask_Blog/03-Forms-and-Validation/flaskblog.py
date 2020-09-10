from flask import Flask, redirect, render_template, flash, url_for, request, session
from datetime import timedelta
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.secret_key = '159d8c5feb822966b55582cc1ad7b43c'
# app.config["SECRETE_KRY"] = ""
# import secrests
# secrets.token_hex(16)
app.permanent_session_lifetime = timedelta(minutes=5)

posts = [
    {
        "author": "Roegr No.1",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "2020/1/1"
    },
    {
        "author": "Roger No.2",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "2020/2/2"
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)


@app.route('/about')
def about():
    return render_template("about.html", title="About")

@app.route('/register', methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data} !", "success")
        redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)

@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == '939962207@qq.com' and form.password.data == "roger":
            flash("You have been logged in!", 'success')
            redirect(url_for("home"))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template("login.html", title="Login", form=form)

@app.route('/user')
def user():
    if "user" in session:
        user_name = session["user"]    
        return f"<h1>Hello {user_name} !</h1>"
    else:
        return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(debug=True)

    
