from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zxc90zxc@0.0.0.0/alchemy_tutorial'
db = SQLAlchemy(app)

subs = db.Table('subs',
  db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
  db.Column('channel_id', db.Integer, db.ForeignKey('channels.id'), primary_key=True)
)

class Users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), unique=True)


if __name__ == '__main__':
  import pdb;pdb.set_trace()
  db.create_all()
  user1 = Users(name='khaled')
  db.session.add(user1)
  db.session.commit()

  try:
    user2 = Users(name='khaled')
    db.session.add(user2)
    db.session.commit()
  except IntegrityError:
    db.session.rollback()
    print 'user already exists'

  