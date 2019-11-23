from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import sqlite3
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




def count():
    print("Total number of projects is", Project.query.count())

def colum_names():
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



engine = create_engine(DB_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()


project1 = Project(id = 1, title="Building a Road", score = 3)
project2 = Project(id = 2, title="Local Mentoring", score = 10)
project3 = Project(id = 3, title="Mental Health Care", score = 5)
project4 = Project(id = 4, title="Durham Litter Picking", score=0)
project5 = Project(id = 5, title="Park Management", score=6)

ordered_list = session.query(Project).filter_by(Project.score).all()

print(ordered_list)

'''session.add(project1)
session.add(project2)
session.add(project3)
session.add(project4)
session.add(project5)
session.commit()'''
