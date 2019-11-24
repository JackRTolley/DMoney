import sqlite3
from datetime import datetime
import psycopg2
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app import db
import os
basedir = os.path.abspath(os.path.dirname(__file__))

#DB_URL = 'sqlite:///database.db'

#app = Flask(__name__)
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
#app.config['SECRET_KEY'] = 'secret-key'


# Create our database model
#db = SQLAlchemy(app)
Base = declarative_base()
class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False,nullable=False)
    display_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    location = db.Column(db.String(255),unique=False, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    credit = db.Column(db.Float, unique=False)
    projects = db.relationship('Project',backref='users',lazy=True)
    transactions = db.relationship('Transaction',backref='users',lazy=True)


    def __repr__(self):
        return '<User {}>'.format(self.display_name)

class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable = False)
    title = db.Column(db.String(120), unique=True)
    description = db.Column(db.String(1000), unique = True)
    score = db.Column(db.Integer)
    total_funding = db.Column(db.Float, unique=False)
    transactions = db.relationship('Transaction',backref='projects',lazy=True)


    def __repr__(self):
        return '<Title {}>'.format(self.title)

class Transaction(db.Model):
    __tablename__="transactions"
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, unique=False)
    #rate = db.Column(db.Float)
    user_key = db.Column(db.Integer, db.ForeignKey('users.id'),nullable = False)
    project_key = db.Column(db.Integer, db.ForeignKey('projects.id'),nullable = False)


    def __repr__(self):
        return '<Transaction {}>'.format(self.value)

def create_database_and_session(Base):

    engine = create_engine(DB_URL, echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    return session

def populate_db(session):


    user_1 = User(id=1, )


    user_1 = User(id=1, name="Mr. Jack", display_name="Mr. Jack",   email="na1", location="Durham", credit=100)
    user_2 = User(id=2, name="Mr. James", display_name="Mr. James", email="na2", location="Durham", credit=100)
    user_3 = User(id=3, name="Ms. Laura", display_name="Ms. Laura", email="na3", location="Durham", credit=100)

    project_1 = Project(id=1, creator_id=1, title="Help Save our Cats", description="The cats are in trouble, please save them.", score=5,
    total_funding=20)

    session.add(user_1)
    session.add(user_2)
    session.add(user_3)

    session.add(project_1)

    session.commit()

def count():
    print("Total number of projects is", Project.query.count())

def colunm_names():
    print()

#@app.cli.command('resetdb')
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

#@app.cli.command('add_sample_data')
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

def get_projects_by_score():
    ordered_list = db.session.query(Project).order_by(Project.score)
    list = []
    for project in ordered_list:
        id = project.id
        name = project.title
        score = project.score
        creator = project.creator_id
        descrit = project.description
        dict = {'id':id, 'name':name, 'score':score, 'creator':creator, 'description': descrit}
        list.append(dict)
    return(list)

if __name__ == "__main__":

    session = create_database_and_session(Base)

    populate_db(session)





    '''
    print("Print")

    engine = create_engine(DB_URL, echo=True)
    #resetdb_command()
    Session = sessionmaker(bind=engine)
    session = Session()

    user1 = User(id =1, name="jwpetley", display_name="James Petley", email="jwpetley@gmail.com", location="Durham", credit=100)
    session.add(user1)
    session.commit()

    user_list = session.query(users)
    print(user_list)
    print("done")

    user_list = session.query(users).first()

    get_projects_by_score()

    project1 = Project(id = 1, title="Building a Road", score = 3, total_funding=100)
    project2 = Project(id = 2, title="Local Mentoring", score = 10, total_funding=100)
    project3 = Project(id = 3, title="Mental Health Care", score = 5, total_funding=100)
    project4 = Project(id = 4, title="Durham Litter Picking", score=0, total_funding=100)
    project5 = Project(id = 5, title="Park Management", score=6, total_funding=100)
    '''
