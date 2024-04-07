from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
  __tablename__ = 'persons'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
  
  def __repr__(self):
    return f'<Person ID: {self.id}, name: {self.name}>'
app.app_context().push()
db.create_all()


@app.route('/')

def index(): 
  person = Person.query.first() 
  return 'Hello World!' + person.name