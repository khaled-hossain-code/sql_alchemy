from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zxc90zxc@0.0.0.0/alchemy_tutorial'
db = SQLAlchemy(app)

class Example(db.Model):
  id = db.Column('id', db.Integer, primary_key=True)
  ex_text = db.Column('ex_text', db.String(255))

