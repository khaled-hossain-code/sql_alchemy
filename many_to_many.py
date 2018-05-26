from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zxc90zxc@0.0.0.0/alchemy_tutorial'
db = SQLAlchemy(app)

subs = db.Table('subs',
  db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
  db.Column('channel_id', db.Integer, db.ForeignKey('channels.id'), primary_key=True)
)

class Users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20))
  subscriptions = db.relationship('Channels', secondary=subs, backref=db.backref('subscribers', lazy='dynamic'))

class Channels(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20))
