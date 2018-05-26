from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.sqlalchemy import get_debug_queries

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zxc90zxc@0.0.0.0/alchemy_tutorial'
db = SQLAlchemy(app)

class Person(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  pets = db.relationship('Pet', backref='owner', lazy='dynamic')


class Pet(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))

