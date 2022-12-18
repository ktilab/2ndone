from flask import Flask


app = Flask(__name__)


from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


from routes import *


from models import Users


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()

