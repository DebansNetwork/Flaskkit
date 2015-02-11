from flask import Flask, render_template
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

app.config['MONGO_HOST'] = '127.0.0.1'
app.config['MONGO_PORT'] = 27017
app.config['MONGO_DBNAME'] = 'flasktest1'
mongo = PyMongo(app, config_prefix='MONGO')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()