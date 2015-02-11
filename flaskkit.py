from flask import Flask, render_template
from flask.ext.pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_HOST'] = '127.0.0.1'
app.config['MONGO_PORT'] = 27017
app.config['MONGO_DBNAME'] = 'flasktest1'
mongo = PyMongo(app, config_prefix='MONGO')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def index():
    return render_template('index.html')

@app.route('/team')
def index():
    return render_template('index.html')

@app.route('/team/<name>')
def index(name=null):
    return render_template('team.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

@app.route('/register', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

if __name__ == '__main__':
    app.run()