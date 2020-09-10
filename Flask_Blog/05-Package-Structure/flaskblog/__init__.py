from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = '159d8c5feb822966b55582cc1ad7b43c'
# app.config["SECRETE_KEY"] = ""
# import secrests
# secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes
#in case circle imports