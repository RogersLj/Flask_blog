from flask import Flask, redirect, render_template, flash, url_for
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


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

