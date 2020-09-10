from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '<h1 style="color: red">This is home page!</h1>'

@app.route('/about')
def about():
    return '<h1 style="color: red">Welcome to about page!</h1>'

if __name__ == '__main__':
    app.run(debug=True)

    
