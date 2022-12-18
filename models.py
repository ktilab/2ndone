from app import db


class Users(db.Model):
    identifier = db.Column(db.Integer,
                           primary_key=True,
                           autoincrement=True,
                           unique=True,
                           nullable=False)
    email = db.Column(db.String(30),
                      unique=True,
                      nullable=False)
    login = db.Column(db.String(30),
                      unique=True,
                      nullable=False,
                      )
    password = db.Column(db.String(30),
                         nullable=False)

