import sqlite3
import psycopg2
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_URL = 'sqlite:///database.db'




app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db = SQLAlchemy(app)

# Create our database model
class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)
    score = db.Column(db.Integer)
    total_funding = db.Column(db.Float, unique=False)

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False,nullable=False)
    display_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    location = db.Column(db.String(255),unique=False, nullable=False)
    credit = db.Column(db.Float, unique=False)

class Transaction(db.Model):
    __tablename__="transactions"
    id = db.Column(db.Integer, primary_key=True)
    user_key = db.Column(db.Integer, unique=True)
    project_key = db.Column(db.Integer, unique=True)
    value = db.Column(db.Float, unique=False)
    #rate = db.Column(db.Float)




def count():
    print("Total number of projects is", Project.query.count())

def colunm_names():
    print()

@app.cli.command('resetdb')
def resetdb_command():
    """Destroys and creates the database + tables."""

    from sqlalchemy_utils import database_exists, create_database, drop_database
    if database_exists(DB_URL):
        print('Deleting database.')
        drop_database(DB_URL)
    if not database_exists(DB_URL):
        print('Creating database.')
        create_database(DB_URL)

    print('Creating tables.')
    db.create_all()
    print('Shiny!')

#resetdb_command()




project1 = Project(id = 1, title="Building a Road", score = 3, total_funding=100)
project2 = Project(id = 2, title="Local Mentoring", score = 10, total_funding=100)
project3 = Project(id = 3, title="Mental Health Care", score = 5, total_funding=100)
project4 = Project(id = 4, title="Durham Litter Picking", score=0, total_funding=100)
project5 = Project(id = 5, title="Park Management", score=6, total_funding=100)


user1 = User(id =1, name="jwpetley", display_name="James Petley", email="jwpetley@gmail.com", location="Durham", credit=100)

@app.cli.command('add_sample_data')
def add_data():
    engine = create_engine(DB_URL, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(user1)


    session.add(project1)
    session.add(project2)
    session.add(project3)
    session.add(project4)
    session.add(project5)
    session.commit()

if __name__ == "__main__":
    engine = create_engine(DB_URL, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    user_list = session.query(User).first()
    print(user_list.email)

    ordered_list = session.query(Project).order_by(Project.score)
    print(ordered_list.all())
