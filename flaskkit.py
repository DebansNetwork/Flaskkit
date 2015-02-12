from flask import Flask, render_template, session
from flask.ext.pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_HOST'] = '127.0.0.1'
app.config['MONGO_PORT'] = 27017
app.config['MONGO_DBNAME'] = 'flasktest1'
mongo = PyMongo(app, config_prefix='MONGO')

@app.route('/')
def index():
	if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('index.html')

@app.route('/team')
@app.route('/team/<name>')
def team(name=None):
    return render_template('team.html', name=name)

@app.route("/login")
def login():
    return render_template('user/login.html')

@app.route("/register")
def register():
    return render_template('user/register.html')

if __name__ == '__main__':
    app.run()