from flask import Flask, redirect, render_template, flash, url_for
from datetime import datetime
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = '159d8c5feb822966b55582cc1ad7b43c'
# app.config["SECRETE_KEY"] = ""
# import secrests
# secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='auther', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

        
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    data_posted = db.Column(db.DateTime, nullable=False, default=datetime.now())
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"post('{self.title}, '{self.data_posted}')"

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
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)

@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'blablabla@qq.com' and form.password.data == "roger":
            flash("You have been logged in!", 'success')
            redirect(url_for("home"))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template("login.html", title="Login", form=form)

if __name__ == '__main__':
    app.run(debug=True)

    
